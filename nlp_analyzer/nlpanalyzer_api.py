from flask import Flask
from flask_restful import Resource, Api
from nlp_analyzer import nlpanalyzer as nlp

app = Flask(__name__)
api = Api(app)

class NLPSplash(Resource):
    def get(self):
        return """<h1>Welcome to the NLP Analyzer</h1>"""

class AnalyzeSentiment(Resource):
    def get(self, text):
        return nlp.analyze_sentiment(text)

class AnalyzeEntity(Resource):
    def get(self, text):
        return nlp.analyze_entity(text)

class AnalyzeEntitySentiment(Resource):
    def get(self, text):
        return nlp.analyze_entity_sentiment(text)

class ClassifyContent(Resource):
    def get(self, text):
        return nlp.classify_content(text)


api.add_resource(NLPSplash, '/nlp', '/')
api.add_resource(AnalyzeSentiment, '/nlp/sentiment/<text>')
api.add_resource(AnalyzeEntity, '/nlp/entity/<text>')
api.add_resource(AnalyzeEntitySentiment, '/nlp/entitysentiment/<text>')
api.add_resource(ClassifyContent, '/nlp/classifycontent/<text>')

if __name__ == '__main__':
    app.run(debug=True)