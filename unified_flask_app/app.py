# app.py
import os, sys
#
# # Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# import file_uploader

import file_uploader
from file_uploader import fileuploader_api as fu_api
# from file_uploader import fileuploader_api as fu_api

# import nlp_analyzer
import nlp_analyzer
from nlp_analyzer import nlpanalyzer_api as nlp_api

# merge
application = DispatcherMiddleware(
    fu_api.FileUploaderSplash.get(), {
        '/nlp': nlp_api.NLPSplash
    })

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5000,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True)
