# ======================================================
# NewsFeed Ingester API - Public API Functions
# ======================================================


import logging
import sys
import datetime

if __name__ == '__main__':
    import _newsfeedingester_events as ev
    import _newsfeedingester_helpers as helpers
else:
    from newsfeed_ingester import _newsfeedingester_events as ev
    from newsfeed_ingester import _newsfeedingester_helpers as helpers
import json

# Init logger
logger = logging.getLogger(__name__)  # set module level logger
# configure logging -- note: set to std:out for debug
logging.basicConfig(filename='newsfeed.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Queries newsfeed sources based on provided keyword(s)
# @param<keywords> a list of keyword(s) for the query
# @return A list of articles containing a dictionary associated with each article, including article summary and url.
#         If the query is not successful, returns an empty list
def keyword_query(keywords):
    logging.info(f"{{Event: {ev.Event.KWordQuery_Initiated}, Target: {keywords}}}")
    if keywords is None or type(keywords) != list or keywords == []:
        logging.error(f"{{Event: {ev.Event.KWordQuery_Error}, Target: {keywords}}}")
        return []
    else:
        ret = helpers.kqueryhelper(keywords)
        logging.info(f"{{Event: {ev.Event.KWordQuery_Success}, Target: {keywords}}}")
        return ret


# Queries newsfeed sources based on provided first/last name
# @param<name> the name (first last, separated by a space) of the person to query
# @return A list of articles containing a dictionary associated with each article, including article summary and url.
#         If the query is not successful, returns an empty list
def person_query(name):
    logging.info(f"{{Event: {ev.Event.PersonQuery_Initiated}, Target: {name}}}")
    if type(name) != str:
        logging.error(f"{{Event: {ev.Event.PersonQuery_Error}, Target: {name}}}")
        return []
    else:
        ret = helpers.pqueryhelper(name)
        logging.info(f"{{Event: {ev.Event.PersonQuery_Success}, Target: {name}}}")
        return ret


# Queries newsfeed sources from a given month/year based on provided keyword(s)
# @param<year> the year (as a numerical string, eg '1998') in which articles of interest would be published
# @param<month> the month (as a numerical string, eg '12') in which articles of interest would be published
# @param<keywords> a list of keyword(s) to search
# @return A list of articles containing a dictionary associated with each article, including article summary and url.
#         If the query is not successful, returns an empty list
def historical_query(year, month, keywords):
    logging.info(f"{{Event: {ev.Event.HistQuery_Initiated}, Target: {year, month, keywords}}}")
    if type(year) != str or type(month) != str or type(keywords) != list or keywords is None or keywords == []:
        logging.error(f"{{Event: {ev.Event.HistQuery_Error}, Target: {year, month, keywords}}}")
        return []
    else:
        try:
            month = int(month)
            year = int(year)
        except ValueError as E:
            logging.error(f"{{Event: {ev.Event.HistQuery_Error}, Target: {year, month, keywords}}}")
            return []
        if 0 < month < 13 and year < datetime.datetime.now().year:
            ret = helpers.histqueryhelper(year, month, keywords)
        elif year == datetime.datetime.now().year and month <= datetime.datetime.now().month:
            ret = helpers.histqueryhelper(year, month, keywords)
        else:
            logging.error(f"{{Event: {ev.Event.HistQuery_Error}, Target: {year, month, keywords}}}")
            return []
        logging.info(f"{{Event: {ev.Event.HistQuery_Success}, Target: {year, month, keywords}}}")
        return ret


