# Database
This Folder contains the functions used to manage interactions between the API's and the application's MongoDB database.

## Database Overview
For the database, I chose to use MongoDB due to the unstructured nature of the documents we will be processing. This database contains 2 collections: *Documents* and *Users*

### Documents
Our documents collection is used to store documents uploaded by users through the document ingester. Each document is stored as a JSON in the following format:
<pre>
   {
       "_id":/File/< File_ID >/>,
       "UID":< User ID > 
       "Upload_Date":< YYYY-MM-DD >, 
       "File_Metadata":{
           "Authors":[< author1 >,...], 
           "File_Creation_Date":< YYYY-MM-DD >, 
           "File_Source":< file_source >, "File_Tags":[< Tag1 >,...]
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

A snapshot of the current Documents collection is included here (containing a pair of sample documents uploaded during testing.
