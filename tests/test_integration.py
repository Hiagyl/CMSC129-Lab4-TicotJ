# tests/test_integration.py
import pytest


def test_add_book_success(client):
    """
    Test that a valid POST request creates a book and returns 201.
    This should fail because the route /books does not exist yet.
    """
    payload = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
    response = client.post('/books', json=payload)

    assert response.status_code == 201
    assert response.get_json()['message'] == "Book added successfully"


def test_add_book_validation_failure(client):
    """
    Test that an invalid POST request (missing author) returns 400.
    This should fail because the route does not exist.
    """
    payload = {"title": "Invalid Book"}  # Missing author
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert "error" in response.get_json()
