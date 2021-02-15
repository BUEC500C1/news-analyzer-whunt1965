# ======================================================
# File Uploader API - Private ENUM event class
# ======================================================
from enum import Enum

# Enum class for events related to file uploader API
class Event(Enum):
    POST_Initiated = 1
    POST_Success = 2
    POST_Error = 3
    DELETE_Initiated = 4
    DELETE_Success = 5
    DELETE_Error = 6
    GET_Initiated = 7
    GET_Success = 8
    GET_Error = 9
    PUT_Initiated = 10
    PUT_Success = 11
    PUT_Error = 12

    # Class to-string method to support logging
    def __str__(self):
        return self.name

