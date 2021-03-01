if __name__ == '__main__':
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    import fileuploader as fu
else:
    from file_uploader import fileuploader as fu

from flask import Flask
from flask_restful import Resource, Api
import json

# Version to run as its own module
# import fileuploader as fu


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

# =================================
# Ignore - copied in on bad branch merge - developing as a new feature in a branch
# =================================

# @app.route('/')
# def home():
#     return """<h1>Welcome to the File Uploader</h1>"""
#
# # POST method
# @app.route('/upload/<path:filepath>', methods=['POST'])
# def upload(filepath):
#     return fu.create(filepath)
#
# #GET method
# @app.route('/read/id=<path:fileid>', methods=['GET'])
# def get(fileid):
#     return fu.read(fileid)
#
# #DELETE method
# @app.route('/delete/id=<path:fileid>', methods=['DELETE'])
# def delete(fileid):
#     return fu.delete(fileid)
#
# #PUT method
# @app.route('/update/mod=<string:fileobj>', methods=['PUT'])
# def put(fileobj):
#     return fu.update(fileobj)