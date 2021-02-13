# ======================================================
# NewsFeed Ingester API - Public API Functions
# ======================================================
import logging
import sys
from _newsfeedingester_events import *

#Init logger
logger = logging.getLogger(__name__) #set module level logger
#configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Queries newsfeed sources based on provided keyword and returns a specified number of results
# @param<numresults> The number of results to return 
# @param<*keywords> a list of keyword(s) for the query
# @return A JSON object containing the results of the query
def keyword_query(numresults, *keywords):
    logging.info(f"{{action: {Event.KWordQuery_Initiated}, Target: {keywords}, NumResults: {numresults}}}")
    try:
        # Insert call to keyword_query helper
        logging.info(f"{{action: {Event.KWordQuery_Success}, Target: {keywords}, NumResults: {numresults}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.KWordQuery_Error}, Target: {keywords}, NumResults: {numresults}}}")
        return "Unable to process query"

# Queries newsfeed sources based on provided keyword and returns a specified number of results
# @param<numresults> The number of results to return 
# @param<fname> the first name of the person to query
# @param<lname> the last name of the person to query
# @return A JSON object containing the results of the query
def person_query(numresults, fname, lname):
    logging.info(f"{{action: {Event.PersonQuery_Initiated}, Target: {fname, lname}, NumResults: {numresults}}}")
    try:
        # Insert call to keyword_query helper
        logging.info(f"{{action: {Event.PersonQuery_Success}, Target: {fname, lname}, NumResults: {numresults}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.PersonQuery_Error}, Target: {fname, lname}, NumResults: {numresults}}}")
        return "Unable to process query"

# Queries newsfeed sources based on provided keyword and returns a specified number of results
# @param<numresults> The number of results to return 
# @param<year> the year in which articles of interest would be published
# @param<month> the month in which articles of interest would be published
# @param<keywords> the keyword(s) to search
# @return A JSON object containing the results of the query
def historical_query(numresults, year, month, *keywords):
    logging.info(f"{{action: {Event.HistQuery_Initiated}, Target: {year, month, keywords}, NumResults: {numresults}}}")
    try:
        # Insert call to keyword_query helper
        logging.info(f"{{action: {Event.HistQuery_Success}, Target: {year, month, keywords}, NumResults: {numresults}}}")
        return 'results'
    except:
        logging.error(f"{{action: {Event.HistQuery_Error}, Target: {year, month, keywords}, NumResults: {numresults}}}")
        return "Unable to process query"


#Simple debug for log -- to be deleted
if __name__ == '__main__':
    keyword_query(10, "test", "test2")
    person_query(10, "John", "Doe") 
    historical_query(10, "June", "1997", "Space", "Mars") 
