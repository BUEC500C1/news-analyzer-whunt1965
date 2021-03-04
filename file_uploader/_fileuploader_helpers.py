# ======================================================
# Private Helper Functions for File Uploader API
# ======================================================

from PyPDF2 import PdfFileReader
from datetime import datetime
import os


# Generate a default file object with empty fields
def _getDefaultFileObj():
    fileobj = {
        "Name": "",
        "path": "",
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
def generateObject(path, userId):

    if not os.access(path, os.R_OK) and not os.path.exists(path):  # Check if file exists before processing
        return None

    myobj = _getDefaultFileObj()
    myobj["Name"] = _getDocName(path)  # Extract name from path
    myobj["path"] = path  # Add path
    myobj["UID"] = userId  # update later when we add user login support
    myobj["Upload_Date"] = str(datetime.now())  # Add upload date
    myobj["File_Metadata"] = _getMetadata(path)  # Extract and add metadata
    myobj["Text"]["Text"] = _generateText(path)  # Extract and add Text
    return myobj


def _getDocName(path):
    path = path.strip().split('/')  # Strip off whitespace and break into components by '/' delimiter
    return path[len(path)-1]  # Return last element(the name of the document)

# Method to extract file metadata
def _getMetadata(path):
    metadata = {
        "Title": "",
        "Author": "",
        "Creator": ""
    }
    f = open(path, "rb")
    pdf_file_obj = PdfFileReader(f)
    doc_info = pdf_file_obj.getDocumentInfo()
    metadata["Title"] = doc_info.title
    metadata["Author"] = doc_info.author
    metadata["Creator"] = doc_info.creator
    return metadata


# Extracts text from a PDF file
def _generateText(path):
    text = []
    with open(path, "rb") as f:
        pdf_file_obj = PdfFileReader(f)
        numpages = pdf_file_obj.numPages
        for i in range(0, numpages):
            page = pdf_file_obj.getPage(i)
            textstring = page.extractText()  # Extract all text from a single page
            textstring = textstring.strip().split('\n \n') # Split into paragraphs as possible
            for j in range(len(textstring)):  # Append each paragraph to text list
                textstring[j] = textstring[j].replace('\n', ' ')  # Remove excess newlines that may have been generated
                text.append(textstring[j])

    return text


if __name__ == '__main__':
    print(generateObject('./test/test.pdf', "Wiley"))
    print(generateObject('./test/test333.pdf', "Wiley"))