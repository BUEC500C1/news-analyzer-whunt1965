# file_uploader
The file uploader module provides an API to securely upload a file into the database, access the file (or its components), modify the file (or its components), and delete the file (or its components)

## User Stories
- **End User (journalists):**
    - As a journalist, I want a way to securely upload a file into a database and subsequently be able to access, modify, and delete specific components of the file
    - As a journalist, I an easy means to extract text and other data from a file which I previously uploaded.

- **Developers**
    - As a developer, I want a simple API to upload, access, modify, and delete files in a database
    - As a developer, I want access to log-level information on each method for debugging and system analysis purposes

## Build Instructions
This API can be utilized by simply cloning the repo (using git clone) and then using import file_uploader in whichever file needs to access the API. Note: This module is linked to a database and will also require the database module to function. Please also clone [app_db](https://github.com/BUEC500C1/news-analyzer-whunt1965/tree/main/app_db), register a MONGO db acocunt, create teh appropriate User and Documents collections, and add MONGOKEY (your access key) as an environmental variable.

## API Details
The create method will turn a PDF into the following JSON structure. These fields can (other than UID, which must be provided separately) can be used during subsequent accesses
<pre>
   {
       "Name": < the file name extracted from the path >,
       "path": < The file path as uploaded in the database >,
       "UID":< User ID associated with file > 
       "Upload_Date":< YYYY-MM-DD >, 
       "File_Metadata":{
           "Title":< Title extracted from PDF file >, 
           "Author":< Author extracted from PDF file >, 
           "Creator":< Creator extracted from PDF file >
        }, 
       "Text":{
           "Text":[< Paragraph1 >, ...],
           "Sentiment":[< Paragraph1_Sentiment >, ...],
           "Entity":[< Paragraph1_Entity >, ...],
           "Entity_Sentiment":[< Paragraph1_Entity_Sentiment >, ...],
           "Content_Classification":[< Paragraph1_Content_Class >, ...],
        },
   }
</pre>
- create(path, username): Uploads a file, parses it into JSON, and creates an entry in the Database
    - @param< username > The username of the user creating an entry
    - @param< path > A path to a file to be uploaded into the database
    - @return If successful, returns the JSON version of the file and a success response code. Otherwise, returns the original parameters and an error code

- read_one(fileobj, username): Accessor for a single file in the DB
    - @param< username > A string containing the username of the user associated with the files
    - @param< fileobj > A (stringified) JSON object containing fields from which the file can be referenced (eg, Title or _id)
    - @return If the read is successful returns the file as a JSON object containing the file found along with a Success code. Otherwise, returns the original object, username, and an error code

- read_many(username): Accessor for all files in the DB belonging to a single user
    - @param< username > A string containing the username of the user associated with the files
    - @return If the read is successful returns the file as a JSON object containing the files found along with a Success code. Otherwise, returns the username and an error code

- update(username, identifier, update): Modifies a file in the DB
    - @param< username > A string containing the username of the user associated with the file to update
    - @param< identifier > A JSON object containing fields from which the file can be referenced (eg, Title or _id)
    - @param< update > A JSON string object containing the specific parameters to update (eg, { "TEXT" \[ "TEXT" ] : { "some new text"})
    - @return If the update is successful returns updated file as a JSON object along with a Success code. Otherwise, otherwise returns the original parameters and an error code

- delete(username, myFileObj): Delete a file in the DB
    - @param< username > A string containing the username of the user associated with the file
    - @param< fileObj > A JSON object containing a unique identifier (eg file name or _id) associated with the file to delete.
    - @return If the delete is successful, returns a success message and the number of files deleted. Otherwise, returns the original object and an error code

## Internal Details
Below are a few internal details of the API stub implementation in response to requirements for this phase:
- **Status:** Currently, the create, update, and delete methods return teh updated file (as well as a message indicating a success or failure)
- **Events:** The _fileuploader_events class defines a set of events related to the methods for this module. These events are logged (see logging below)
- **Logging:** A rudimentary logging system has been implemented to report each time a method is called and its result. The format of the log messages is as follows: < date/time > < type (eg, info or error) > < {Event: < specific event, eg POST_Success >, Target: < specific file and components >}>
