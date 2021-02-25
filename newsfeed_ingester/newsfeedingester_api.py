import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from flask import Flask
from flask_restful import Resource, Api
from newsfeed_ingester import newsfeedingester as nfi

app = Flask(__name__)
api = Api(app)

class NewsFeedSplash(Resource):
    def get(self):
        return """<h1>Welcome to the Newsfeed Ingester</h1>"""

class KeywordQuery(Resource):
    def get(self, keywords):
        return nfi.keyword_query(list(keywords))

class PersonQuery(Resource):
    def get(self, name):
        return nfi.person_query(name)

class HistoricalQuery(Resource):
    def get(self, year, month, keywords):
        return nfi.historical_query(year, month, list(keywords))


api.add_resource(NewsFeedSplash, '/newsfeed', '/')
api.add_resource(KeywordQuery, '/newsfeed/keyquery/<keywords>')
api.add_resource(PersonQuery, '/newsfeed/personquery/<name>')
api.add_resource(HistoricalQuery, '/newsfeed/histquery/year=<year>&month=<month>&keywords=<keywords>')

if __name__ == '__main__':
    app.run(debug=True)