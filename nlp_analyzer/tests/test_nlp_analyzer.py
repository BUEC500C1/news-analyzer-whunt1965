# Tests for nlp module
from memory_profiler import profile
import tracemalloc
import cProfile
import re
from nlp_analyzer import nlpanalyzer as np


# ==================
# Start Tests
# ==================

def test_analyze_sent():
    printTitle()
    tracemalloc.start()  # Start trace malloc

    #Valid Tests
    j = np.analyze_sentiment("text")
    assert type(j) is float
    j = np.analyze_sentiment("more text")
    assert type(j) is float

    #Failure Tests
    k = np.analyze_sentiment(7)  # Not a string
    assert k == ""
    k = np.analyze_sentiment([])  # Not a string
    assert k == ""

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)


def test_analyze_ent():
    tracemalloc.start()  # Start trace malloc

    #Success Tests
    j = np.analyze_entity("John Kerry is Great")
    assert type(j) is list
    if j:
        assert type(j[0]) is str
    j = np.analyze_entity("I love NASCAR")
    assert type(j) is list
    if j:
        assert type(j[0]) is str

     #Failure Tests
    k = np.analyze_entity(7)  # Not a string
    assert k == []
    k = np.analyze_entity(None)  # Not a string
    assert k == []

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)


def test_analyze_ent_sent():

    tracemalloc.start()  # Start trace malloc

    #Success Tests
    j = np.analyze_entity_sentiment("John Kerry is Great")
    assert type(j) is list
    if j:
        assert type(j[0]) is dict
    j = np.analyze_entity_sentiment("Denzel Washington is awful. That's a joke")
    assert type(j) is list
    if j:
        assert type(j[0]) is dict

     #Failure Tests
    k = np.analyze_entity_sentiment(7)  # Not a string
    assert k == []
    k = np.analyze_entity_sentiment({"Hello"})  # Not a string
    assert k == []

    # Get snapshot
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 5 ]")
    for stat in top_stats[:5]:
        print(stat)


def test_classify_content():

    tracemalloc.start()  # Start trace malloc

    #Success Tests
    text = "I hate Bruce Willis. But I love Brad Pitt and I feel very strongly about Claude Van Damme. That is all " \
           "I want to say"
    j = np.classify_content(text)
    assert type(j) is list
    if j:
        assert type(j[0]) is dict
    text2 = "Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, " \
            "Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, Tractors, " \
            "Tractors, Tractors,"
    j = np.classify_content(text2)
    if j:
        assert type(j[0]) is dict

     #Failure Tests
    k = np.classify_content("This is a test")  # Under 20 words
    assert k == []
    k = np.classify_content(None)  # Not a string
    assert k == []
    k = np.classify_content(16)  # Not a string
    assert k == []

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
    print("===NLP ANALYZER TESTS===")
    print()
