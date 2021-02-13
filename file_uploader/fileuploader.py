# ======================================================
# File Uploader API - Public API Functions
# ======================================================
import logging
import sys
from _fileuploader_events import *

#Init logger
logger = logging.getLogger(__name__) #set module level logger
#configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Uploads a file and creates an entry in the Database
# @param<myFile> the file to upload
# @return a message indicating whether the upload was successful or failed
def create(myFile):
    logging.info(f"{{Event: {Event.Upload_Initiated}, Target: {myFile}}}")
    try:
        # Insert call to create helper
        logging.info(f"{{Event: {Event.Upload_Success}, Target: {myFile}}}")
        return 'File Successfully Uploaded'
    except:
        logging.error(f"{{Event: {Event.Upload_Error}, Target: {myFile}}}")
        return "Unable to Upload this File"

# Accesor for a file or component of a file in the DB
# @param<myFile> the file to access
# @param<*attrs> the specific components of the file to access
# @return a message indicating whether the read was successful or failed
def read(myFile, *attrs):
    logging.info(f"{{Event: {Event.Read_Initiated}, Target: {myFile, attrs}}}")
    try:
        # Insert call to read helper
        logging.info(f"{{Event: {Event.Read_Success}, Target: {myFile, attrs}}}")
        return '<Results...>'
    except:
        logging.error(f"{{Event: {Event.Read_Error}, Target: {myFile, attrs}}}")
        return "Unable to read this File"

# Mutator for a file or component of a file in the DB
# @param<myFile> the file to modify
# @param<*attrs> the specific components of the file to modify
# @return a message indicating whether the modification was successful or failed
def update(myFile, *attrs):
    logging.info(f"{{Event: {Event.Update_Initiated}, Target: {myFile, attrs}}}")
    try:
        # Insert call to upload helper
        logging.info(f"{{Event: {Event.Update_Success}, Target: {myFile, attrs}}}")
        return 'Update Successful'
    except:
        logging.error(f"{{Event: {Event.Update_Error}, Target: {myFile, attrs}}}")
        return "Unable to update this File"

# Delete a file or component of a file in the DB
# @param<myFile> the file to modify (or delete entirely)
# @param<*attrs> the specific components of the file to delete
# @return a message indicating whether the deletion was successful or failed
def delete(myFile, *attrs):
    logging.info(f"{{Event: {Event.Delete_Initiated}, Target: {myFile, attrs}}}")
    try:
        # Insert call to delete helper
        logging.info(f"{{Event: {Event.Delete_Success}, Target: {myFile, attrs}}}")
        return 'Deletion Successful'
    except:
        logging.error(f"{{Event: {Event.Delete_Error}, Target: {myFile, attrs}}}")
        return "Deletion failed"

#Simple debug for log -- to be deleted
if __name__ == '__main__':
    create("test")
    read("test")
    read("test", "test1")
    update("test", "test1")
    delete("test", "test1")