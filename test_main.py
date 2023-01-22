from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Wikipedia API - Call /search, /wiki or /phrase"}

def test_read_search():
    response = client.get("/search/barack")
    assert response.status_code == 200
    assert "Barack Obama" in response.json()["result"]

def test_read_wiki():
    response = client.get("/wiki/Barack Obama")
    assert response.status_code == 200
    assert "44th president" in response.json()["result"] 

def test_read_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert "44th president" in response.json()["result"] 