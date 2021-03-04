# Database
This Folder contains the functions used to manage interactions between the API's and the application's MongoDB database.

## Database Overview
For the database, I chose to use MongoDB due to the unstructured nature of the documents we will be processing. This database contains 2 collections: *Documents* and *Users*

### Documents
Our documents collection is used to store documents uploaded by users through the document ingester. Each document is stored as a JSON in the following format:
<pre>
   {
       "_id": < id assigned by MongoDB >,
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
        "Deleted" : < "True" or "False" indicating whether the document has been marked as deleted > 
   }
</pre>

#### Document Accessor Public Methods
- **addDocument(document_input)**: ***Add a document to the DB***
   - @param<document> A JSON document object to store in the database. Note: To prevent duplicates, the document's "Name" and "UID" fields must not match an existing (non-deleted) document in the database (ie, it must not have both the same UID and Name as another document already stored and not marked as deleted)
   - @return 1 if the document is successfully added and None otherwise

- **getDocument(docobj)**: ***Retrieve a single document from the DB***
   - @param<docobj> A JSON object containing the UID and another valid identifier (id or Name) associated with the document
   - @return The document (as a JSON) if one is found and None otherwise

- **getDocuments(uid)**: ***Retrieve multiple documents belonging to a single user from the DB***
   - @param<UID> A string containing the username of a user who's documents we wish to access
   - @return The documents (as a JSON) if atleast one is found and None otherwise

- **updateDocument(idObj, update)**: ***Update a document in DB***
   - param<idObj> A JSON object containing the UID and another valid identifier (id or Name) associated with the document
   - @param<update> A JSON object containing the update to apply to the document
   - @return The updated document (as a JSON) if one is updates and none otherwise

- **updateDocument(idObj, update)**: ***Mark a document in the DB as deleted***
   - @param<idObj>  A JSON object containing the UID and another valid identifier (id or Name) associated with the document
   - @return The number of documents updated 

- **deleteAllUserDocs(username)**: ***Mark all documents associated with a username as deleted***
   - @param<UID> A string containing the username of a user who's documents we wish to mark as deleted
   - @return  The number of documents marked with a deleted flag


#### Documents Collection Snaphot
A snapshot of the current Documents collection is included here (containing a few sample documents uploaded during testing):

![snapshot](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/readme_pics/docs.png)

### Users
Our users collection is used to store account information for users of ur system. Each user is stored as a JSON in the following format:
<pre>
{
   "_id":<ID assigned by MongoDB>,
   "username" < a username for the user -- must be unique>,
   "email":<email -- must be unique>,
   "password"<hashed password">,
   "Deleted" : < "True" or "False" indicating whether the user has been marked as deleted > 
}
</pre>
      
#### Users Accessor Public Methods

- **addUser(newuser)**: ***Add a user to the DB***
   - @param<newUser>   A user object containing a unique username and email (cannot match those of another non-deleted user) as well as a hashed password
   - @return 1 if the insert is successful and None otherwise

- **getUser(username)**: ***Retrieve User info from username***
   - @param<username>   A username (string) to be queried in the DB
   - @return The entry for this user in the DB (as a JSON) or None if no user is found

- **getUserName(email)**: ***Retrieve a username from an email***
   - @param<email>   An email (string) to be queried in the DB
   - @return The username for this user in the DB (as a JSON) or None if no user is found

- **getHashedPass(username)**: ***Retrieve a hashed password for a user (to be used by login)***
   - @param<username> A username (string) to be queried in the DB
   - @return The hashed password for this user or None if no user is found

- **updateUserEmail(username, update)**: ***Update a user's email in the DB***
   - @param<username>  A username (string) to be queried in the DB
   - @param<update>    The new value for a user's email
   - @return 1 if successful and 0 otherwise

- **updateUserPass(username, update)**: ***Update a user's password in the DB***
   - @param<username>  A username (string) to be queried in the DB
   - @param<update>    The new value for a user's hashed password
   - @return 1 if successful and 0 otherwise

- **deleteUser(username)**: ***Mark a user as deleted in the DB and mark all associated documents as deleted***
   - @param<username>  A username (string) to be queried in the DB
   - @return A tuple containing the number of users deleted and the number of documents deleted


#### Users Collection Snaphot
A snapshot of our current Users collection is included here (containing a pair of sample users uploaded during testing):
![snapshot](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/readme_pics/users.png)

