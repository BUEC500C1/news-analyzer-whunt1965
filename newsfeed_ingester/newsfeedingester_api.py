from flask import Flask, redirect, url_for, jsonify
from flask_restful import Resource, Api

if __name__ == '__main__':
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    import newsfeedingester as nfi
else:
    from newsfeed_ingester import newsfeedingester as nfi

app = Flask(__name__)
api = Api(app)


# Redirects to splash page for the newsfeed ingester API
@app.route('/')
def index():
    return redirect(url_for('NewsFeed_splash'))


# Renders a simple splash page for the newsfeed ingester API
@app.route('/newsfeed')
def NewsFeed_splash():
    return """<h1>Welcome to the Newsfeed Ingester</h1>"""


# Queries newsfeed sources based on provided keyword(s)
# @param<string:keywords> A text string (containing no '/' characters) including a list of keywords separated by '&'
# @return a JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each
#         entry in the list contains a JSON object with the following fields: "Title": < Article Title >,
#         "URL": < Article URL >, "Summary": < Short summary of the article >
@app.route('/newsfeed/keyquery/<string:keywords>')
def keywordquery(keywords):
    keywords = keywords.split('&')
    ret = dict()
    ret["Results"] = nfi.keyword_query(keywords)
    return jsonify(ret)


# Queries newsfeed sources based on provided name
# @param<string:name> A text string (containing no '/' characters) including a first and last name separated by a space
# @return a JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each
#         entry in the list contains a JSON object with the following fields: "Title": < Article Title >,
#         "URL": < Article URL >, "Summary": < Short summary of the article >
@app.route('/newsfeed/personquery/<string:name>')
def personquery(name):
    ret = dict()
    ret["Results"] = nfi.person_query(name)
    return jsonify(ret)


# Queries newsfeed sources for a given month, year, and list of keywords
# @param<string> A text string (containing no '/' characters) of the following format:
#                       year=<string:year>&month=<string:month>&keywords=<string:keywords where each keyword is
#                       separated by a & character>
# @return a JSON object containing a single key ("Results") with a value of a list of articles found by the query. Each
#         entry in the list contains a JSON object with the following fields: "Title": < Article Title >,
#         "URL": < Article URL >, "Summary": < Short summary of the article >
@app.route('/newsfeed/histquery/year=<string:year>&month=<string:month>&keywords=<string:keywords>')
def histquery(year, month, keywords):
    keywords = keywords.split('&')
    ret = dict()
    ret["Results"] = nfi.historical_query(year, month, keywords)
    return jsonify(ret)


if __name__ == '__main__':
    app.run()
