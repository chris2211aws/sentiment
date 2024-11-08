import pytest
from fastapi.testclient import TestClient
from sentiment import app  # Replace 'your_filename' with the name of your FastAPI file

client = TestClient(app)

def test_analyze_sentiment_positive():
    response = client.post("/sentiment/", json={"text": "I love programming!"})
    assert response.status_code == 200
    assert response.json()["score"] >= 6  # Expect a positive score

def test_analyze_sentiment_negative():
    response = client.post("/sentiment/", json={"text": "I hate bugs!"})
    assert response.status_code == 200
    assert response.json()["score"] <= 4  # Expect a negative score

def test_analyze_sentiment_neutral():
    response = client.post("/sentiment/", json={"text": "It's okay."})
    assert response.status_code == 200
    assert response.json()["score"] == 5  # Expect a neutral score
