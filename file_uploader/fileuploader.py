# ======================================================
# File Uploader API - Public API Functions
# ======================================================
import logging
import sys
import _fileuploader_events as ev

#Init logger
logger = logging.getLogger(__name__) #set module level logger
#configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Uploads a file and creates an entry in the Database
# @param<myFile> the file to upload
# @return a message indicating whether the upload was successful or failed
def post(myFile):
    logging.info(f"{{Event: {ev.Event.POST_Initiated}, Target: {myFile}}}")
    try:
        # Insert call to create helper
        logging.info(f"{{Event: {ev.Event.POST_Success}, Target: {myFile}}}")
        return 'File Successfully Uploaded'
    except:
        logging.error(f"{{Event: {ev.Event.POST_Error}, Target: {myFile}}}")
        return "Unable to Upload this File"

# Accesor for a file or component of a file in the DB
# @param<myFile> the file to access
# @param<*attrs> the specific components of the file to access
# @return a message indicating whether the read was successful or failed
def get(myFile, *attrs):
    logging.info(f"{{Event: {ev.Event.GET_Initiated}, Target: {myFile, attrs}}}")
    try:
        # Insert call to read helper
        logging.info(f"{{Event: {ev.Event.GET_Success}, Target: {myFile, attrs}}}")
        return '<Results...>'
    except:
        logging.error(f"{{Event: {ev.Event.GET_Error}, Target: {myFile, attrs}}}")
        return "Unable to read this File"

# Modified\s a file or component of a file in the DB
# @param<myFile> the file to modify
# @param<*attrs> the specific components of the file to modify
# @return a message indicating whether the modification was successful or failed
def put(myFile, *attrs):
    logging.info(f"{{Event: {ev.Event.PUT_Initiated}, Target: {myFile, attrs}}}")
    try:
        # Insert call to upload helper
        logging.info(f"{{Event: {ev.Event.PUT_Success}, Target: {myFile, attrs}}}")
        return 'Update Successful'
    except:
        logging.error(f"{{Event: {ev.Event.PUT_Error}, Target: {myFile, attrs}}}")
        return "Unable to update this File"

# Delete a file or component of a file in the DB
# @param<myFile> the file to modify (or delete entirely)
# @param<*attrs> the specific components of the file to delete
# @return a message indicating whether the deletion was successful or failed
def delete(myFile, *attrs):
    logging.info(f"{{Event: {ev.Event.DELETE_Initiated}, Target: {myFile, attrs}}}")
    try:
        # Insert call to delete helper
        logging.info(f"{{Event: {ev.Event.DELETE_Success}, Target: {myFile, attrs}}}")
        return 'Deletion Successful'
    except:
        logging.error(f"{{Event: {ev.Event.DELETE_Error}, Target: {myFile, attrs}}}")
        return "Deletion failed"

#Simple debug for log -- to be deleted
if __name__ == '__main__':
    post("test")
    get("test")
    get("test", "test1")
    put("test", "test1")
    delete("test", "test1")