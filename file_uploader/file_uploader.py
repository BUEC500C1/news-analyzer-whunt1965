# ======================================================
# File Uploader API - Public API Functions
# ======================================================

def create(myFile):
    try:
        return 'File Successfully Uploaded'
    except:
        return "Unable to Upload this File"

def read(myFile, *attrs):
    try:
        return 'Results'
    except:
        return "Unable to read this File"

def update(myFile, *attrs):
    try:
        return 'Update Successful'
    except:
        return "Unable to update this File"

def delete(myFile, *attrs):
    try:
        return 'Deletion Successful'
    except:
        return "Deletion failed"