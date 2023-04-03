from fastapi.testclient import TestClient
from api import app


client = TestClient(app)


def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_book_by_id():
    response = client.get("/books/id/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Flamengo"


def test_get_book_by_author():
    response = client.get("/books/author/Zico")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_add_book():
    new_book = {
        "id": 3,
        "title": "São Paulo",
        "author": "Raí",
        "release_year": 2005,
        "ISBN": "201202002",
        "publisher": "CBF",
        "genre": "Futebol",
        "format": "Paperback",
        "description": "Campeão do mundo em 2005"
    }
    response = client.post("/add_book", json=new_book)
    assert response.status_code == 201
    assert response.json()["message"] == "Book added successfully!"


def test_delete_book_by_id():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Book id 1 deleted successfully."


def test_update_book():
    updated_book = {
        "id": 2,
        "title": "Corinthians",
        "author": "Socrates",
        "release_year": 2010,
        "ISBN": "-10001010",
        "publisher": "CBF",
        "genre": "Futebol",
        "format": "Paperback",
        "description": "Democracia corinthiana - atualizado"
    }
    response = client.put("/books/2", json=updated_book)
    assert response.status_code == 200
    assert response.json()["message"] == "Book with id 2 updated successfully"
