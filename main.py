from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikiLogic
from mylib.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Wikipedia API - Call /search, /wiki or /phrase"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retreive Wikipedia Page"""

    result = wikiLogic(name)
    return {"result": result}

@app.get("/phrase/{value}")
async def phrase(value: str):
    """Retreive Wikipedia Page and return phrases"""

    result = wikiphrases(value)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")