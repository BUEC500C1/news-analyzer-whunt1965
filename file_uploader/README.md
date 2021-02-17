# file_uploader
The file uploader module provides an API to securely upload a file into the database, access the file (or its components), modify the file (or its components), and delete the file (or its components)

## User Stories
- **End User (journalists):**
    - As a journalist, I want a way to securely upload a file into a database and subsequently be able to access, modify, and delete specific components of the file

- **Developers**
    - As a developer, I want a simple API to upload, access, modify, and delete files in a database
    - As a developer, I want access to log-level information on each method for debugging and system analysis purposes

## Build Instructions
This API can be utilized by simply cloning the repo (using git clone) and then using import file_uploader in whichever file needs to access the API.

## API Details
All functions require a JSON input of the following format (Note: a subset of these fields may only need specification as outlined in the function documentation  below):
<pre>
   {
       "ID":/File/< File_ID >/< User_ID >, 
       "Upload_Date":< YYYY-MM-DD >, 
       "File_Metadata":{
           "Authors":[< author1 >,...], 
           "File_Creation_Date":< YYYY-MM-DD >, 
           "File_Source":< file_source >, "File_Tags":[< Tag1 >,...]
        }, 
       "Text":{
           "Text_ID": /File/< File_ID >/< User_ID >/< Text_ID >,
           "Text":[< Paragraph1 >, ...],
           "Sentiment":[< Paragraph1_Sentiment >, ...],
           "Entity":[< Paragraph1_Entity >, ...],
           "Entity_Sentiment":[< Paragraph1_Entity_Sentiment >, ...],
        },
   }
</pre>
- create(JSON fileObject): Uploads a file and creates an entry in the Database
    - @param< JSON fileObject > A JSON file object containing all fields specified in the above format
    - @return The JSON object along with a reponse code indeicating success or failure
- read(JSON fileObject): Allows a user to read a file (or specific components) from the database
    - @param< Fileobject > A JSON object containing the file ID and (optionally) the specific parameters to read
    - @return If the read is successful returns the file (or specified subcomponents of a file) as a JSON object along with a Success code. Otherwise, returns the original object and an error code
- update(JSON fileObject): Allows a user to update a file (or specific components) in the database
    - @param< fileObject > A JSON object containing the file ID and the specific parameters to update
    - @return If the update is successful returns updated file as a JSON object along with a Success code. Otherwise, returns the original object and an error code
- delete(JSON fileObject): Allows a user to delete a file (or specific components) in the database
    - @param< fileObject > If the delete is successful, returns the updated file (an empty object if the entire file is deleted) and a message code indicating success. Otherwise, returns the original object and an error code
    - @return a message indicating success or failure

## Internal Details
Below are a few internal details of the API stub implementation in response to requirements for this phase:
- **Status:** Currently, the create, update, and delete methods return teh updated file (as well as a message indicating a success or failure)
- **Events:** The _fileuploader_events class defines a set of events related to the methods for this module. These events are logged (see logging below)
- **Logging:** A rudimentary logging system has been implemented to report each time a method is called and its result. The format of the log messages is as follows: < date/time > < type (eg, info or error) > < {Event: < specific event, eg POST_Success >, Target: < specific file and components >}>
