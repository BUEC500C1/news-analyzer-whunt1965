# EC500 - Project 2 
This repository contains an application designed to help journalists store and analyze documents (as well as query additional information from other news feeds) in order to inform stories they produce. Descriptions of key components (and API documentation) are linked below.
## Links to Component and API Documentation:
- **file_uploader:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/file_uploader/README.md)
- **newsfeed_ingester:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/newsfeed_ingester/README.md)
- **nlp_analyzer:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/nlp_analyzer/README.md)

## Web API's
Currently, the file_uplaoder, newsfeed_ingester, and nlp_analyzer stubs are available as REST API's hosted on an AWS EC2 instance. Details for each API are included below:

- **file_uploader:**
  - The file_uploader is available on port 80 of the EC2 instance and can be accessed via the following URI: *< EC2 Public IP >/FileUploader/< docobject >* with the doc object parameters as defined below based on the request type:
    - **POST**: the doc object is a JSON object containing a path to a file {"PATH":< path >}to be uploaded/parsed (a JSON representation of the parsed file is returned).
    - **GET**: the doc object a JSON of the following for {"doc_id":< id >) containing the document id to fetch. The document is returned as a JSON object
    - **PUT**: the doc object is a JSON containing the document id and and any relevant fields of the document to update. The JSON of the updated document is returned.
    - **DELETE**: the doc object is a JSON of the following for {"doc_id":< id >) containing the document id to fetch. A success message is returned if the document is successfully deleted.
- **newsfeed_ingester:**
  - The newsfeed_ingester is available on port 8081 of the EC2 instance via the following URI *<EC2 Public IP>:8081/newsfeed*. Specific functions of the API can be accessed at the following URIs via GET methods:
    - **Keyword Query** (URI: *< EC2 Public IP >:8081/newsfeed/< string:keywords >*). Queries newsfeed sources based on provided keyword(s)
        - @param< string:keywords > A text string (containing no '/' characters) including a list of keywords separated by '&'
        - @return A JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each entry in the list contains a JSON object with the following fields: "Title": < Article Title >, "URL": < Article URL >, "Summary": < Short summary of the article >
        - Example: *< EC2 Public IP >:8081/newsfeed/keyquery/'kw1&kw2'*
    - **Person Query** (URI: *< EC2 Public IP >:8081/newsfeed/personquery/< firstname&lastname >*): Queries newsfeed sources based on provided first/last name
        - @param< string:name > A text string (containing no '/' characters) including a first and last name separated by a space
        - @return A JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each entry in the list contains a JSON object with the following fields: "Title": < Article Title >, "URL": < Article URL >, "Summary": < Short summary of the article >
        - Example: *< EC2 Public IP >:8081/newsfeed/personquery/'John Doe'*
    - **Historical Query** (URI: *< EC2 Public IP >:8081/newsfeed/histquery/year=< string:year >&month=< string:month >&keywords=< string:keywords >*). Queries newsfeed sources for a given month, year, and list of keywords
        - @param<string> A text string (containing no '/' characters) of the following format: year=< string:year >&month=< string:month >&keywords=< string:keywords where each keyword is separated by a & character >
      - Example: *< EC2 Public IP >:8081/newsfeed/histquery/year='1998'&month='June'&keywords='arg1&arg2'*
- **nlp_analyzer:** 
  - The nlp_analyzer is available on port 8080 of the EC2 instance via the following URI *<EC2 Public IP>:8081/nlp*. Specific functions of the API can be accessed at the following URIs via GET methods:
    - **Sentiment analysis** (URI: *< EC2 Public IP >:8081/nlp/sentiment/< string:text >*): Performs a sentiment analysis on a given text string
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Score") with a value of the associated sentiment score of the text
    - **Entity Analysis** (URI: *< EC2 Public IP >:8081/nlp/entity/< string:text >*): Performs entity analysis on a given text string
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Entities") with a value of a list of entities extracted from the text
    - **Entity Sentiment Analysis** (URI: *< EC2 Public IP >:8081/nlp/entitysentiment/< string:text >*): Performs both entity and sentiment analysis on a given text string
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Results") with a value of a list of key-value pair entries. Within the list, each entry contains two key-value pairs: {"Entity":< entity name >,"Score":< sentiment score associated with the entity >}
    - **Content Classification** (URI: *< EC2 Public IP >:8081/nlp/classifycontent/< string:text >*): Performs content classification on a given string text
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Results") with a list of key-value pair entries. Within the list, each entry contains two key-value pairs: {"Content":< entity name >,"Score":< confidence score associated with the content >}
