# Tests for file uploader module
from memory_profiler import profile
from file_uploader.fileuploader import *
import tracemalloc
import cProfile
import re


# ==================
# Start Tests
# ==================

# Post Tests
@profile
def test_post():
    assert post("nonsense") == 'File Successfully Uploaded'

# Get Tests
@profile
def test_get():
    assert get("nonsense") == '<Results...>'

# Put Tests
@profile
def test_put():
    assert put("nonsense") == 'Update Successful'

# Delete Tests
@profile
def test_delete():
    assert delete("nonsense") == 'Deletion Successful'

# ==================
# Ends Tests
# ==================


#Print header for report
def printTitle():
    print()
    print("===FILE UPLOAD TESTS===")
    print()

# Include all test functions here to use memory and CPU profilers
def main():
    printTitle()
    tracemalloc.start()# Start trace malloc
    test_post()
    test_get()
    test_put()
    test_delete()  

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat) 

if __name__ == '__main__':
    cProfile.run('main()')