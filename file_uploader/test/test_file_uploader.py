# Tests for file uploader module
from memory_profiler import profile

from file_uploader import fileuploader as fup
from app_db import db
import tracemalloc
import json


# ==================
# Start Tests
# ==================

file = "fakedb.txt"

#Init tracemalloc
def test_init():
    tracemalloc.start()  # Start trace malloc
    f = open(file, "w")
    f.write('\n')
    f.seek(0)
    f.truncate()
    f.close()
    assert 1 == 1

# Create Tests
# @profile
def test_create():
    # Create a test user to associate with files
    user = {
        "username": "test_fileuploader",
        "email": "test_fileuploader@EC500.edu",
        "password": 123
    }

    # Correct Creates
    fileObj, code = fup.create(user["username"], "./test.pdf", test=True, fn=file)
    assert fileObj["path"] == "./test.pdf"
    assert fileObj["Name"] == "test.pdf"
    assert code == 200

    fileObj, code = fup.create(user["username"], "./test2.pdf", test=True, fn=file)
    assert fileObj["path"] == "./test2.pdf"
    assert fileObj["Name"] == "test2.pdf"
    assert code == 200

    # # Invalid Create (bad username) - Test will work with valid connection to DB, not GitHub Actions
    # un, path, msg, code = fup.create("InvalidUser", "./test2.pdf")
    # assert un == "InvalidUser"
    # assert path == "./test2.pdf"
    # assert msg == "This Document already exists!"
    # assert code == 400

    # Invalid Create (bad file path)
    un, path, msg, code = fup.create(user["username"], "./notafile.pdf", test=True, fn=file)
    assert un == user["username"]
    assert path == "./notafile.pdf"
    assert msg == "File could not be converted"
    assert code == 400

    # assert db.deleteAllUserDocs(user["username"]) == 2


# @profile
def test_read():
    # Ref to test user to associate with files
    user = {
        "username": "test_fileuploader",
        "email": "test_fileuploader@EC500.edu",
        "password": 123
    }

    query1 = '{"Name": "test.pdf"}'
    query2 = '{"Name": "test2.pdf"}'

    # Valid read one op
    obj, code = fup.read_one(user["username"], query1, test=True, fn=file)
    assert obj["path"] == "./test.pdf"
    assert code == 200

    # Valid read one op
    obj, code = fup.read_one(user["username"], query2, test=True, fn=file)
    assert obj["path"] == "./test2.pdf"
    assert code == 200

    # Invalid read one op (bad params)
    retuser, obj, msg, code = fup.read_one(user["username"], 7, test=True, fn=file)
    assert retuser == user["username"]
    assert obj == 7
    assert msg == "Invalid object (Non-JSON) for File Read Request"
    assert code == 400

    # Invalid read one op (bad query)
    retuser, obj, msg, code = fup.read_one(user["username"], '{"Name": "notafile.pdf"}', test=True, fn=file)
    assert retuser == user["username"]
    assert obj == '{"Name": "notafile.pdf"}'
    assert msg == "File Not Found"
    assert code == 404

    # valid read many - will not work without DB connection
    # w = json.loads(db.getUser(user["username"]))
    # result, code = fup.read_many(user["username"])
    # for item in result:
    #     assert item["UID"] == w["_id"]
    # assert code == 200

    # Valid read many for no DB connection
    w = user
    result, code = fup.read_many(user["username"], test=True, fn=file)
    for item in result:
        assert item["UID"] == w["username"]
    assert code == 200

    # invalid read many
    retuser, msg, code = fup.read_many("notauser", test=True, fn=file)
    assert retuser == "notauser"
    assert msg == "Files Not Found"
    assert code == 404


