"""System modules"""
from fastapi.testclient import TestClient
from api import app


client = TestClient(app)


def test_add_book():
    """Adds a new book"""
    new_book = {
        "id": 1,
        "title": "Flamengo",
        "author": "Zico",
        "release_year": 1981,
        "isbn": "ABC123456789",
    }
    response = client.post("/add_book", json=new_book)
    assert response.status_code == 201
    assert response.json()["message"] == "Book added successfully!"


def test_get_all_books():
    """Retrieves all books"""
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


def test_get_book_by_id():
    """Retrieves a book by id"""
    response = client.get("/books/id/1")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 1


def test_get_book_by_author():
    """Retrieve books by author"""
    response = client.get("/books/author/Zico")
    assert response.status_code == 200
    assert response.json()["data"]["author"] == "Zico"


def test_update_book():
    """Update a book by id"""
    updated_book = {
        "id": 1,
        "title": "Corinthians",
        "author": "Socrates",
        "release_year": 2012,
        "isbn": "XYZ123456789",
    }

    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    assert response.json()["message"] == "Book with id 1 updated successfully"


def test_delete_book_by_id():
    """Deletes a book by id"""
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Book was successfully deleted!"
