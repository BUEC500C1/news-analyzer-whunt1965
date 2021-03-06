# ======================================================
# File Uploader API - Public API Functions
# See documentation for required input format
# ======================================================
import logging
import sys
import json

import sys

if __name__ == '__main__':
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    import _fileuploader_events as ev
    import _fileuploader_helpers as funcs
    from app_db import db

else:
    from file_uploader import _fileuploader_events as ev
    from file_uploader import _fileuploader_helpers as funcs
    from app_db import db

# Init logger
logger = logging.getLogger(__name__)  # set module level logger
# configure logging -- note: set to std:out for debug
logging.basicConfig(filename='example.log', format='%(asctime)s %(levelname)s %(message)s')


# Re


# Uploads a file, parses it into JSON, and creates an entry in the Database
# @param<username> The username of the user creating an entry
# @param<path> A path to a file to insert into the DB
# @return If successful, returns the JSON version of the file and a success response code. Otherwise, returns the
#         original parameters and an error code
def create(username, path):
    logging.info(f"{{Event: {ev.Event.CREATE_Initiated}, Target: {path, username}}}")
    fileObj = funcs.generateObject(path, username)
    if fileObj is None:
        logging.error(f"{{Event: {ev.Event.CREATE_Error}, Target: {path, username}}}")
        return username, path, "File could not be converted", 400
    result = db.addDocument(fileObj)
    if result:
        logging.info(f"{{Event: {ev.Event.CREATE_Success}, Target: {path, username}}}")
        return fileObj, 200
    else:
        logging.error(f"{{Event: {ev.Event.CREATE_Error}, Target: {path, username}}}")
        return username, path, "This Document already exists!", 400


# Accessor for a single file in the DB
# @param<username> A string containing the username of the user associated with the files
# @param<fileobj> A (stringified) JSON object containing fields from which the file can be referenced (eg, Title or _id)
# @return If the read is successful returns the file as a JSON object containing the file found along with a Success
#         code. Otherwise, returns the original object, username, and an error code
def read_one(username, fileobj):
    logging.info(f"{{Event: {ev.Event.READ_Initiated}, Target: {fileobj, username}}}")

    # Ensure JSON compatible input
    try:
        db_fileobj = json.loads(fileobj)
    except ValueError as E:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {fileobj, username}}}")
        return username, fileobj, "Invalid object (Non-JSON) for File Read Request", 400
    except TypeError as E:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {fileobj, username}}}")
        return username, fileobj, "Invalid object (Non-JSON) for File Read Request", 400

    # Extract requested document from database
    result = db.getDocument(username, db_fileobj)  # Extract requested document from database

    # If database returns none, file is not in database
    if result is None or result == []:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {fileobj, username}}}")
        return username, fileobj, "File Not Found", 404
    # Otherwise return result
    else:
        result = json.loads(result)
        logging.info(f"{{Event: {ev.Event.READ_Success}, Target: {fileobj, username}}}")
        return result, 200


# Accessor for all files in the DB belonging to a single user
# @param<username> A string containing the username of the user associated with the files
# @return If the read is successful returns the file as a JSON object containing the files found along with a Success
#         code. Otherwise, returns the username and an error code
def read_many(username):
    logging.info(f"{{Event: {ev.Event.READ_Initiated}, Target: {username}}}")

    # Extract requested document from database
    result = db.getDocuments(username)  # Extract requested documents from database

    # If database returns none, there are no files in the database belonging to this user
    if result is None or result == []:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {username}}}")
        return username, "Files Not Found", 404
    # Otherwise return result
    else:
        result = json.loads(result)
        logging.info(f"{{Event: {ev.Event.READ_Success}, Target: {username}}}")
        return result, 200


# Modifies a file in the DB
# @param<username> A string containing the username of the user associated with the files
# @param<identifier> A JSON object containing fields from which the file can be referenced (eg, Title or _id)
# @param<update> A JSON string object containing the specific parameters to update
# @return If the update is successful returns updated file as a JSON object along with a Success code
#         Otherwise, otherwise returns the original parameters and an error code
def update(username, identifier, updateObj):
    logging.info(f"{{Event: {ev.Event.UPDATE_Initiated}, Target: {username, identifier, updateObj}}}")

    # Ensure JSON compatible inputs
    try:
        db_identifier = json.loads(identifier)
        db_update = json.loads(updateObj)
    except ValueError as E:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {username, identifier, updateObj}}}")
        return username, identifier, updateObj, "Invalid Request parameters", 400
    except TypeError as E:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {username, identifier, updateObj}}}")
        return username, identifier, updateObj, "Invalid Request parameters", 400


    # Request to update file in database
    result = db.updateDocument(username, db_identifier, db_update)

    # A none result means that the file could not be updated, return an error
    if result is None or result == []:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {identifier, updateObj}}}")
        return username, identifier, updateObj, "Could not complete your update", 400
    # Otherwise, return the updated files
    else:
        result = json.loads(result)
        logging.info(f"{{Event: {ev.Event.UPDATE_Success}, Target: {identifier, updateObj}}}")
        return "Update Successful", result, 200


# Delete a file in the DB
# @param<username> A string containing the username of the user associated with the files
# @param<fileObj> A JSON object containing a unique identifier (eg file name or _id) associated with the file to delete.
# @return If the delete is successful, returns a success message and the number of files deleted.
#         Otherwise, returns the original object and an error code
def delete(username, fileObj):
    logging.info(f"{{Event: {ev.Event.DELETE_Initiated}, Target: {username, fileObj}}}")

    # Ensure JSON compatible inputs
    try:
        db_fileObj = json.loads(fileObj)
    except ValueError as E:
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {username, fileObj}}}")
        return username, fileObj, "Invalid request Parameters", 400
    except TypeError as E:
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {username, fileObj}}}")
        return username, fileObj, "Invalid request Parameters", 400

    # Attempt to delete from DB
    result = db.deleteDocument(username, db_fileObj)
    if result <= 0 or result is None:
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {username, fileObj}}}")
        return username, fileObj, "Unable to delete file", 404

    # Log success and return number of documents deleted
    logging.info(f"{{Event: {ev.Event.DELETE_Success}, Target: {username, fileObj}}}")
    return f"Deleted {result} documents", 200


# # Simple debug for log -- to be deleted
# if __name__ == '__main__':
#     # print(create('./test/test.pdf', "Wiley"))
#     # print(read('{"UID": "Wiley", "Name": "test.pdf"}'))
#     # print(update('{"UID": "Wiley", "Name": "test.pdf"}', '{"Name": "test3.pdf"}'))
#     print(read_many("Wiley"))
#     # print(delete('{"UID": "Wiley", "Name": "test3.pdf"}'))
