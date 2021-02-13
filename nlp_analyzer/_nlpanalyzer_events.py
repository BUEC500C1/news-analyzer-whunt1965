# ======================================================
# NLP API - Private ENUM event class
# ======================================================
from enum import Enum

# Enum class for events related to the NLP API
class Event(Enum):
    AnalyzeSentiment_Initiated = 1
    AnalyzeSentiment_Success = 2
    AnalyzeSentiment_Error = 3
    AnalyzeEntity_Initiated = 4
    AnalyzeEntity_Success = 5
    AnalyzeEntity_Error = 6
    AnalyzeSyntax_Initiated = 7
    AnalyzeSyntax_Success = 8
    AnalyzeSyntax_Error = 9
    AnalyzeEntitySentiment_Initiated = 10
    AnalyzeEntitySentiment_Success = 11
    AnalyzeEntitySentiment_Error = 12
    ClassifyContent_Initiated = 13
    ClassifyContent_Success = 14
    ClassifyContent_Error = 15

    # Class to-string method to support logging
    def __str__(self):
        return self.name