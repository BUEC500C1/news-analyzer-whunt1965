# ======================================================
# NewsFeed Ingester API - Private API Helper Functions
# ======================================================
from pynytimes import NYTAPI
import os
import json
import datetime


# Connect to NYT API
def getAPI():
    key = os.getenv("NYT")
    nyt = NYTAPI(str(key), parse_dates=True)
    return nyt


# KeyWord Query Helper
# @param<keywords>  A list of keywords to search
# @return a list of JSON objects containing an abstract of the article and a URL for the article
def kqueryhelper(keywords):
    nyt = getAPI()
    ret = []
    for keyword in keywords:
        articles = nyt.article_search(
            query=keyword,
            results=10,
        )
        for article in articles:
            item = dict()
            item["Summary"] = article.get('snippet')
            item["URL"] = article.get('web_url')
            ret.append(item)

    return ret


# Person Query Helper
# @param<name>  A name to search
# @return a list of JSON objects containing a summary of the article and a URL for the article
def pqueryhelper(name):
    nyt = getAPI()
    ret = []
    articles = nyt.article_search(
        query=name,
        results=10,
    )
    for article in articles:
        item = dict()
        item["Summary"] = article.get('snippet')
        item["URL"] = article.get('web_url')
        ret.append(item)

    return ret

# Historical Query Helper
# @param<keywords>  A list of keywords to search
# @return a list of JSON objects containing an abstract of the article and a URL for the article
def histqueryhelper(year, month, keywords):
    nyt = getAPI()
    ret = []
    for keyword in keywords:
        start_date = datetime.datetime(year, month, 1)
        end_date = _last_day_of_month(start_date)
        articles = nyt.article_search(
            query=keyword,
            results=10,
            dates={
                "begin": start_date,
                "end": end_date,
            }
        )
        for article in articles:
            item = dict()
            item["Summary"] = article.get('snippet')
            item["URL"] = article.get('web_url')
            ret.append(item)

    return ret

# Referenced from https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month
# Gets the last day of a given month
def _last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)


