# Tests for newsfeed module
from memory_profiler import profile

import tracemalloc
import cProfile
from newsfeed_ingester import newsfeedingester as ni


# ==================
# Start Tests
# ==================

def test_keyword_query():
    printTitle()
    tracemalloc.start()# Start trace malloc

    #Valid Tests
    validquery1 = ["hats"]
    Result = ni.keyword_query(validquery1)
    assert type(Result) == list
    assert type(Result[0]) == dict

    validquery2 = ["hats", "bananas", "apples"]
    Result = ni.keyword_query(validquery2)
    assert type(Result) == list
    assert type(Result[0]) == dict

    #Invalid Test
    invalidquery1 = 1
    Result = ni.keyword_query(invalidquery1)
    assert Result == []
    invalidquery2 = []
    Result = ni.keyword_query(invalidquery2)
    assert Result == []

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)

def test_person_query():

    tracemalloc.start()# Start trace malloc
    #Valid Tests
    Result = ni.person_query("Denzel Washington")
    assert type(Result) == list
    assert type(Result[0]) == dict
    Result = ni.person_query("Javier Bardim")
    assert type(Result) == list
    assert type(Result[0]) == dict

    #Invalid Test
    Result = ni.person_query(1)
    assert Result == []
    Result = ni.person_query(["hats"])
    assert Result == []

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)

def test_historical_query():

    tracemalloc.start()# Start trace malloc

    #Valid Tests
    Result = ni.historical_query("1973", "10", ["Oil", "OPEC"])
    assert type(Result) == list
    assert type(Result[0]) == dict
    Result = ni.historical_query("1980", "10", ["Bonds", "Stocks, Ivan Boesky"])
    assert type(Result) == list
    assert type(Result[0]) == dict

    #Invalid Test
    Result = ni.historical_query(1970, "July", "cow")
    assert Result == []
    Result = ni.historical_query("1980", 6, "Covid")
    assert Result == []
    Result = ni.historical_query("1980", "13", [])
    assert Result == []
    Result = ni.historical_query("2022", "6", "President")
    assert Result == []
    Result = ni.historical_query("1980", "June", [])
    assert Result == []

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)

# ==================
# Ends Tests
# ==================


#Print header for report
def printTitle():
    print()
    print("===NEWS FEED TESTS===")
    print()
