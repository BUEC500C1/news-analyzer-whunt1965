# EC500 - Project 2 Test
This repository contains an application designed to help journalists store and analyze documents (as well as query additional information from other news feeds) in order to inform stories they produce. Descriptions of key components (and API documentation) are linked below.
## Links to Component and API Documentation:
- **file_uploader:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/file_uploader/README.md)
- **newsfeed_ingester:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/newsfeed_ingester/README.md)
- **nlp_analyzer:** [link](https://github.com/BUEC500C1/news-analyzer-whunt1965/blob/main/nlp_analyzer/README.md)

## Web API's
Currently, the file_uplaoder, newsfeed_ingester, and nlp_analyzer stubs are available as REST API's hosted on an AWS EC2 instance. Details for each API are included below:

- **file_uploader:**
  - The file_uploader is available on port 80 of the EC2 instance and can be accessed via the following URI: */FileUploader/<docobject>* with the doc object parameters as defined below based on the request type:
    - POST: the doc object is a JSON object containing a path to a file {"PATH":<path>}to be uploaded/parsed (a JSON representation of the parsed file is returned).
    - GET: the doc object a JSON of the following for {"doc_id":<id>) containing the document id to fetch. The document is returned as a JSON object
    - PUT: the doc object is a JSON containing the document id and and any relevant fields of the document to update. The JSON of the updated document is returned.
    - DELETE: the doc object is a JSON of the following for {"doc_id":<id>) containing the document id to fetch. A success message is returned if the document is successfully deleted.
- **newsfeed_ingester:** 
- **nlp_analyzer:** 
