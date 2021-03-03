if __name__ == '__main__':
    import sys
    import os
    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from . import db
else:
    from app_db import db

import json
from datetime import datetime


def test_users():
    user = {
        "username": "test",
        "email": "Osama@bu.edu",
        "password": 123
    }

    testdoc = {
        "Name": "1012.pdf",
        "path": "/Test/789/1012.pdf",
        "UID": "test",
        "Upload_Date": date,
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

    assert db.addUser(user) == 1
    # Test try insert same unique ID
    assert db.addUser(user) == None
    # Test get Username from email
    assert db.getUserName("Osama@bu.edu") == "test"
    # Test get hashed password
    assert db.getHashedPass("test") == 123

    # Test change hashed password
    assert db.updateUserPass("test", 234) == 1
    assert db.getHashedPass("test") == 234

    # Test Update email
    db.updateUserEmail("test", "osama@gmail.com")
    assert db.getUserName("osama@gmail.com") == "test"
    db.updateUserEmail("test", "Osama@BU.edu")  # reset for future tests

    # Test delete
    db.addDocument(testdoc)  # Insert a document for recursive deletion
    delusers, deldocs = db.deleteUser("test")
    assert delusers == 1
    assert deldocs == 1


# Data for doc tests
date = datetime.now()
document1 = {
    "Name": "1012.pdf",
    "path": "/Test/789/1012.pdf",
    "UID": "test",
    "Upload_Date": date,
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
    "Name": "3457.pdf",
    "path": "/Files/34/3457.pdf",
    "UID": "test",
    "Upload_Date": datetime.now(),
    "File_Metadata": {
        "Authors": ["Jose"],
        "File_Creation_Date": "1999-07-22",
        "File_Source": "Wiley",
        "File_Tags": ["Sports"],
    },
    "Text": {
        "Text": ["Wow", "Wow"],
        "Sentiment": [0, -10],
        "Entity": [],
        "Entity_Sentiment": [],
        "Content_Classification": [],
    },
}

modification = {"Text": {
    "Text": ["Hello, this is another test", "Its terrible"],
    "Sentiment": [0, -10],
    "Entity": [],
    "Entity_Sentiment": [],
    "Content_Classification": [],
}}


def test_docs():
    # Test add document
    assert db.addDocument(document1) == 1

    # Test get Single Document
    query = {'Name': "1012.pdf", "UID": "test"}
    q = json.loads(db.getDocument(query))
    assert q[0]['File_Metadata']["Authors"][0] == "Osama"

    #  Test that we cannot re-insert the same document
    assert db.addDocument(document1) is None

    # Test add second document and get all documents belonging to same user
    assert db.addDocument(document2) == 1

    # Test get all docs belonging to UID "test"
    q = json.loads(db.getDocuments("test"))
    for item in q:
        assert item["UID"] == "test"

    # Test modify document
    query = {'Name': "1012.pdf", "UID": "test"}
    q = json.loads(db.updateDocument(query, modification))
    assert q[0]['Text']['Text'] == ["Hello, this is another test", "Its terrible"]

    # Test delete document
    query = {'Name': "1012.pdf", "UID": "test"}
    assert db.deleteDocument(query) == 1
    q = json.loads(db.getDocument(query))
    assert q[0]["Deleted"] == "True"

    # Now reinsert document and test that deleting all documents belong to test returns correct deleted count
    assert db.addDocument(document1) == 1
    assert db.deleteAllUserDocs("test") == 2

    q = json.loads(db.getDocuments("test"))
    for item in q:
        assert item["Deleted"] == "True"

    # # Clean up unit tests from DB
    # documents = db._getDocCollection()
    # documents.delete_many({"UID": "test"})


if __name__ == '__main__':
    print("in main loop")
    test_users()
    test_docs()
