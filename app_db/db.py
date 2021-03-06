from pymongo import MongoClient
from bson.json_util import dumps, loads
import json
import os
import copy
import logging

# Valid identifiers for a document (in combination with UID)
docIds = ["_id", "Name"]


# Initialize DB connection
def _connect():
    key = os.getenv('MONGOKEY')
    client = MongoClient(key)
    return client


# ==========================================
# Methods for accessing Documents Collection
# ==========================================

# Get reference to Documents Collection
def _getDocCollection():
    client = _connect()
    db = client["NEWS_ANALYZER"]  # Name of Database
    documents = db["Documents"]  # Name of Collection
    return documents


# Add a document to the DB
# @param<document> A JSON document object to store in the database. Note: To prevent duplicates, the document's "Name"
#                  and "UID" fields must not match an existing (non-deleted) document in the database (ie, it must not
#                  have both the same UID and Name as another document already stored and not marked as deleted)
# @return          1 if the document is successfully added and None otherwise
def addDocument(document_input):
    documents = _getDocCollection()

    UID = _getActiveUserID(document_input["UID"]) # Ensure we have a valid user in the DB to associate with this document
    if UID is None:
        return None

    document = copy.copy(document_input)  # Create a copy so don't update fields of original document

    # Query to determine if this document already exists in the DB
    query = {"Name": document["Name"], "UID": UID, "Deleted": "False"}

    # Check if this document exists in the DB and if not, insert it
    if documents.count_documents(query) == 0:
        document["UID"] = _getActiveUserID(document["UID"])
        document["Deleted"] = "False"
        documents.insert_one(document)  # Insert document
        return 1
    else:
        return None  # Otherwise, don't insert


# Retrieve a single document from the DB
# @param<username>   A string containing the username of a user whose documents we wish to access
# @param<docobj>   A JSON object containing a valid identifier (id or Name) associated with the document
# @return          The document (as a JSON) if one is found and None otherwise
def getDocument(username, docobj):
    ids = _validateDocObj(docobj)  # Validate that this json object has the correct identifiers for a query

    UID = _getActiveUserID(username)  # Ensure we have a valid user in the DB to associate with this document

    # If no valid identifiers or username is passed, return None
    if not ids or UID is None:
        return None

    # Add valid identifiers to query
    query = dict()
    query["UID"] = UID  # Add internal UID to doc
    query["Deleted"] = "False"  # Ensure we do not fetch deleted documents
    for identifier in ids:
        query[identifier] = docobj[identifier]

    query["Deleted"] = "False"  # Ensure we do not fetch deleted documents

    documents = _getDocCollection()

    if documents.count_documents(query) == 0:  # Check if this document exists
        return None

    doc = documents.find_one(query)  # find document(s)
    ret = dumps(doc, indent=2)  # convert to JSON
    return ret


# Retrieve multiple documents belonging to a single user from the DB
# @param<UID>   A string containing the username of a user whose documents we wish to access
# @return       The documents (as a JSON) if atleast one is found and None otherwise
def getDocuments(uid):
    documents = _getDocCollection()  # Get collection

    UID = _getActiveUserID(uid)  # Retrieve UID associated with this file in DB
    query = {"UID": UID, "Deleted": "False"}  # Set query parameters

    if UID is None or documents.count_documents(query) == 0:  # Ensure there are documents in the DB
        return None

    doc = documents.find(query)  # find document(s)
    ret = dumps(doc, indent=2)  # convert to JSON
    return ret


# Update a document in DB
# @param<username>   A string containing the username of a user whose documents we wish to update
# @param<idObj>  A JSON object containing a valid identifier (id or Name) associated with the document
# @param<update> A JSON object containing the update to apply to the document
# @return        The updated document (as a JSON) or None if the query is invalid
def updateDocument(username, idObj, update):
    ids = _validateDocObj(idObj)  # Validate that this json object has the correct identifiers for a query
    UID = _getActiveUserID(username)  # Retrieve UID associated with this file in DB

    # If no valid identifiers are passed, return None
    if not ids or UID is None:
        return None

    # Add valid identifiers to query
    query = dict()
    query["Deleted"] = "False"  # Ensure we do not fetch deleted documents
    query["UID"] = UID  # Add internal UID
    for identifier in ids:
        query[identifier] = idObj[identifier]

    documents = _getDocCollection()  # Fetch collection
    newvalues = {"$set": update}  # Set update params
    result = documents.update_one(query, newvalues)  # Update document

    if result.modified_count > 0:  # If we have successfully updated the document, return the document by calling get
        objcopy = copy.copy(idObj)  # Create a shallow copy to avoid mutating original object
        if "Name" in update:
            objcopy["Name"] = update["Name"]
        obj = getDocument(username, objcopy)
        return obj


# Mark a document in the DB as deleted
# @param<username>  A string containing the username of a user whose documents we wish to delete
# @param<idObj>  A JSON object containing a valid identifier (id or Name) associated with the document
# @return        The number of documents marked as deleted
def deleteDocument(username, idObj):
    ids = _validateDocObj(idObj)  # Validate that this json object has the correct identifiers for a query
    UID = _getActiveUserID(username)  # Retrieve UID associated with this file in DB

    # If no valid identifiers are passed, return None
    if not ids or UID is None:
        return None

    # Add valid identifiers to query
    query = dict()
    query["UID"] = UID
    query["Deleted"] = "False"  # Ensure we do not fetch deleted documents
    for identifier in ids:
        query[identifier] = idObj[identifier]

    newvalues = {"$set": {"Deleted": "True"}}  # Set deleted flag on "deleted" document

    documents = _getDocCollection()
    result = documents.update_one(query, newvalues)  # Update document with deleted flag
    return result.modified_count  # Return # docs updated with deleted flag


