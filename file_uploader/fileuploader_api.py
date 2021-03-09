# Note: In creating this app, I used tutorial code from:
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
#
# I subsequently modified this stock code for the purposes of this application


if __name__ == '__main__':
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    import fileuploader as fu
else:
    from file_uploader import fileuploader as fu

import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import pathlib
import json

# Version to run as its own module
# import fileuploader as fu

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = './files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Ensure a file is an allowed file type (for now, just PDF)
# Source: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Redirects to splash page for the File Uploader API
@app.route('/')
def index():
    return redirect(url_for('FileUploader_splash'))


# Simple splash page for the File Uploader API
@app.route('/FileUploader')
def FileUploader_splash():
    return """<h1>Welcome to the File Uploader</h1>"""


# Upload a file to the DB through a form submission
# @return a JSON version of the uploaded file along with success parameters if successful. Otherwise, if file could not
#         be converted or added to the database, returns the original parameters and an error message. If no file or
#         or username is provided, returns to the file submission page
# Source: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
@app.route('/FileUploader/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        username = request.form['username']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if username == '':
            flash('No username entered')
            return redirect(request.url)
        if file and allowed_file(file.filename) and username:
            filename = secure_filename(file.filename)
            pathlib.Path(app.config['UPLOAD_FOLDER'], username).mkdir(parents=True, exist_ok=True)
            path = os.path.join(app.config['UPLOAD_FOLDER'], username, filename)
            file.save(path)
            ret = fu.create(username, path)
            # leave now for debug, but consider using next step to delete stored pdf files after parse so we don't
            # overload memory
            # path = pathlib.Path(path)
            # path.unlink()
            return jsonify(ret)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <label for=username>Username</label>
      <input type=text name=username>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# View all user files
# @param<username> The username of the user in the DB whose files we want to view
# return If the read is successful returns the file as a JSON object containing the files found along with a Success
#        code. Otherwise, returns the username and an error code
@app.route('/FileUploader/view/<string:username>', methods=['GET'])
def read_all_files(username):
    return jsonify(fu.read_many(username))


# View a single user file
# @param<username> The username of the user in the DB whose files we want to view
# @param<fileobj> A JSON object containing fields from which the file can be referenced (eg, Title or _id)
# @return If the read is successful returns the file as a JSON object containing the file found along with a Success
#         code. Otherwise, returns the original object, username, and an error code
@app.route('/FileUploader/view/<string:username>/file=<string:fileobj>', methods=['GET'])
def read_file(username, fileobj):
    return jsonify(fu.read_one(username, fileobj))


# Update a user file
# @param<username> The username of the user in the DB whose files we want to view
# @param<identifier> A JSON object containing fields from which the file can be referenced (eg, Title or _id)
# @param<fileobj> A JSON object containing the specific parameters to update
# @return If the update is successful returns updated file as a JSON object along with a Success code
#         Otherwise, otherwise returns the original parameters and an error code
@app.route('/FileUploader/update/<string:username>/identifier=<string:identifier>&fileobj=<string:fileobj>', methods=['GET'])
def update_file(username, identifier, fileobj):
    return jsonify(fu.update(username, identifier, fileobj))


# Delete a file in the DB
# @param<username> A string containing the username of the user associated with the files
# @param<identifier> A JSON object containing a unique identifier (eg file name or _id) associated with the file to
#                    delete.
# @return If the delete is successful, returns a success message and the number of files deleted.
#         Otherwise, returns the original object and an error code
@app.route('/FileUploader/delete/<string:username>/<string:identifier>', methods=['GET'])
def delete_file(username, identifier):
    return jsonify(fu.delete(username, identifier))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
