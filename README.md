# EC500 - Project 2 
This repository contains an application designed to help journalists store and analyze documents (as well as query additional information from other news feeds) in order to inform stories they produce. Descriptions of key components (and API documentation) are linked below.

## AWS Testing
(Note -- see Web API's below for more details)

IP for Running EC2 Instance: 18.217.67.70

Notes on testing:
- I would recommend using Google Chrome as Safari does not seem to like the EC2 IPs
- If there are issues with the file uploader not accessing the DB, please let me know. I'm using Mongo Atlas (cloud MongoDB) for file storage and have whitelisted the current IP of the EC2 instance. If this IP changes while running, though, I will need to updated the allowed IP's in my system
- For the file uploader, please use the username *test_fileuploader* for uploading and accessing files. This is a name that's already in the system which is allowed to create, access, and modify files (since we did not get to a login module, only this default name is enabled). Additionally, no files are currently in teh DB. You will need to upload a file if you want to view results!
- Sample Queries for each of the API's
  - *File Uploader* - 18.217.67.70:80
    - Upload - 18.217.67.70:80/FileUploader/upload - just fill in the form on the webpage using test_fileuploader as the user
    - READ
      - READ ALL FILES BELONGING TO A USER: (note, there is currently nothing for this user in the DB. Please first upload a file) - 18.217.67.70:80/FileUploader/view/test_fileuploader
      - READ A SINGLE FILE BELONGING TO A USER: (assuming you have created a file called test.pdf) - 18.217.67.70:80/FileUploader/view/test_fileuploader/file={"Name":"test.pdf"}
      - UPDATE (update the name of your file): 18.217.67.70:80/FileUploader/update/test_fileuploader/identifier={"Name":"test.pdf"}&fileobj={"Name":"test4.pdf"}
      - DELETE: 18.217.67.70:80/FileUploader/delete/test_fileuploader/identifier={"Name":"test4.pdf"}

  - *NewsFeed Ingester* - 18.217.67.70:8081 (Note: if this page hangs, may be the NYT API -- it went down on me today when making these links)
    - Keyword Query: 18.217.67.70:8081/newsfeed/keyquery/'Oil&OPEC'
    - Person Query: 18.217.67.70:8081/newsfeed/personquery/'John Doe'
    - Historical Query: 18.217.67.70:8081/newsfeed/histquery/year=1998&month=6&keywords=Stocks&Bonds
  - *NLP Analysis - 18.217.67.70:8080*
    - Sentiment Analysis: 18.217.67.70:8080/nlp/sentiment/"some test text here"
    - Entity Analysis: 18.217.67.70:8080/nlp/entity/"some test text here about Lebron James"
    - Entity-Sentiment Analysis: 18.217.67.70:8080/nlp/entitysentiment/"some test text here about Lebron James. I do like Lebron James"
    - Content Classification (note: query text must be atleast 20 words) 18.217.67.70:8080/nlp/classifycontent/"I hate Notre Dame football. But I love the Alabama Crimson Tide and I feel very strongly about the Georgia Bulldogs. That is all I want to say"


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
            - Example: < EC2 Public IP >:80/FileUploader/view/test_fileuploader
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
        - @return A JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each entry in the list contains a JSON object with the following fields: "Summary": < Short summary of the article >, "URL": < Article URL >
        - Example: *< EC2 Public IP >:8081/newsfeed/keyquery/'kw1&kw2'*
    - **Person Query** (URI: *< EC2 Public IP >:8081/newsfeed/personquery/< firstname&lastname >*): Queries newsfeed sources based on provided first/last name
        - @param< string:name > A text string (containing no '/' characters) including a first and last name separated by a space
        - @return A JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each entry in the list contains a JSON object with the following fields: "Summary": < Short summary of the article >, "URL": < Article URL >
        - Example: *< EC2 Public IP >:8081/newsfeed/personquery/'John Doe'*
    - **Historical Query** (URI: *< EC2 Public IP >:8081/newsfeed/histquery/year=< string:year >&month=< string:month >&keywords=< string:keywords >*). Queries newsfeed sources for a given month, year, and list of keywords
        - @param<string> A text string (containing no '/' characters) of the following format: year=< string:year >&month=< string:month >&keywords=< string:keywords where each keyword is separated by a & character >
        - @return A JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each entry in the list contains a JSON object with the following fields: "Summary": < Short summary of the article >, "URL": < Article URL >
      - Example: *< EC2 Public IP >:8081/newsfeed/histquery/year=1998&month=6&keywords=arg1&arg2*
- **nlp_analyzer:** 
  - The nlp_analyzer is available on port 8080 of the EC2 instance via the following URI *<EC2 Public IP>:8081/nlp*. Specific functions of the API can be accessed at the following URIs via GET methods:
    - **Sentiment analysis** (URI: *< EC2 Public IP >:8080/nlp/sentiment/< string:text >*): Performs a sentiment analysis on a given text string
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Score") with a value of the associated sentiment score of the text
    - **Entity Analysis** (URI: *< EC2 Public IP >:8080/nlp/entity/< string:text >*): Performs entity analysis on a given text string
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Entities") with a value of a list of entities extracted from the text
    - **Entity Sentiment Analysis** (URI: *< EC2 Public IP >:8080/nlp/entitysentiment/< string:text >*): Performs both entity and sentiment analysis on a given text string
        - @param< string:text > A text string (containing no '/' characters)
        - @return a JSON object containing a single key ("Results") with a value of a list of key-value pair entries. Within the list, each entry contains two key-value pairs: {"Entity":< entity name >,"Score":< sentiment score associated with the entity >}
    - **Content Classification** (URI: *< EC2 Public IP >:8080/nlp/classifycontent/< string:text >*): Performs content classification on a given string text
        - @param< string:text > A text string (containing no '/' characters and a minimum of 20 words)
        - @return a JSON object containing a single key ("Results") with a list of key-value pair entries. Within the list, each entry contains two key-value pairs: {"Category":< category name >,"Score":< confidence score associated with the category >}
