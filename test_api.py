from fastapi.testclient import TestClient
from api import app, add_book


client = TestClient(app)


def test_get_all_books():
    # CREATE 2 new books
    new_book_1 = {
        "id": 1,
        "title": "Flamengo",
        "author": "Zico",
        "release_year": 1981,
        "isbn": "FLA1981",
    }
    add_book(new_book_1)
    response = client.post("/add_book", json=new_book_1)
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


def test_get_book_by_id():
    response = client.get("/books/id/1")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 1


def test_get_book_by_author():
    response = client.get("/books/author/Zico")
    assert response.status_code == 200
    assert response.json()["data"]["author"] == "Zico"


def test_add_book():
    new_book = {
        "id": 30,
        "title": "Gremio",
        "author": "Renato",
        "release_year": 2000,
        "isbn": "GR123456789",
        "publisher": "CBF",
        "genre": "Futebol",
        "format": "Paperback",
        "description": "Cincum"
    }
    response = client.post("/add_book", json=new_book)
    assert response.status_code == 201
    assert response.json()["message"] == "Book added successfully!"


def test_delete_book_by_id():
    response = client.delete("/books/3")
    assert response.status_code == 200
    assert response.json()["message"] == "Book was successfully deleted!"


def test_update_book():
    updated_book = {
        "id": 2,
        "title": "Corinthians",
        "author": "Socrates",
        "release_year": 2010,
        "isbn": "-10001010",
        "publisher": "CBF",
        "genre": "Futebol",
        "format": "Paperback",
        "description": "Democracia corinthiana - atualizado"
    }
    response = client.put("/books/2", json=updated_book)
    assert response.status_code == 200
    assert response.json()["message"] == "Book with id 2 updated successfully"
