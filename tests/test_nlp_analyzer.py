# Tests for nlp module
from memory_profiler import profile
import tracemalloc
import cProfile
import re

# Start trace malloc
tracemalloc.start()

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

# Get snapshot
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 5 ]")
for stat in top_stats[:5]:
    print(stat)

# Include all test functions here to use memory and CPU profilers
def main():
    test_placeholder()  

if __name__ == '__main__':
    cProfile.run('main()')