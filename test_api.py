from fastapi.testclient import TestClient
from main import app, Book, books

client = TestClient(app)


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['title'] == 'Flamengo'


def test_add_book():
    new_book = Book(id=3,
                    title="Botafogo",
                    author="Nilton Santos",
                    release_year=2015,
                    ISBN="10-12345678")
    response = client.post("/add_book", json=new_book.dict())
    assert response.status_code == 201
    assert len(books) == 3
    assert books[-1].title == 'Botafogo'
