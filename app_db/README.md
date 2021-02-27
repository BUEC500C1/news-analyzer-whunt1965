# Database
This Folder contains the functions used to manage interactions between the API's and the application's MongoDB database.

## Database Overview
For the database, I chose to use MongoDB due to the unstructured nature of the documents we will be processing. This database contains 2 collections: *Documents* and *Users*

### Documents
Our documents collection is used to store documents uploaded by users through the document ingester. Each document is stored as a JSON in the following format:
