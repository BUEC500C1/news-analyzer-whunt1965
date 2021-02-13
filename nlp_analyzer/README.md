# nlp_analyzer
The nlp analyzer module provides an API to perform sentiment, enity, and syntax analysis (as well as content classification) on a text. 

## User Stories
- **End User (journalists):**
    - As a journalist, I want to quickly extract key entities (names, places, etc.) from a given text. 
    - As a journalist, I want to be able to get an analysis of the overall sentiment (positive or negative) as well as the magnitude of this sentiment on a given piece of text and/or the entities mentioned in this text.
    - As a journalist, I want to be able to perform content classification (eg, understand what categories are mentioned) in a given text.

- **Developers**
    - As a developer, I want a simple API to perform sentiment and entity analysis on a text either as a deliverable to an end-user or as part of my application for understanding user input.
    - As a developer, I want to be able to use syntax analysis to break down user input in order to determine what actions to perform in my application. 
    - As a developer, I want access to log-level information on each method for debugging and system analysis purposes

## API Details
(Note: exact format of params to be fed into each method are TBD -- further API documentation to be provided with implementation)
- analyze_sentiment(String text): Performs sentiment analysis on a given text
    - @param< text > A text string on which to perform sentiment analysis
    - @return A sentiment score on the provided text (or an error message indicating the analysis failed)
- analyze_entity(String text): Performs sentiment analysis on a given text
    - @param< text > A text string on which to perform entity analysis
    - @return A list of entities extracted from the text (or an error message indicating the analysis failed)
- analyze_syntax(String text): Performs syntax analysis on a given text
    - @param< text > A text string on which to perform syntax analysis
    - @return The results of the syntactic analysis (parts of speech, etc) (or an error message indicating the analysis failed)
- analyze_entity_sentiment(String text): Performs sentiment analysis on entities extracted from a given text
    - @param< text > The text on which to perform entity-sentiment analysis
    - @return The entities (and associated sentiments) extracted from the text (or an error message indicating the analysis failed)
- classify_content(String text): Performs content classification on a given text
    - @param< text > The text on which to perform content classification 
    - @return A list of content categories that are found in the provided text

## Internal Details
Below are a few internal details of the API stub implementation in response to requirements for this phase:
- **Status:** Currently, all methods either return the result of the operation or a failure message. Depending on implementation, it may also be worthwhile to explore adding some sort of "Processing" (or other status) message given that the analysis may take a while
- **Events:** The _nlpanalyzer_events class defines a set of events related to the methods for this module. These events are logged (see logging below)
- **Logging:** A rudimentary logging system has been implemented to report each time a method is called and its result. The format of the log messages is as follows: < date/time > < type (eg, info or error) > < {Event: < specific event, eg ClassifyContext_Success >, Target: < the first 10 characters of the text being analyzed >}>