"""System modules."""
from typing import Optional
from psycopg2.extras import RealDictCursor
import psycopg2
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

# pylint: disable = too-few-public-methods


app = FastAPI()


class Book(BaseModel):
    """
    Book model, with the fields id, title, author, release_year, isbn, publisher,
    genre, format, and description.
    """
    book_id: int
    title: str
    author: str
    release_year: int
    isbn: str
    publisher: Optional[str] = None
    genre: Optional[str] = None
    format: Optional[str] = None
    description: Optional[str] = None


try:
    conn = psycopg2.connect(host='localhost', database='books-crud',
                            user='user', password='password', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('Database connection was succesfull!')
except psycopg2.Error as error:
    print('Connecting to database failed')
    print('Error:', error)


@app.get("/books")
def get_books():
    """Retrieves all books"""
    cursor.execute(""" SELECT * FROM books """)
    books = cursor.fetchall()

    return {"data": books}


@app.post("/add_book", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    """Adds a book"""
    cursor.execute(
        """ INSERT INTO books (book_id, title, author, release_year, isbn) VALUES \
            (%(book_id)s, %(title)s, %(author)s, %(release_year)s, %(isbn)s) \
            RETURNING * """, book.dict(),)
    cursor.fetchone()
    conn.commit()

    return {"message": "Book added successfully!"}


@ app.get("/books/book_id/{book_id}")
def get_book_by_id(book_id: int):
    """Retrieve a book by book_id"""
    cursor.execute(""" SELECT * from books WHERE book_id = %s """, (book_id,))
    book_by_id = cursor.fetchone()
    if not book_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with book_id: {book_id} was not found")

    return {"data": book_by_id}


# GET book by author
@ app.get("/books/author/{author}")
def get_book_by_author(author: str):
    """Retrieve books by author"""
    cursor.execute(""" SELECT * from books WHERE author = %s """, (author,))
    book_by_author = cursor.fetchone()
    if not book_by_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with author: {author} was not found")

    return {"data": book_by_author}


@ app.delete("/books/{book_id}")
def del_book_by_id(book_id: int):
    """Delets a book by book_id"""
    cursor.execute(""" DELETE FROM books WHERE book_id = %s """, (book_id,))
    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with book_id: {book_id} was not found")

    return {"message": "Book was successfully deleted!"}


@ app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    """Updates a book by book_id"""
    cursor.execute(""" UPDATE books SET \
        book_id = %s,\
        title = %s, \
        author = %s, \
        release_year = %s, \
        isbn = %s, \
        publisher = %s, \
        genre = %s, \
        format = %s, \
        description = %s \
            WHERE book_id = %s RETURNING * """,
                   (book.book_id, book.title, book.author, book.release_year, book.isbn,
                    book.publisher, book.genre, book.format, book.description, book_id,))

    updated_book = cursor.fetchone()
    conn.commit()

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"book with book_id: {book_id} not found")

    return {"message": f"Book with book_id {book_id} updated successfully"}
