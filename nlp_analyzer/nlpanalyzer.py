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
# @return A sentiment score on the provided text
def analyze_sentiment(text):
    logging.info(f"{{action: {Event.AnalyzeSentiment_Initiated}, Target: {text[:10]}}}")
    try:
        # Insert call to helper
        logging.info(f"{{action: {Event.AnalyzeSentiment_Success}, Target: {text[:10]}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.AnalyzeSentiment_Error}, Target: {text[:10]}}}")
        return "Unable to process text"

# Performs entity analysis on a given text
# @param<text> The text on which to perform entity analysis
# @return the entities extracted from the text
def analyze_entity(text):
    logging.info(f"{{action: {Event.AnalyzeEntity_Initiated}, Target: {text[:10]}}}")
    try:
        # Insert call to helper
        logging.info(f"{{action: {Event.AnalyzeEntity_Success}, Target: {text[:10]}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.AnalyzeEntity_Error}, Target: {text[:10]}}}")
        return "Unable to process text"

# Performs syntax analysis on a given text
# @param<text> The text on which to perform syntax analysis
# @return the results of the syntactic analysis (parts of speech, etc)
def analyze_syntax(text):
    logging.info(f"{{action: {Event.AnalyzeSyntax_Initiated}, Target: {text[:10]}}}")
    try:
        # Insert call to helper
        logging.info(f"{{action: {Event.AnalyzeSyntax_Success}, Target: {text[:10]}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.AnalyzeSyntax_Error}, Target: {text[:10]}}}")
        return "Unable to process text"

# Performs sentiment analysis on entities extracted from a given text
# @param<text> The text on which to perform entity-sentiment analysis
# @return the entities (and associated sentiments) extracted from the text
def analyze_entity_sentiment(text):
    logging.info(f"{{action: {Event.AnalyzeEntitySentiment_Initiated}, Target: {text[:10]}}}")
    try:
        # Insert call to helper
        logging.info(f"{{action: {Event.AnalyzeEntitySentiment_Success}, Target: {text[:10]}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.AnalyzeEntitySentiment_Error}, Target: {text[:10]}}}")
        return "Unable to process text"

# Performs content classification on a given text
# @param<text> The text on which to perform content classification 
# @return a list of content categories that apply to the provided text
def classify_content(text):
    logging.info(f"{{action: {Event.ClassifyContent_Initiated}, Target: {text[:10]}}}")
    try:
        # Insert call to helper
        logging.info(f"{{action: {Event.ClassifyContent_Success}, Target: {text[:10]}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.ClassifyContent_Error}, Target: {text[:10]}}}")
        return "Unable to process text"

#Simple debug for log -- to be deleted
if __name__ == '__main__':
    analyze_sentiment("why, hello there!!!")
    analyze_entity("why, hello there John Doe!!!")
    analyze_syntax("Why? Hello there!!!")
    analyze_entity_sentiment("Jeremy Pruitt was fired!!!")
    classify_content("Jeremy Pruitt was fired!!!")