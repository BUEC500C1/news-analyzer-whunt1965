# ======================================================
# NewsFeed Ingester API - Private Event Class
# ======================================================
from enum import Enum

# Enum class for events related to newsfeed ingester API
class Event(Enum):
    KWordQuery_Initiated = 1
    KWordQuery_Success = 2
    KWordQuery_Error = 3
    PersonQuery_Initiated = 4
    PersonQuery_Success = 5
    PersonQuery_Error = 6
    HistQuery_Initiated = 7
    HistQuery_Success = 8
    HistQuery_Error = 9

    # Class to-string method to support logging
    def __str__(self):
        return self.name