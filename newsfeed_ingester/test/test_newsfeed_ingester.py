# Tests for newsfeed module
from memory_profiler import profile

import tracemalloc
import cProfile
import re
from newsfeedingester import *
import json


# ==================
# Start Tests
# ==================

# Dummy test to test workflow
@profile
def test_keyword_query():

    #Valid Tests
    validquery1 = "hats"
    Result = keyword_query(validquery1)
    assert type(Result) == list
    validquery2 = ["hats", "bananas", "apples"]
    Result = keyword_query(validquery2)
    assert type(Result) == list

    #Invalid Test
    invalidquery1 = 1
    Result = keyword_query(invalidquery1)
    assert Result == []
    invalidquery2 = []
    Result = keyword_query(invalidquery2)
    assert Result == []

@profile
def test_person_query():
    #Valid Tests
    Result = person_query("Osama Alshaykh")
    assert type(Result) == list
    Result = person_query("Javier Bardim")
    assert type(Result) == list

    #Invalid Test
    Result = person_query(1)
    assert Result == []
    Result = person_query(["hats"])
    assert Result == []

@profile
def test_historical_query():
    #Valid Tests
    Result = historical_query("1970", "June", ["Oil"])
    assert type(Result) == list
    Result = historical_query("1980", "January", ["Bonds"])
    assert type(Result) == list

    #Invalid Test
    Result = historical_query(1, 2, "cow")
    assert Result == []
    Result = historical_query(1980, "June", "Covid")
    assert Result == []
    Result = historical_query("1980", "June", [])
    assert Result == []

# ==================
# Ends Tests
# ==================


#Print header for report
def printTitle():
    print()
    print("===NEWS FEED TESTS===")
    print()

# Include all test functions here to use memory and CPU profilers
def main():
    printTitle()
    tracemalloc.start()# Start trace malloc
    test_keyword_query()
    test_person_query()
    test_historical_query() 

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)

if __name__ == '__main__':
    cProfile.run('main()')