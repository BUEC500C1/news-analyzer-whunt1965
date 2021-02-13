# ======================================================
# File Uploader API - Private ENUM event class
# ======================================================
from enum import Enum

# Enum class for events related to file uploader API
class Event(Enum):
    Upload_Initiated = 1
    Upload_Success = 2
    Upload_Error = 3
    Delete_Initiated = 4
    Delete_Success = 5
    Delete_Error = 6
    Read_Initiated = 7
    Read_Success = 8
    Read_Error = 9
    Update_Initiated = 10
    Update_Success = 11
    Update_Error = 12

    # Class to-string method to support logging
    def __str__(self):
        return self.name

