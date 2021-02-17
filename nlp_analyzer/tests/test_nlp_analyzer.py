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

    #Valid Test
    j = analyze_sentiment("text")
    assert type(j) is int

    #Failure Test
    k = analyze_sentiment(7)
    assert k == ""

@profile
def test_analyze_ent():

    #Success Test
    j = analyze_entity("John Doe is Great")
    assert type(j) is list

     #Failure Test
    k = analyze_entity(7)
    assert k == []

@profile
def test_analyze_ent_sent():
    #Success Test
    j = analyze_entity_sentiment("John Doe is Great")
    assert type(j) is list

     #Failure Test
    k = analyze_entity(7)
    assert k == []

@profile
def test_classify_content():
    #Success Test
    j = classify_content("John Doe is Great")
    assert type(j) is dict

     #Failure Test
    k = classify_content(7)
    assert k == {}

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
    test_analyze_ent_sent()  

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)

if __name__ == '__main__':
    cProfile.run('main()')