# Tests for file uploader module
from memory_profiler import profile
from fileuploader import *
import tracemalloc
import cProfile
import re
import json


# ==================
# Start Tests
# ==================
valid = {
    "ID":"/File/12/123",
    "Upload_Date":"2021-02-17",
    "File_Metadata": {
        "Authors":["Osama"],
        "File_Creation_Date": "1999-01-22",
        "File_Source": "Wiley",
        "File_Tags": ["Sports"],
    },
    "Text": {
        "Text_ID": '/File/12/123/456',
        "Text":["Hello, this is a test", "Its not a very good test"],
        "Sentiment": [0, -10],
        "Entity": [],
        "Entity_Sentiment": [],
        "Content_Classification": [],
    },
}

partial_valid_for_Read_and_Delete  = {
    "ID":"/File/12/123",
    "Text": {},
}

update_valid  = {
    "ID":"/File/12/123",
    "Text": {
        "Text": ["New Stuff!", "and more new stuff!"]
    },
}

expected_update_valid_output = {
    "ID":"/File/12/123",
    "Upload_Date":"2021-02-17",
    "File_Metadata": {
        "Authors":["Osama"],
        "File_Creation_Date": "1999-01-22",
        "File_Source": 'Wiley',
        "File_Tags": ["Sports"],
    },
    "Text": {
        "Text_ID": "/File/12/123/456",
        "Text":["Stuff", "and more new stuff"],
        "Sentiment": [],
        "Entity": [],
        "Entity_Sentiment": [],
        "Content_Classification": [],
    },
}

expected_partial_read_output = {
        "Text_ID": "/File/12/123/456",
        "Text":["Hello, this is a test", "Its not a very good test"],
        "Sentiment": [0, -10],
        "Entity": [],
        "Entity_Sentiment": [],
        "Content_Classification": [],
}

expected_partial_delete_output = {
    "ID":"/File/12/123",
    "Upload_Date":"2021-02-17",
    "File_Metadata": {
        "Authors":["Osama"],
        "File_Creation_Date": "1999-01-22",
        "File_Source": "Wiley",
        "File_Tags": ["Sports"],
    },
    "Text": {
        "Text_ID": "",
        "Text":[],
        "Sentiment": [],
        "Entity": [],
        "Entity_Sentiment": [],
        "Content_Classification": [],
    },
}


invalid = {
    "ID":'',
    "Upload_Date":"2021-02-17",
    "File_Metadata": {
        "Authors":["Osama"],
        "File_Creation_Date": "1999-01-22",
        "File_Source": "Wiley",
        "File_Tags": ["Sports"],
    },
    "Text": {
        "Text_ID": '/File/12/123/456',
        "Text": ["Hello, this is a test", "Its not a very good test"],
        "Sentiment": [0, -10],
        "Entity": [],
        "Entity_Sentiment": [],
        "Content_Classification": [],
    },
}

#Create Tests
# @profile
def test_create():
    l_valid = json.dumps(valid)
    l_invalid = json.dumps(invalid)
    #Correct Create
    assert create(l_valid) == (l_valid, "200 OK")
    #Invalid Create (no ID)
    assert create(l_invalid) == (l_valid, "404 Not Found")

# @profile
def test_read():
    full_file = {"ID":"/File/12/123"}
    l_full_file = json.dumps(full_file)
    invalid_file = {"ID":""}
    l_invalid_file = json.dumps(invalid_file)
    l_expected_partial_read_output = json.dumps(expected_partial_read_output)
    l_partial_valid_for_Read_and_Delete = json.dumps(partial_valid_for_Read_and_Delete)
    l_valid = json.dumps(valid)
    l_invalid = json.dumps(invalid)

    #Read full File - Expect fail for now... until DB
    assert read(l_full_file) == (l_valid, "200 OK")
    #Read Invalid File (no ID key)
    assert read(l_invalid_file) == (l_invalid_file, "404 Not Found")
    #Read partial File - Expect to fail for now
    assert read(l_partial_valid_for_Read_and_Delete) == (l_expected_partial_read_output, "200 OK")

# @profile
def test_update():
    l_update_valid = json.dumps(update_valid)
    l_expected_update_valid_output = json.dumps(expected_update_valid_output)

    invalidupdate = {"ID":"/File/12/123", "Hat": 22}
    l_invalidupdate = json.dumps(invalidupdate)
    #Valid update, expect to fail until impl
    assert update(l_update_valid) == (l_expected_update_valid_output, "200 OK")
    
    #Invalid update, expect fail until implement db
    assert update(l_invalidupdate) == (l_invalidupdate, "404 Not Found")

# @profile
def test_delete():
    l_partial_valid_for_Read_and_Delete = json.dumps(partial_valid_for_Read_and_Delete)
    l_expected_partial_delete_output = json.dumps(partial_valid_for_Read_and_Delete)
    invalid_delete = {"Text": 1234}
    l_invalid_delete = json.dumps(invalid_delete)

    #Valid delete -- expect fail until implementation
    assert delete(l_partial_valid_for_Read_and_Delete) == (l_expected_partial_delete_output, "200 OK")
    valid_delete= {"File_ID": "/File/123/1234"}
    l_invalid_delete = json.dumps(invalid_delete)
    valid_delete_out = json.loads({})
    assert delete(l_partial_valid_for_Read_and_Delete) == (valid_delete_out, "200 OK")
    #Invalid Deletes - Should work for now
    assert delete(l_invalid_delete) == (l_invalid_delete, "404 Not Found")
    invalid_delete = {}
    l_invalid_delete = json.dumps(invalid_delete)
    assert delete(l_invalid_delete) == (l_invalid_delete, "404 Not Found")

# ==================
# Ends Tests
# ==================

# #Included to show output from CPU and mem usage
def test_main():
    main()

#Print header for report
def printTitle():
    print()
    print("===FILE UPLOAD TESTS===")
    print()

# Include all test functions here to use memory and CPU profilers
def main():
    printTitle()
    tracemalloc.start()# Start trace malloc
    test_create()
    test_read()
    test_update()
    test_delete()

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat) 

if __name__ == '__main__':
    cProfile.run('main()')