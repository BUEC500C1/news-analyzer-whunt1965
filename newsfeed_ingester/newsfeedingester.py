# ======================================================
# NewsFeed Ingester API - Public API Functions
# ======================================================


import logging
import sys

if __name__ == '__main__':
    import _newsfeedingester_events as ev
else:
    from newsfeed_ingester import _newsfeedingester_events as ev
import json

# Init logger
logger = logging.getLogger(__name__)  # set module level logger
# configure logging -- note: set to std:out for debug
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Queries newsfeed sources based on provided keyword(s)
# @param<keywords> a list of keyword(s) for the query
# @return A list object containing a dictionary associated with each article, including article title, URL, and summary.
#         If the query is not successful, returns an empty list
def keyword_query(keywords):
    logging.info(f"{{Event: {ev.Event.KWordQuery_Initiated}, Target: {keywords}}}")
    if keywords is None or type(keywords) != list or keywords == []:
        logging.error(f"{{Event: {ev.Event.KWordQuery_Error}, Target: {keywords}}}")
        return []
    else:
        # Insert call to keyword_query helper
        logging.info(f"{{Event: {ev.Event.KWordQuery_Success}, Target: {keywords}}}")
        hardcoded_ret = [
            {"Title": "Article", "URL": "fake@fakenews.com", "Summary": "This, in fact, is a fake article"}]
        return hardcoded_ret


# Queries newsfeed sources based on provided first/last name
# @param<name> the name (first last, separated by a space) of the person to query
# @return A list object containing a dictionary associated with each article, including article title, URL, and summary.
#         If the query is not successful, returns an empty list
def person_query(name):
    logging.info(f"{{Event: {ev.Event.PersonQuery_Initiated}, Target: {name}}}")
    if type(name) != str:
        logging.error(f"{{Event: {ev.Event.PersonQuery_Error}, Target: {name}}}")
        return []
    else:
        # Insert call to keyword_query helper
        logging.info(f"{{Event: {ev.Event.PersonQuery_Success}, Target: {name}}}")
        hardcoded_ret = [
            {"Title": "Article", "URL": "fake@fakenews.com", "Summary": "This, in fact, is a fake article"}]
        return hardcoded_ret


# Queries newsfeed sources from a given month/year based on provided keyword(s)
# @param<year> the year in which articles of interest would be published
# @param<month> the month in which articles of interest would be published
# @param<keywords> a list of keyword(s) to search
# @return A list object containing a dictionary associated with each article, including article title, URL, and summary.
#         If the query is not successful, returns an empty list
def historical_query(year, month, keywords):
    logging.info(f"{{Event: {ev.Event.HistQuery_Initiated}, Target: {year, month, keywords}}}")
    if type(year) != str or type(month) != str or type(keywords) != list or keywords is None or keywords == []:
        logging.error(f"{{Event: {ev.Event.HistQuery_Error}, Target: {year, month, keywords}}}")
        return []
    else:
        # Insert call to keyword_query helper
        logging.info(f"{{Event: {ev.Event.HistQuery_Success}, Target: {year, month, keywords}}}")
        hardcoded_ret = [
            {"Title": "Article", "URL": "fake@fakenews.com", "Summary": "This, in fact, is a fake article"}]
        return hardcoded_ret


