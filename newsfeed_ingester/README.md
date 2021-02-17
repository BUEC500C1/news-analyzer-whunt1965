# newsfeed_ingester
The newsfeed_ingester module provides an API for extracting news articles based on keyword, person name, or time-based (from a specific month/year) queries

## User Stories
- **End User (journalists):**
    - As a journalist, I to be able to quickly find news stories related to a specific keyword or person. 
    - As a journalist, I want to have the option to perform a keyword search for articles published during a specific month/year to provide historical context or additional information for my story.

- **Developers**
    - As a developer, I want a simple API to add news feed content to my web application based on specific topics or people.
    - As a developer, I the ability to give my application the ability to suggest news articles to my users (including providing links) based on their recent searches, interests, or activities (eg, using "interests" listed in a social media post as keywords) 
    - As a developer, I the ability to give my application the ability to access an array of news content text related to specific topics to train a machine learning model
    - As a developer, I want access to log-level information on each method for debugging and system analysis purposes

## Build Instructions
This API can be utilized by simply cloning the repo (using git clone) and then using import newsfeed_ingester in whichever file needs to access the API.

## API Details
(Note: exact format of params to be fed into each method are TBD -- further API documentation to be provided with implementation)
- keyword_query(List keywords): Queries newsfeed sources based on provided keyword(s) 
    - @param<*keywords> a list of keyword(s) for the query 
    - @return A JSON object containing a list of articles, including article title, URL, and summary. If the query is not successful, returns an empty JSON
- person_query(String year, String month, list keywords): Queries newsfeed sources based on provided first/last name 
    - @param< fname > the first name of the person to query
    - @param< lname > the last name of the person to query
    - @return A JSON object containing a list of articles, including article title, URL, and summary. If the query is not successful, returns an empty JSON
- historical_query(String firstname, String lastname): Queries newsfeed sources from a given month/year based on provided keyword
    - @param< year > the year in which articles of interest would be published
    - @param< month > the month in which articles of interest would be published
    - @param< keywords > the list of keyword(s) to search
    - @return A JSON object containing the results of the query including article names, summary, and link to article (or an error message indicating the analysis failed)

## Internal Details
Below are a few internal details of the API stub implementation in response to requirements for this phase:
- **Status:** Currently, all methods either return the result of the operation or a failure message. Depending on implementation, it may also be worthwhile to explore adding some sort of "Processing" (or other status) message given that fetching results may take a while
- **Events:** The _newsfeedingester_events class defines a set of events related to the methods for this module. These events are logged (see logging below)
- **Logging:** A rudimentary logging system has been implemented to report each time a method is called and its result. The format of the log messages is as follows: < date/time > < type (eg, info or error) > < {Event: < specific event, eg PersonQuery_Success >, Target: < query search parameters (eg keywords) > }>