# Update tests
# @profile
def test_update():
    # Ref to test user to associate with files
    user = {
        "username": "test_fileuploader",
        "email": "test_fileuploader@EC500.edu",
        "password": 123
    }

    # Valid Update Test 1
    identifier = '{"Name":"test.pdf"}'
    validupdate = '{"Upload_Date":"2020-12-17"}'
    msg, obj, code = fup.update(user["username"], identifier, validupdate, test=True, fn=file)
    assert msg == "Update Successful"
    assert obj["Upload_Date"] == "2020-12-17"
    assert code == 200

    # Valid Update Test 2
    identifier = '{"Name":"test2.pdf"}'
    validupdate = '{"File_Metadata": {"Authors": ["Jose"]}}'
    msg, obj, code = fup.update(user["username"], identifier, validupdate, test=True, fn=file)
    assert msg == "Update Successful"
    assert obj["File_Metadata"]["Authors"][0] == "Jose"
    assert code == 200

    # Invalid Update - bad params
    identifier = 7
    validupdate = '{"File_Metadata": {"Authors": ["Jose"]}]'
    uname, idobj, updateobj, msg, code = fup.update(user["username"], identifier, validupdate, test=True, fn=file)
    assert uname == user["username"]
    assert idobj == 7
    assert updateobj == validupdate
    assert msg == "Invalid Request parameters"
    assert code == 400

    #Invlalid Update - bad user
    identifier = '{"Name":"test2.pdf"}'
    validupdate = '{"File_Metadata": {"Authors": ["Jose"]}}'
    uname, idobj, updateobj, msg, code = fup.update("badusername", identifier, validupdate, test=True, fn=file)
    assert uname == "badusername"
    assert idobj == identifier
    assert updateobj == validupdate
    assert msg == "Could not complete your update"
    assert code == 400


# @profile
def test_delete():
    # Ref to test user to associate with files
    user = {
        "username": "test_fileuploader",
        "email": "test_fileuploader@EC500.edu",
        "password": 123
    }

    # Invalid Delete - bad file name
    invalid_id = '{"Name":"nonexistentfile.pdf"}'
    un, obj, msg, code = fup.delete(user["username"], invalid_id, test=True, fn=file)
    assert un == user["username"]
    assert obj == invalid_id
    assert msg == "Unable to delete file"
    assert code == 404

    # Invalid Delete - bad request params
    invalid_id = 7
    un, obj, msg, code = fup.delete(user["username"], invalid_id, test=True, fn=file)
    assert un == user["username"]
    assert obj == invalid_id
    assert msg == "Invalid request Parameters"
    assert code == 400

    # Valid Delete 1
    idobj = '{"Name":"test.pdf"}'
    msg, code = fup.delete(user["username"], idobj, test=True, fn=file)
    assert msg == "Deleted 1 documents"
    assert code == 200

    idobj2 = '{"Name":"test2.pdf"}'
    msg, code = fup.delete(user["username"], idobj2, test=True, fn=file)
    assert msg == "Deleted 1 documents"
    assert code == 200


# If tests fail, ensure we still cleanup documents so new tests can run without insertion errors. Also print tracemalloc
# results
def test_cleanup():
    # Ref to test user to associate with files
    # user = {
    #     "username": "test_fileuploader",
    #     "email": "test_fileuploader@EC500.edu",
    #     "password": 123
    # }
    # db.deleteAllUserDocs(user["username"])
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)
    assert 1 == 1




#
# # ==================
# # Ends Tests
# # ==================
#
# # #Included to show output from CPU and mem usage
# def test_main():
#     main()
#
# #Print header for report
# def printTitle():
#     print()
#     print("===FILE UPLOAD TESTS===")
#     print()
#
# # Include all test functions here to use memory and CPU profilers
# def main():
#     printTitle()
#     tracemalloc.start()# Start trace malloc
#     test_create()
#     test_read()
#     test_update()
#     test_delete()
#
#     # Get snapshot
#     snapshot = tracemalloc.take_snapshot()
#     top_stats = snapshot.statistics('lineno')
#     print("[ Top 5 ]")
#     for stat in top_stats[:5]:
#         print(stat)
#
# if __name__ == '__main__':
#     cProfile.run('main()')

