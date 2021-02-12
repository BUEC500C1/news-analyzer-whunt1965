# Tests for nlp module

import tracemalloc
import cProfile
import re

# Start trace malloc
tracemalloc.start()
# Dummy test to test workflow
def test_placeholder():
    assert "helloworld" == "helloworld"

# Get snapshot
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
