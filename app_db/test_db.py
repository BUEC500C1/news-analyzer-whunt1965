import db
from datetime import datetime

def test_users():
    user = {
        "_id": "Osama",
        "email":"Osama@bu.edu",
        "password":123
    }

    db.addUser(user)
    # Test try insert same unique ID
    assert db.addUser(user) == None 
    # Test get Username from email
    assert db.getUserName("Osama@bu.edu") == "Osama"
    # Test get hashed password
    assert db.getHashedPass("Osama") == 123
    #Test Update email
    db.updateUserEmail("Osama", "osama@gmail.com")
    assert db.getUserName("osama@gmail.com") == "Osama"
    #Test delete
    assert db.deleteUser("Osama") == 1

date = datetime.now()
document = {
        "_id":"/Test/789/1012",
        "UID":"Wiley",
        "Upload_Date": date,
        "File_Metadata": {
            "Authors":["Osama"],
            "File_Creation_Date": "2010-01-22",
            "File_Source": "Wiley",
            "File_Tags": ["Sports"],
        },
        "Text": {
            "Text":["Hello, this is a test", "Its not a very good test"],
            "Sentiment": [0, -10],
            "Entity": [],
            "Entity_Sentiment": [],
            "Content_Classification": [],
        },
    }

modification = {"Text": {
            "Text":["Hello, this is another test", "Its terrible"],
            "Sentiment": [0, -10],
            "Entity": [],
            "Entity_Sentiment": [],
            "Content_Classification": [],
        }}

modifieddoc = {
        "_id":"/Files/789/1012",
        "UID":"Wiley",
        "Upload_Date": date,
        "File_Metadata": {
            "Authors":["Osama"],
            "File_Creation_Date": "2010-01-22",
            "File_Source": "Wiley",
            "File_Tags": ["Sports"],
        },
        "Text": {
            "Text":["Hello, this is another test", "Its terrible"],
            "Sentiment": [0, -10],
            "Entity": [],
            "Entity_Sentiment": [],
            "Content_Classification": [],
        },
    }

def test_docs():

    #Test add document
    db.addDocument(document)
    assert db.getDocument("/Test/789/1012")['UID'] == "Wiley"

    #Test modify document
    db.updateDocument("/Test/789/1012", modification)
    assert db.getDocument("/Test/789/1012")['Text']['Text'] == ["Hello, this is another test", "Its terrible"]

    #Test insert doc with same id
    assert db.addDocument(document) == None

    #Test delete document
    assert db.deleteDocument("/Test/789/1012") == 1

# if __name__ == '__main__':
#     print("in main loop")
#     test_users()
#     test_docs()