"""
Main module of the book API.
"""
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()


class Book(BaseModel):
    """
    Book model, with the fields id, title, author, release_year, isbn, publisher,
    genre, format, and description.
    """
    id: int
    title: str
    author: str
    release_year: int
    isbn: str
    publisher: Optional[str] = None
    genre: Optional[str] = None
    format: Optional[str] = None
    description: Optional[str] = None


"""
Connecting to PostgreSQL database
"""
try:
    conn = psycopg2.connect(host='localhost', database='books-crud',
                            user='postgres', password='Password1234', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('Database connection was succesfull!')
except Exception as error:
    print('Connecting to database failed')
    print('Error:', error)


# GET all books
@app.get("/books")
def get_books():
    # Retrieve all books.
    cursor.execute(""" SELECT * FROM books """)
    books = cursor.fetchall()

    return {"data": books}


# ADD a book
@app.post("/add_book", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    cursor.execute(
        """ INSERT INTO books (id, title, author, release_year, isbn) VALUES (%(id)s, %(title)s, %(author)s, %(release_year)s, %(isbn)s) RETURNING * """, book.dict())
    cursor.fetchone()
    conn.commit()

    return {"message": "Book added successfully!"}


# GET book by id
@ app.get("/books/id/{id}")
def get_book_by_id(id: int):
    # Retrieve a book by ID.
    cursor.execute(""" SELECT * from books WHERE id = %s """, (id,))
    book_by_id = cursor.fetchone()
    if not book_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with id: {id} was not found")

    return {"data": book_by_id}


# GET book by author
@ app.get("/books/author/{author}")
def get_book_by_author(author: str):
    cursor.execute(""" SELECT * from books WHERE author = %s """, (author,))
    book_by_author = cursor.fetchone()
    if not book_by_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with author: {author} was not found")

    return {"data": book_by_author}


# DELETE a book by id
@ app.delete("/books/{id}")
def del_book_by_id(id: int):
    cursor.execute(""" DELETE FROM books WHERE id = %s """, (id,))
    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with id: {id} was not found")

    return {"message": "Book was successfully deleted!"}


# UPDATE a book by id
@ app.put("/books/{id}")
def update_book(id: int, book: Book):
    cursor.execute(""" UPDATE books SET id = %s, title = %s, author = %s, release_year = %s, isbn = %s, publisher = %s, genre = %s, format = %s, description = %s WHERE id = %s RETURNING * """,
                   (book.id, book.title, book.author, book.release_year, book.isbn, book.publisher, book.genre, book.format, book.description, id,))

    updated_book = cursor.fetchone()
    conn.commit()

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"book with id: {id} not found")

    return {"message": f"Book with id {id} updated successfully"}
