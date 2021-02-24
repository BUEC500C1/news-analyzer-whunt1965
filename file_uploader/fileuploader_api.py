from flask import Flask
from flask_restful import Resource, Api
import fileuploader as fu

app = Flask(__name__)
api = Api(app)

class FileUploaderSplash(Resource):
    def get(self):
        return """<h1>Welcome to the File Uploader</h1>"""

class FileUploader(Resource):
    def post(self, docId):
        return fu.create(docId)

    def get(self, docId):
        return fu.read(docId)

    def put(self, docId):
        return fu.update(docId)

    def delete(self, docId):
        return fu.delete(docId)

api.add_resource(FileUploaderSplash, '/FileUploader', '/')
api.add_resource(FileUploader, '/FileUploader/<docId>')

if __name__ == '__main__':
    app.run(debug=True)
