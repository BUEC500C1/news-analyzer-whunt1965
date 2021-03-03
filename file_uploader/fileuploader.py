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
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Re


# Uploads a file and creates an entry in the Database
# @param<myFileObj> A path to a file to insert into the DB
# @param<userId> The username of the user creating an entry
# @return The JSON object along with a reponse code indeicating success or failure
def create(path, userId):
    logging.info(f"{{Event: {ev.Event.CREATE_Initiated}, Target: {path}}}")
    fileObj = funcs.generateObject(path, userId)
    if fileObj is None:
        logging.error(f"{{Event: {ev.Event.CREATE_Error}, Target: {path}}}")
        return path, "File could not be converted", 400
    result = db.addDocument(fileObj)
    if result:
        logging.info(f"{{Event: {ev.Event.CREATE_Success}, Target: {path}}}")
        return fileObj, 200
    else:
        logging.error(f"{{Event: {ev.Event.CREATE_Error}, Target: {path}}}")
        return path, "This Document already exists!", 400


# Accessor for a single file in the DB
# @param<fileobj> A JSON object containing fields from which the file can be referenced (eg, Title or _id) as well as
#                 the username of the individual who uploaded the file (required)
# @return If the read is successful returns the file as a JSON object containing the files found along with a Success
#         code. Otherwise, returns the original object and an error code
def read_one(fileobj):
    logging.info(f"{{Event: {ev.Event.READ_Initiated}, Target: {fileobj}}}")

    # Ensure JSON compatible input
    try:
        fileobj = json.loads(fileobj)
    except ValueError as E:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {fileobj}}}")
        return fileobj, "Invalid object (Non-JSON) for File Read Request", 400

    # Extract requested document from database
    result = json.loads(db.getDocument(fileobj))  # Extract requested document from database

    # If database returns none, file is not in database
    if result is None or result == []:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {fileobj}}}")
        return fileobj, "File Not Found", 404

    logging.info(f"{{Event: {ev.Event.READ_Success}, Target: {fileobj}}}")
    # Retrieve specific components Here and return those
    return result, "200 OK"

# Accessor for all files in the DB belonging to a single uder
# @param<fileobj> A string containing the username of the user associated with the files
# @return If the read is successful returns the file as a JSON object containing the files found along with a Success
#         code. Otherwise, returns the original object and an error code
def read_many(uid):
    logging.info(f"{{Event: {ev.Event.READ_Initiated}, Target: {uid}}}")

    # Extract requested document from database
    result = json.loads(db.getDocuments(uid))  # Extract requested documents from database

    # If database returns none, there are no files in the database belonging to this user
    if result is None or result == []:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {uid}}}")
        return uid, "Files Not Found", 404

    logging.info(f"{{Event: {ev.Event.READ_Success}, Target: {uid}}}")
    # Retrieve specific components Here and return those
    return result, "200 OK"




# Modifies a file or component of a file in the DB
# @param<identifier> A JSON object containing fields from which the file can be referenced (eg, Title or _id) as well as
#                   the username of the individual who uploaded the file (required)
# @param<myFile> A JSON string object containing the specific parameters to update
# @return If the update is successful returns updated file as a JSON object along with a Success code
#         Otherwise, returns the original objects and an error code
def update(identifier, update):
    logging.info(f"{{Event: {ev.Event.UPDATE_Initiated}, Target: {identifier, update}}}")

    # Ensure JSON compatible inputs
    try:
        identifier = json.loads(identifier)
        update = json.loads(update)
    except ValueError as E:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {identifier, update}}}")
        return identifier, update, "Invalid Request parameters", 404

    # Request to update file in database
    result = json.loads(db.updateDocument(identifier, update))

    # A none result means that the file could not be updated, return an error
    if result is None or result == []:
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {identifier, update}}}")
        return identifier, update, "Could not complete your update", 400

    # Otherwise, return the updated files
    logging.info(f"{{Event: {ev.Event.UPDATE_Success}, Target: {identifier, update}}}")
    return "Update Successful", result, 200


# Delete a file or component of a file in the DB
# @param<myFile> A JSON object containing a unique identifier (eg file name or _id) as well as UID of a file to delete
#                Note: UID is a required field
# @return If the delete is successful, returns a success message and the number of files deleted.
#         Otherwise, returns the original object and an error code
def delete(myFileObj):
    logging.info(f"{{Event: {ev.Event.DELETE_Initiated}, Target: {myFileObj}}}")

    # Ensure JSON compatible inputs
    try:
        myFileObj = json.loads(myFileObj)
    except ValueError as E:
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {myFileObj}}}")

    # Attempt to delete from DB
    result = db.deleteDocument(myFileObj)
    if result <= 0:
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {myFileObj}}}")
        return myFileObj, "Unable to delete file", 404

    # Log success and return number of documents deleted
    logging.info(f"{{Event: {ev.Event.DELETE_Success}, Target: {myFileObj}}}")
    return f"Deleted {result} documents", 200


# Simple debug for log -- to be deleted
if __name__ == '__main__':
    # print(create('./test/test.pdf', "Wiley"))
    # print(read('{"UID": "Wiley", "Name": "test.pdf"}'))
    # print(update('{"UID": "Wiley", "Name": "test.pdf"}', '{"Name": "test3.pdf"}'))
    print(read_many("Wiley"))
    # print(delete('{"UID": "Wiley", "Name": "test3.pdf"}'))

