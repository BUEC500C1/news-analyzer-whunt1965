# ======================================================
# File Uploader API - Private ENUM event class
# ======================================================
from enum import Enum

# Enum class for events related to file uploader API
class Event(Enum):
    CREATE_Initiated = 1
    CREATE_Success = 2
    CREATE_Error = 3
    DELETE_Initiated = 4
    DELETE_Success = 5
    DELETE_Error = 6
    READ_Initiated = 7
    READ_Success = 8
    READ_Error = 9
    UPDATE_Initiated = 10
    UPDATE_Success = 11
    UPDATE_Error = 12

    # Class to-string method to support logging
    def __str__(self):
        return self.name

