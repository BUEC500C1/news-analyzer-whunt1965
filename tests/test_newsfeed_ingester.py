# Tests for newsfeed module
from memory_profiler import profile

import tracemalloc
import cProfile
import re


# Dummy test to test workflow
@profile
def test_placeholder():
    assert "helloworld" == "helloworld"

if __name__ == '__main__':
    test_placeholder()