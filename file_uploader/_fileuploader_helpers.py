# ======================================================
# Private Helper Functions for File Uploader API
# ======================================================

from PyPDF2 import PdfFileReader
from datetime import datetime
import json


# Generate a default file object with empty fields
def _getDefaultFileObj():
    fileobj = {
        "_id": "",
        "UID": "",
        "Upload_Date": "",
        "File_Metadata": {},
        "Text": {
            "Text": [],
            "Sentiment": [],
            "Entity": [],
            "Entity_Sentiment": [],
            "Content_Classification": [],
        },
    }
    return fileobj


# Method to generate our file object
def _generateObject(path):
    myobj = _getDefaultFileObj()
    myobj["_id"] = path
    myobj["UID"] = "user"  # update later when we add user login support
    myobj["Upload_Date"] = str(datetime.now())
    myobj["File_Metadata"] = _getMetadata(path)
    myobj["Text"]["Text"] = _generateText(path)
    # myobj = json.dumps(myobj)
    return myobj


# Method to extract file metadata
def _getMetadata(path):
    metadata = {
        "Title": "",
        "Author": "",
        "Creator": ""
    }
    with open(path, "rb") as f:
        pdf_file_obj = PdfFileReader(f)
        doc_info = pdf_file_obj.getDocumentInfo()
        metadata["Title"] = doc_info.title
        metadata["Author"] = doc_info.author
        metadata["Creator"] = doc_info.creator
    return metadata


# Generates text from a PDF file
def _generateText(path):
    text = []
    with open(path, "rb") as f:
        pdf_file_obj = PdfFileReader(f)
        numpages = pdf_file_obj.numPages
        for i in range(0, numpages):
            page = pdf_file_obj.getPage(i)
            textstring = page.extractText()
            textstring = textstring.strip().split('\n \n')
            for j in range(len(textstring)):
                textstring[j] = textstring[j].replace('\n', ' ')
                text.append(textstring[j])

    return text


if __name__ == '__main__':
    print(_generateObject('./test/test.pdf'))