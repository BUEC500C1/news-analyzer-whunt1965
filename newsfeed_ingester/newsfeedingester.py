# ======================================================
# NewsFeed Ingester API - Public API Functions
# ======================================================
import logging
import sys
from _newsfeedingester_events import *
import json

#Init logger
logger = logging.getLogger(__name__) #set module level logger
#configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Queries newsfeed sources based on provided keyword(s) 
# @param<*keywords> a list of keyword(s) for the query
# @return A JSON object containing a list of articles, including article title, URL, and summary. If the query is not successful, returns an empty JSON
def keyword_query(*keywords):
    logging.info(f"{{Event: {Event.KWordQuery_Initiated}, Target: {keywords}}}")
    if keywords == None:
        logging.error(f"{{Event: {Event.KWordQuery_Error}, Target: {keywords}}}")
        ret = []
        ret = json.dumps(ret)
        return ret
    else:
        # Insert call to keyword_query helper
        logging.info(f"{{Event: {Event.KWordQuery_Success}, Target: {keywords}}}")
        hardcoded_ret = [{"Title":"Article", "URL":"fake@fakenews.com", "Summary":"This, in fact, is a fake article"}]
        ret = json.dumps(hardcoded_ret)
        return ret

# Queries newsfeed sources based on provided first/last name 
# @param<fname> the first name of the person to query
# @param<lname> the last name of the person to query
# @return A JSON object containing a list of articles, including article title, URL, and summary. If the query is not successful, returns an empty JSON
def person_query(fname, lname):
    logging.info(f"{{Event: {Event.PersonQuery_Initiated}, Target: {fname, lname}}}")
    if type(fname) != str or type(lname) != str:
        logging.error(f"{{Event: {Event.PersonQuery_Error}, Target: {fname, lname}}}")
        ret = []
        ret = json.dumps(ret)
        return ret
    else:
        # Insert call to keyword_query helper
        logging.info(f"{{Event: {Event.PersonQuery_Success}, Target: {fname, lname}}}")
        hardcoded_ret = [{"Title":"Article", "URL":"fake@fakenews.com", "Summary":"This, in fact, is a fake article"}]
        ret = json.dumps(hardcoded_ret)
        return ret

# Queries newsfeed sources from a given month/year based on provided keyword
# @param<year> the year in which articles of interest would be published
# @param<month> the month in which articles of interest would be published
# @param<keywords> the keyword(s) to search
# @return A JSON object containing a list of articles, including article title, URL, and summary. If the query is not successful, returns an empty JSON
def historical_query(year, month, *keywords):
    logging.info(f"{{Event: {Event.HistQuery_Initiated}, Target: {year, month, keywords}}}")
    if type(year) != str or type(month) != str or keywords == None:
        logging.error(f"{{Event: {Event.HistQuery_Error}, Target: {year, month, keywords}}}")
        ret = []
        ret = json.dumps(ret)
        return ret
    else:
        # Insert call to keyword_query helper
        logging.info(f"{{Event: {Event.HistQuery_Success}, Target: {year, month, keywords}}}")
        hardcoded_ret = [{"Title":"Article", "URL":"fake@fakenews.com", "Summary":"This, in fact, is a fake article"}]
        ret = json.dumps(hardcoded_ret)
        return ret


#Simple debug for log -- to be deleted
if __name__ == '__main__':
    keyword_query(10, "test", "test2")
    person_query(10, "John", "Doe") 
    historical_query(10, "June", "1997", "Space", "Mars") 
