# ======================================================
# NLP Analyzer API - Private API Helper Functions
# ======================================================
import os

# Imports the Google Cloud client library
from google.cloud import language_v1


# Authorizes API and returns service client
def getClient():
    client = language_v1.LanguageServiceClient()
    return client


# Performs sentiment analysis on a given text string
# @param<text> The text string to analyze
# @return A "scaled" sentiment score (sentiment * magnitude)
def analyzeSent(text):
    client = getClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    sent_score = sentiment.score * sentiment.magnitude
    return sent_score


# Performs entity analysis on a given text string
# @param<text> The text string to analyze
# @return A list of entities extracted from the text
def analyzeEnt(text):
    client = getClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(request={'document': document})
    entities = []
    for entity in response.entities:
        entities.append(entity.name)
    return entities

# Performs entity and sentiment analysis on a given text string
# @param<text> The text string to analyze
# @return A list of dictionaries, with each item containing an "Entity" and "Score" key
def analyzeEntSent(text):
    client = getClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entity_sentiment(request={'document': document})
    entities = []
    for entity in response.entities:
        item = dict()
        item["Entity"] = entity.name
        item["Score"] = entity.sentiment.score * entity.sentiment.magnitude
        entities.append(item)
    return entities

# Performs entity and sentiment analysis on a given text string
# @param<text> The text string to analyze
# @return A list of dictionaries, with each item containing an "Entity" and "Score" key
def classCont(text):
    client = getClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.classify_text(request={'document': document})
    entities = []
    for category in response.categories:
        item = dict()
        item["Category"] = category.name
        item["Score"] = category.confidence
        entities.append(item)
    return entities

