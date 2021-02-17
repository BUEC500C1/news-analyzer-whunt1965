# ======================================================
# NLP API - Public API Functions
# ======================================================
import logging
import sys
from _nlpanalyzer_events import *

#Init logger
logger = logging.getLogger(__name__) #set module level logger
#configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Performs sentiment analysis on a given text
# @param<text> The text on which to perform sentiment analysis
# @return A sentiment score on the provided text (or an empty string if failed)
def analyze_sentiment(text):
    logging.info(f"{{Event: {Event.AnalyzeSentiment_Initiated}, Target: {text[:10]}}}")
    if type(text) is str:
        # Insert call to helper
        logging.info(f"{{Event: {Event.AnalyzeSentiment_Success}, Target: {text[:10]}}}")
        return 1 #hard coded result
    else:
        logging.error(f"{{Event: {Event.AnalyzeSentiment_Error}, Target: {text[:10]}}}")
        return ""

# Performs entity analysis on a given text
# @param<text> The text on which to perform entity analysis
# @return a list of entities extracted from the text (or an empty list if failed)
def analyze_entity(text):
    logging.info(f"{{Event: {Event.AnalyzeEntity_Initiated}, Target: {text[:10]}}}")
    if type(text) is str:
        # Insert call to helper
        logging.info(f"{{Event: {Event.AnalyzeEntity_Success}, Target: {text[:10]}}}")
        return ["John Cooper"] #hard coded result
    else:
        logging.error(f"{{Event: {Event.AnalyzeEntity_Error}, Target: {text[:10]}}}")
        return []

# Performs sentiment analysis on entities extracted from a given text
# @param<text> The text on which to perform entity-sentiment analysis
# @return a list of entitities (and associated scores) from the inputted text (or an empty list if failed)
def analyze_entity_sentiment(text):
    logging.info(f"{{Event: {Event.AnalyzeEntitySentiment_Initiated}, Target: {text[:10]}}}")
    if type(text) is str:
        # Insert call to helper
        logging.info(f"{{Event: {Event.AnalyzeEntitySentiment_Success}, Target: {text[:10]}}}")
        return [{"Entity": "John Doe", "Score": 9}]
    else:
        logging.error(f"{{Event: {Event.AnalyzeEntitySentiment_Error}, Target: {text[:10]}}}")
        return []

# Performs content classification on a given text
# @param<text> The text on which to perform content classification 
# @return a dictionary of content categories (with associated confidence) that are found in the provided text (or an empty dictionary if failed)
def classify_content(text):
    logging.info(f"{{Event: {Event.ClassifyContent_Initiated}, Target: {text[:10]}}}")
    if type(text) is str:
        # Insert call to helper
        logging.info(f"{{Event: {Event.ClassifyContent_Success}, Target: {text[:10]}}}")
        return {'/EC530': .9} #Hard code for now
    else:
        logging.error(f"{{Event: {Event.ClassifyContent_Error}, Target: {text[:10]}}}")
        return {}

#Simple debug for log -- to be deleted
if __name__ == '__main__':
    analyze_sentiment("why, hello there!!!")
    analyze_entity("why, hello there John Doe!!!")
    analyze_entity_sentiment("Jeremy Pruitt was fired!!!")
    classify_content("Jeremy Pruitt was fired!!!")