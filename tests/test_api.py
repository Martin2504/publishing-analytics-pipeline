from fastapi.testclient import TestClient
from api.main import app

"""
API integration tests

Tests FastAPI endpoints using TestClient to ensure correct responses,
status codes, and error handling.
"""

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Publishing Analytics API is running"

def test_get_books_endpoint():
    response = client.get("/books")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_missing_book_returns_404():
    response = client.get("/books/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"