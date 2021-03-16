from flask import Flask, redirect, url_for, jsonify
from flask_restful import Resource, Api
import json

if __name__ == '__main__':
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    import nlpanalyzer as nlp
else:
    from nlp_analyzer import nlpanalyzer as nlp

app = Flask(__name__)
api = Api(app)


# Redirects to splash page for the NLP analyzer API
@app.route('/')
def index():
    return redirect(url_for('NLP_splash'))


# Renders a simple splash page for the NLP analyzer API
@app.route('/nlp')
def NLP_splash():
    return """<h1>Welcome to the NLP Analyzer</h1>"""


# Performs a sentiment analysis on a given text string
# @param<string:text> A text string (containing no '/' characters)
# @return a JSON object containing a single key ("Score") with a value of the associated sentiment score of the text
@app.route('/nlp/sentiment/<string:text>')
def analyze_sentiment(text):
    ret = dict()
    ret["Score"] = nlp.analyze_sentiment(text)
    return jsonify(ret)


# Performs entity analysis on a given text string
# @param<string:text> A text string (containing no '/' characters)
# @return a JSON object containing a single key ("Entities") with a value of a list of entities extracted from the text
@app.route('/nlp/entity/<string:text>')
def analyze_entity(text):
    ret = dict()
    ret["Entities"] = nlp.analyze_entity(text)
    return jsonify(ret)


# Performs both entity and sentiment analysis on a given text string
# @param<string:text> A text string (containing no '/' characters)
# @return a JSON object containing a single key ("Results") with a value of a list of key-value pair entries. Within
#         the list, each entry contains two key-value pairs: {"Entity":<entity name>,"Score":<sentiment score
#         associated with the entity>}
@app.route('/nlp/entitysentiment/<string:text>')
def analyze_entity_sentiment(text):
    ret = dict()
    ret["Results"] = nlp.analyze_entity_sentiment(text)
    return ret


# Performs content classification on a given string text
# @param<string:text> A text string (containing no '/' characters and a minimum of 20 words)
# @return a JSON object containing a single key ("Results") with a list of key-value pair entries. Within
#         the list, each entry contains two key-value pairs: {"Category":<category name>,"Score":<confidence score
#         associated with the category>}
@app.route('/nlp/classifycontent/<string:text>')
def classify_content(text):
    ret = dict()
    ret["Results"] = nlp.classify_content(text)
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
