"""System modules."""
from uuid import uuid4
from fastapi import FastAPI, HTTPException, status
import database
import models


app = FastAPI()
conn, cursor = database.get_db_conn()


@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(payload: models.CreateBookRequest):
    book = models.Book(
        str(uuid4()),
        payload.title,
        payload.author,
        payload.release_year,
        payload.isbn,
        payload.publisher,
        payload.genre,
        payload.format,
        payload.description
    )

    try:
        cursor.execute(
            """ INSERT INTO books (id, title, author, \
                release_year, isbn, publisher, genre, format, description) VALUES \
                (%s, %s, %s, %s, %s, %s, %s, %s, %s) \
                RETURNING * """, (
                book.id,
                book.title,
                book.author,
                book.release_year,
                book.isbn,
                book.publisher,
                book.genre,
                book.format,
                book.description
            )
        )
        conn.commit()

    except Exception as e:
        conn.rollback()

        # Check if error is because of duplicate isbn
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"isbn: {book.isbn} already exists"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error: {e}"
            )

    # Return book inside data
    return book


@app.get("/books")
def get_books():
    try:
        cursor.execute(""" SELECT * FROM books """)
        books = cursor.fetchall()

    except Exception as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

    return {
        "data": books
    }


@ app.get("/books/book/{id}")
def get_book_by_id(id: str):
    try:
        cursor.execute(
            """ SELECT * from books WHERE id = %s """, (id,))
        book = cursor.fetchone()

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"book with id: {id} was not found"
            )

    except Exception as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

    return {"data": book}


# GET book by author
@ app.get("/books/author/{author}")
def get_book_by_author(author: str):
    try:
        cursor.execute(
            """ SELECT * from books WHERE author = %s """, (author,))
        books = cursor.fetchall()

    except Exception as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

    return {"data": books}


@ app.delete("/books/{id}")
def del_book_by_id(id: str):
    try:
        cursor.execute(""" DELETE FROM books WHERE id = %s """, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"book with id: {id} was not found"
            )
    except Exception as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

    return {"message": f"Book with id: {id} was successfully deleted!"}


@ app.put("/books/{id}")
def update_book(id: str, payload: models.UpdateBookRequest):
    try:
        cursor.execute(
            """ UPDATE books SET \
            title = %s, \
            author = %s, \
            release_year = %s, \
            publisher = %s, \
            genre = %s, \
            format = %s, \
            description = %s \
                WHERE id = %s RETURNING * """,
            (
                payload.title,
                payload.author,
                payload.release_year,
                payload.publisher,
                payload.genre,
                payload.format,
                payload.description,
                id,
            )
        )

        updated_book = cursor.fetchone()
        conn.commit()

        if updated_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with id: {id} not found"
            )

    except Exception as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
