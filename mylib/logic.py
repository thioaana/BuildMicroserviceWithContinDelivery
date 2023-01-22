import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """this is wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    result = wikipedia.search(name)
    return result


def phrase(name):
    """Return phrases from Wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