# Mark all documents associated with a username as deleted
# @param<UID>   A string containing the username of a user who's documents we wish to mark as deleted
# @return       The number of documents marked with a deleted flag or None if no m matching users are found
def deleteAllUserDocs(username):
    documents = _getDocCollection()

    UID = _getActiveUserID(username)  # Retrieve UID associated with this file in DB

    if UID is None:  # Return None if no matching users found
        return None

    query = {"UID": _getActiveUserID(username), "Deleted": "False"}
    deletedflag = {"$set": {"Deleted": "True"}}  # Set deleted flag on "deleted" document
    result = documents.update_many(query, deletedflag)
    return result.modified_count


# Private helper method to ensure that a JSON has the correct fields to validate a document object
def _validateDocObj(docobj):
    ret = []
    for identifier in docIds:
        if identifier in docobj:
            ret.append(identifier)
    return ret


# ==========================================
# Methods for accessing Users Collection
# ==========================================

# Get reference to Users Collection
def _getUserCollection():
    client = _connect()
    db = client["NEWS_ANALYZER"]
    users = db["Users"]
    return users


# Helper method to get an id of an active user
def _getActiveUserID(username):
    user = _getUserCollection()
    query = {"username": username, "Deleted": "False"}
    if user.count_documents(query) == 1:
        userinfo = user.find_one(query)
        return userinfo.get('_id')
    else:
        return None


# Add a user to the DB
# TODO with login -- ensure emails unique
# @param<newUser>   A user object containing a unique username and email as well as a hashed password
# @return           1 if the insert is successful and None otherwise
def addUser(newuser):
    # User entities must have a username
    if "username" not in newuser or "password" not in newuser or "email" not in newuser:
        return None

    insertuser = copy.copy(newuser)  # create a copy so don't modify original object

    user = _getUserCollection()  # Get reference to collection
    query1 = {"username": newuser["username"], "Deleted": "False"}
    query2 = {"email": newuser["email"], "Deleted": "False"}

    # Check if this user (username and email) exists in the DB and if not, insert it
    if user.count_documents(query1) == 0 and user.count_documents(query2) == 0:
        insertuser["Deleted"] = "False"  # Add deleted tag
        user.insert_one(insertuser)  # Insert user
        return 1

    # Otherwise, return None
    else:
        return None  # Otherwise, don't insert


# Retrieve User info from username
# @param<username>   A username (string) to be queried in the DB
# @return            The entry for this user in the DB (as a JSON) or None if no user is found
def getUser(username):
    user = _getUserCollection()
    query = {"username": username, "Deleted": "False"}
    user_info = user.find_one(query)
    ret = dumps(user_info, indent=2)
    return ret


# Retrieve a username from an email
# @param<email>   An email (string) to be queried in the DB
# @return         The username for this user in the DB (as a JSON) or None if no user is found
def getUserName(email):
    user = _getUserCollection()
    query = {"email": email, "Deleted": "False"}
    user_info = user.find_one(query)
    if user_info is not None:
        list_cur = dict(user_info)
        if list_cur:
            username = list_cur["username"]
            return username
    return None


# Retrieve a hashed password for a user (to be used by login)
# @param<username>   A username (string) to be queried in the DB
# @return            The hashed password for this user or None if no user is found
def getHashedPass(username):
    user = _getUserCollection()
    query = {"username": username, "Deleted": "False"}
    user_info = user.find_one(query)
    ret = json.loads(dumps(user_info, indent=2))

    if ret:  # Check if a user exists for this username
        return ret["password"]

    return None


# Update a user's email in the DB
# # TODO with login -- ensure emails unique
# @param<username>   A username (string) to be queried in the DB
# @param<update>     The new value for a user's email
# @return            1 if successful and 0 otherwise
def updateUserEmail(username, update):
    user = _getUserCollection()
    testquery = {"email": update, "Deleted": "False"}
    if user.count_documents(testquery) == 0:
        query = {"username": username, "Deleted": "False"}
        newvalues = {"$set": {"email": update}}
        result = user.update_one(query, newvalues)
        return result.modified_count
    return None


# Update a user's password in the DB
# @param<username>   A username (string) to be queried in the DB
# @param<update>     The new value for a user's hashed password
# @return            The number of passwords updated (1 if successful and 0 otherwise)
def updateUserPass(username, update):
    user = _getUserCollection()
    query = {"username": username, "Deleted": "False"}
    newvalues = {"$set": {"password": update}}
    result = user.update_one(query, newvalues)
    return result.modified_count


# Mark a user as deleted in the DB and mark all associated documents as deleted
# @param<username>   A username (string) to be queried in the DB
# @return A tuple containing the number of users deleted and the number of documents deleted
def deleteUser(username):
    user = _getUserCollection()
    docsdeleted = deleteAllUserDocs(username)  # Recursively mark as deleted all documents associated with user
    query = {"username": username, "Deleted": "False"}
    update = {"$set": {"Deleted": "True"}}
    result = user.update_one(query, update)
    return result.modified_count, docsdeleted
