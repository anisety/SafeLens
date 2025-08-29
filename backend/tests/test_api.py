import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the SafeLens API"}

def test_moderate_safe_text():
    response = client.post("/moderate", json={"text": "This is a perfectly safe and friendly sentence."})
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "score" in data
    # This model is for sentiment, so we check for POSITIVE/NEGATIVE
    assert data["label"] == "POSITIVE"

def test_moderate_unsafe_text():
    response = client.post("/moderate", json={"text": "I hate this, it's awful and terrible."})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] == "NEGATIVE"

def test_moderate_empty_text():
    response = client.post("/moderate", json={"text": ""})
    # The underlying pipeline might handle this differently, but FastAPI should catch it
    # if the model can't handle empty strings. Let's assume it returns a valid response.
    assert response.status_code == 200
