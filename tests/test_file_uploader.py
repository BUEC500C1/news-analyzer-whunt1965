# Tests for file uploader module
from memory_profiler import profile
import tracemalloc
import cProfile
import re


# ==================
# Start Tests
# ==================

# Dummy test to test workflow
@profile
def test_placeholder():
    assert "helloworld" == "helloworld"

# ==================
# Ends Tests
# ==================

# ==================
# Tracemalloc utils
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
    test_placeholder()  

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat) 

if __name__ == '__main__':
    cProfile.run('main()')