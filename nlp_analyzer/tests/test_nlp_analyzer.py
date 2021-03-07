# Tests for nlp module
from memory_profiler import profile
import tracemalloc
import cProfile
import re
from nlpanalyzer import *


# ==================
# Start Tests
# ==================

# Dummy test to test workflow
@profile
def test_analyze_sent():

    #Valid Tests
    j = analyze_sentiment("text")
    assert type(j) is int
    j = analyze_sentiment("more text")
    assert type(j) is int

    #Failure Tests
    k = analyze_sentiment(7)
    assert k == ""
    k = analyze_sentiment([])
    assert k == ""

@profile
def test_analyze_ent():

    #Success Tests
    j = analyze_entity("John Doe is Great")
    assert type(j) is list
    j = analyze_entity("I love Nascar")
    assert type(j) is list

     #Failure Tests
    k = analyze_entity(7)
    assert k == []
    k = analyze_entity(None)
    assert k == []

@profile
def test_analyze_ent_sent():

    #Success Tests
    j = analyze_entity_sentiment("John Doe is Great")
    assert type(j) is list
    j = analyze_entity_sentiment("Denzel Washington is awful")
    assert type(j) is list

     #Failure Tests
    k = analyze_entity_sentiment(7)
    assert k == []
    k = analyze_entity_sentiment({"Hello"})
    assert k == []

@profile
def test_classify_content():
    #Success Tests
    j = classify_content("John Doe is Great")
    assert type(j) is list
    if j:
        assert type(j[0]) is dict
    j = classify_content("Tractors, Tractors, Tractors")
    if j:
        assert type(j[0]) is list

     #Failure Test
    k = classify_content(None)
    assert k == []
    k = classify_content(16)
    assert k == []

# ==================
# Ends Tests
# ==================

#Included to show output from CPU and mem usage
def test_main():
    main()

#Print header for report
def printTitle():
    print()
    print("===NLP ANALYZER TESTS===")
    print()

# Include all test functions here to use memory and CPU profilers
def main():
    printTitle()
    tracemalloc.start()# Start trace malloc
    test_analyze_sent()
    test_analyze_ent()
    test_analyze_ent_sent()
    test_classify_content()  

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)

if __name__ == '__main__':
    cProfile.run('main()')