# EC500 - Project 2 
This repository contains an application designed to help journalists store and analyze documents (as well as query additional information from other news feeds) in order to inform stories they produce. Descriptions of key components (and API documentation) are linked below.
## Links to Component and API Documentation:
- **file_uploader:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/file_uploader/README.md)
- **newsfeed_ingester:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/newsfeed_ingester/README.md)
- **nlp_analyzer:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/nlp_analyzer/README.md)

## Web API's
Currently, the file_uplaoder, newsfeed_ingester, and nlp_analyzer stubs are available as REST API's hosted on an AWS EC2 instance. Details for each API are included below:

- **file_uploader:**
  - The file_uploader is available on port 80 of the EC2 instance and can be accessed via the following URI: *< EC2 Public IP >/FileUploader/* with the following URI schemes:
    - **UPLOAD (POST)** (URI: *< EC2 Public IP >:80/FileUploader/upload*)
        - This page provides a form for uploading a file. A user provide a username already registered in the DB and select a file to upload
    - **READ (GET)**:
        - **READ ALL FILES BELONGING TO A USER:** (URI: *< EC2 Public IP >:80/FileUploader/view/< string:username >*)
            - @param< username > The username of the user in the DB whose files we want to view
            - @return If the read is successful returns the file as a JSON object containing the files found along with a Success code. Otherwise, returns the username and an error code
        - **READ A SINGLE FILE BELONGING TO A USER:** (URI: *< EC2 Public IP >:80/FileUploader/view/< string:username >/file=< string:fileobj >*)
            - @param< username > The username of the user in the DB whose files we want to view
            - @param<fileobj> A JSON object containing fields from which the file can be referenced (eg, Title or _id)
            - @return If the read is successful returns the file as a JSON object containing the file found along with a Success code. Otherwise, returns the original object, username, and an error code
            - Example: < EC2 Public IP >:80/FileUploader/view/test_fileuploader/file={"Name":"test.pdf"}
    - **UPDATE** (URI: *< EC2 Public IP >:80/FileUploader/update/< string:username >/identifier=< string:identifier >&fileobj=< string:fileobj >*)
        - @param< username > The username of the user in the DB whose files we want to view
        - @param< identifier > A JSON object containing fields from which the file can be referenced (eg, Title or _id)
        - @param< fileobj > A JSON object containing the specific parameters to update
        - @return If the update is successful returns updated file as a JSON object along with a Success code. Otherwise, otherwise returns the original parameters and an error code
        - Example: < EC2 Public IP >:80/FileUploader/update/test_fileuploader/identifier={"Name":"test.pdf"}&fileobj={"Name":"test4.pdf"}
    - **DELETE**: (URI: *< EC2 Public IP >:80/FileUploader/delete/< string:username >/< string:identifier >*)
        - @param< username > A string containing the username of the user associated with the files
        - @param< identifier > A JSON object containing a unique identifier (eg file name or _id) associated with the file to delete
        - @return If the delete is successful, returns a success message and the number of files deleted. Otherwise, returns the original object and an error code
        - Example: < EC2 Public IP >:80/FileUploader/delete/test_fileuploader/identifier={"Name":"test4.pdf"}
- **newsfeed_ingester:**
  - The newsfeed_ingester is available on port 8081 of the EC2 instance via the following URI *<EC2 Public IP>:8081/newsfeed*. Specific functions of the API can be accessed at the following URIs via GET methods:
    - **Keyword Query** (URI: *< EC2 Public IP >:8081/newsfeed/keyquery/< string:keywords >*). Queries newsfeed sources based on provided keyword(s)
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
