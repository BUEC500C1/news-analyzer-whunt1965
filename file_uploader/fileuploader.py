# ======================================================
# File Uploader API - Public API Functions
# See documentation for required input format
# ======================================================
import logging
import sys
import json
import _fileuploader_events as ev

#Init logger
logger = logging.getLogger(__name__) #set module level logger
#configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
#Re


# Uploads a file and creates an entry in the Database
# @param<myFileObj> A JSON object of a file conforming to input format specified in the API documentation
# @return The JSON object along with a reponse code indeicating success or failure
def create(myFileObj):
    logging.info(f"{{Event: {ev.Event.CREATE_Initiated}, Target: {myFileObj}}}")
    fileObj = json.loads(myFileObj)
    if (fileObj["ID"] == None) or fileObj["ID"] == "":
        logging.error(f"{{Event: {ev.Event.CREATE_Error}, Target: {myFileObj}}}")
        return(myFileObj, "404 Not Found")
    logging.info(f"{{Event: {ev.Event.CREATE_Success}, Target: {myFileObj}}}")
    return (myFileObj, "200 OK")


# Accessor for a file or component of a file in the DB
# @param<myFileObj> A JSON object containing the file ID and (optionally) the specific parameters to read
# @return If the read is successful returns the file (or specified subcomponents of a file) as a JSON object along with a Success code
#         Otherwise, returns the original object and an error code
def read(myFileObj):
    logging.info(f"{{Event: {ev.Event.READ_Initiated}, Target: {myFileObj}}}")
    fileObj = json.loads(myFileObj)
    if (fileObj["ID"] == None) or fileObj["ID"] == "":
        logging.error(f"{{Event: {ev.Event.READ_Error}, Target: {myFileObj}}}")
        return(myFileObj, "404 Not Found")
    logging.info(f"{{Event: {ev.Event.READ_Success}, Target: {myFileObj}}}")
    # Retrieve specific components Here and return those
    return (myFileObj, "200 OK")


# Modifies a file or component of a file in the DB
# @param<myFile> A JSON object containing the file ID and the specific parameters to update
# @return If the update is successful returns updated file as a JSON object along with a Success code
#         Otherwise, returns the original object and an error code
def update(myFileObj):
    logging.info(f"{{Event: {ev.Event.UPDATE_Initiated}, Target: {myFileObj}}}")
    fileObj = json.loads(myFileObj)
    if (fileObj["ID"] == None) or fileObj["ID"] == "":
        logging.error(f"{{Event: {ev.Event.UPDATE_Error}, Target: {myFileObj}}}")
        return(myFileObj, "404 Not Found")
    # updates file and returns new version here
    logging.info(f"{{Event: {ev.Event.UPDATE_Success}, Target: {myFileObj}}}")
    return (myFileObj, "200 OK")


# Delete a file or component of a file in the DB
# @param<myFile> A JSON object containing the file ID and the specific parameters to delete. If no parameters others than the
#                the file ID are specified, deletes the entire file
# @return If the delete is successful, returns the updated file (an empty object if the entire file is deleted) and a message code indicating success.
#         Otherwise, returns the original object and an error code
def delete(myFileObj):
    logging.info(f"{{Event: {ev.Event.DELETE_Initiated}, Target: {myFileObj}}}")
    fileObj = json.loads(myFileObj)
    if (fileObj["ID"] == None) or fileObj["ID"] == "":
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {myFileObj}}}")
        return(myFileObj, "404 Not Found")
    # deletes file (or components) and returns empty JSON (or new version here)
    logging.info(f"{{Event: {ev.Event.DELETE_Success}, Target: {myFileObj}}}")
    return (myFileObj, "200 OK")


#Simple debug for log -- to be deleted
if __name__ == '__main__':
    test = {"ID":"/File/123/1234"}
    test = json.dumps(test)
    create(test)
    read(test)
    update(test)
    delete(test)