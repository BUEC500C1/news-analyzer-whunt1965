from pymongo import MongoClient
import os

# connection key
key = os.getenv('MONGOKEY')


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
    db = client["NEWS_ANALYZER"]
    documents = db["Documents"]
    return documents


# Add a document to the DB
def addDocument(document):
    documents = _getDocCollection()
    try:  # An exception will be returned if the id is taken
        result = documents.insert_one(document)
        return result
    except:
        return None


# Retrieve a document from the DB
def getDocument(doc_id):
    documents = _getDocCollection()
    query = {"_id": doc_id}
    doc = documents.find(query)
    return list(doc)[0]


# Update a document in DB
def updateDocument(doc_id, update):
    documents = _getDocCollection()
    query = {"_id": doc_id}
    newvalues = {"$set": update}
    result = documents.update_one(query, newvalues)
    return result


# Delete a document in DB
def deleteDocument(doc_id):
    documents = _getDocCollection()
    query = {"_id": doc_id}
    result = documents.delete_one(query)
    return result.deleted_count


def deleteAllUserDocs(username):
    documents = _getDocCollection()
    query = {"UID": username}
    result = documents.delete_many(query)
    return result.deleted_count


# To do -- add multi delete to accomodate user deleting account

# ==========================================
# Methods for accessing Users Collection
# ==========================================

# Get reference to Users Collection
def _getUserCollection():
    client = _connect()
    db = client["NEWS_ANALYZER"]
    users = db["Users"]
    return users


# Add a document to the DB
def addUser(newuser):
    user = _getUserCollection()
    try:  # An exception will be returned if this id is taken
        result = user.insert_one(newuser)
        return result
    except:
        return None


# Retrieve User info from user Id
def getUser(username):
    user = _getUserCollection()
    query = {"_id": username}
    user_info = user.find(query)
    return user_info


# Retrieve a username from an email
def getUserName(email):
    user = _getUserCollection()
    query = {"email": email}
    user_info = user.find(query)
    return list(user_info)[0]["_id"]


# Retrieve a hashed password for a user (to be used by login)
def getHashedPass(username):
    user = _getUserCollection()
    query = {"_id": username}
    user_info = user.find(query)
    return list(user_info)[0]["password"]


# Update a user's email in the DB
def updateUserEmail(username, update):
    user = _getUserCollection()
    query = {"_id": username}
    newvalues = {"$set": {"email": update}}
    result = user.update_one(query, newvalues)
    return result


# Update a user's password in the DB
def updateUserPass(username, update):
    user = _getUserCollection()
    query = {"_id": username}
    newvalues = {"$set": {"password": update}}
    result = user.update_one(query, newvalues)
    return result


# Delete a document in DB
def deleteUser(username):
    user = _getUserCollection()
    query = {"_id": username}
    result = user.delete_one(query)
    # To-do recursively delete all documents associated with user
    return result.deleted_count


if __name__ == '__main__':
    from datetime import datetime

    user1 = {
        "_id": "Wiley",
        "email": "whunt@bu.edu",
        "password": 5678
    }
    user2 = {
        "_id": "test1",
        "email": "test1@bu.edu",
        "password": 123
    }
    print(addUser(user1))
    print(addUser(user2))

    document = {
        "_id": "/Files/56/567",
        "UID": "Wiley",
        "Upload_Date": datetime.now(),
        "File_Metadata": {
            "Authors": ["Osama"],
            "File_Creation_Date": "2010-01-22",
            "File_Source": "Wiley",
            "File_Tags": ["Sports"],
        },
        "Text": {
            "Text": ["Hello, this is a test", "Its not a very good test"],
            "Sentiment": [0, -10],
            "Entity": [],
            "Entity_Sentiment": [],
            "Content_Classification": [],
        },
    }

    document2 = {
        "_id": "/Files/34/3457",
        "UID": "Wiley",
        "Upload_Date": datetime.now(),
        "File_Metadata": {
            "Authors": ["Osama"],
            "File_Creation_Date": "1999-07-22",
            "File_Source": "Wiley",
            "File_Tags": ["Sports"],
        },
        "Text": {
            "Text": ["Hello, this is a test", "Its not a very good test"],
            "Sentiment": [0, -10],
            "Entity": [],
            "Entity_Sentiment": [],
            "Content_Classification": [],
        },
    }
    addDocument(document)
    addDocument(document2)
