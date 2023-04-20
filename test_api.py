"""System modules"""
import random
import string
import uuid
from fastapi.testclient import TestClient
from api import app, cursor, conn, uuid4


client = TestClient(app)


def test_add_book():
    new_book = {
        "title": "Flamengo",
        "author": "Dinamite",
        "release_year": 2000,
        "isbn": "1234567800"
    }

    response = client.post('/books', json=new_book)
    assert response.status_code == 201

    # Assert if returned book is the same as the one sent
    assert response.json()["title"] == new_book["title"]
    assert response.json()["author"] == new_book["author"]
    assert response.json()["release_year"] == new_book["release_year"]
    assert response.json()["isbn"] == new_book["isbn"]

    uuid.UUID(response.json()["id"])

    # Assert if book was added to the database
    book = get_book_by_id_helper(response.json()["id"])
    assert book is not None

    tear_down()


def test_get_all_books():
    book_id_1 = add_book_helper()
    book_id_2 = add_book_helper()

    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json()["data"]) == 2

    # Check book_id_1 and book_id_2 are in the response
    for book in response.json()["data"]:
        assert book["id"] == book_id_1 or book["id"] == book_id_2

    tear_down()


def test_get_book_by_id():
    book_id = add_book_helper()

    response = client.get(f"/books/book/{book_id}")

    assert response.status_code == 200
    assert response.json()["data"]["id"] == book_id

    tear_down()


def test_get_book_by_author():
    book_id_1 = add_book_helper()
    book_id_2 = add_book_helper()
    default_author = "Zico"

    response = client.get("/books/author/"+default_author)
    assert response.status_code == 200

    for book in response.json()["data"]:
        assert book["author"] == default_author
        assert book["id"] == book_id_1 or book["id"] == book_id_2

    tear_down()


def test_delete_book_by_id():
    book_id = add_book_helper()

    response = client.delete(f"/books/{book_id}")

    assert response.status_code == 200

    # Check if book was deleted from the database
    book = get_book_by_id_helper(book_id)
    assert book is None


def test_update_book():
    book_id = add_book_helper()

    updated_book = {
        "title": "Corinthians",
        "author": "Socrates",
        "release_year": 2012,
    }

    response = client.put(f"/books/{book_id}", json=updated_book)

    assert response.status_code == 200

    # Check if book was updated in the database
    book = get_book_by_id_helper(book_id)
    assert book["title"] == updated_book["title"]
    assert book["author"] == updated_book["author"]
    assert book["release_year"] == updated_book["release_year"]

    tear_down()


def add_book_helper():
    sql = """INSERT INTO books (id, title, author, release_year, isbn,
         publisher, genre, format, description) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    book_id = str(uuid4())

    values = (book_id, 'Flamengo', 'Zico', 1983, get_random_string(), 'CBF',
              'Football', 'Hardcover', 'Em Dezembro de 81')

    cursor.execute(sql, values)
    conn.commit()

    return book_id


def get_book_by_id_helper(book_id):
    sql = """SELECT * FROM books WHERE id = %s;"""
    cursor.execute(sql, (book_id,))
    book = cursor.fetchone()
    return book


def tear_down():
    cursor.execute("""TRUNCATE TABLE books;""")
    conn.commit()


def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str
