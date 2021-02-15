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
(Note: exact format of params to be fed into each method are TBD -- further API documentation to be provided with implementation)
- post(File file): Allows a user to upload a file into the database
    - @param< File > A pdf file (likely parsed into JSON)
    - @return A message indicating the status (success or failure) of the upload
- get(File file, *attrs): Allows a user to read a file (or specific components) from the database
    - @param< File > A file name 
    - @param< *attrs > The specific components to read (default is to read entire file)
    - @return the file or specific component (as a JSON object) or a message indicating failure
- put(File file, *attrs): Allows a user to update a file (or specific components) in the database
    - @param< File > A file name
    - @param< *attrs > The specific components to update
    - @return a message indicating success or failure
- delete(File file, *attrs): Allows a user to delete a file (or specific components) in the database
    - @param< File > A file name
    - @param< *attrs > The specific components to delete (default is to read entire file)
    - @return a message indicating success or failure

## Internal Details
Below are a few internal details of the API stub implementation in response to requirements for this phase:
- **Status:** Currently, the create, update, and delete methods return a message indicating whether the request was successful or failed (in the future, this could be an HTTP status, eg 200 OK or 404 )
- **Events:** The _fileuploader_events class defines a set of events related to the methods for this module. These events are logged (see logging below)
- **Logging:** A rudimentary logging system has been implemented to report each time a method is called and its result. The format of the log messages is as follows: < date/time > < type (eg, info or error) > < {Event: < specific event, eg POST_Success >, Target: < specific file and components >}>
