"""
Main module of the book API.
"""
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    """
    Book model, with the fields id, title, author, release_year, ISBN, publisher,
    genre, format, and description.
    """
    id: int
    title: str
    author: str
    release_year: int
    ISBN: str
    publisher: Optional[str] = None
    genre: Optional[str] = None
    format: Optional[str] = None
    description: Optional[str] = None


# Add book objects
books = [
    Book(id=1,
         title='Flamengo',
         author='Zico',
         release_year=2019,
         ISBN="100100100",
         publisher="CBF",
         genre="Futebol",
         format="Hardcover",
         description="Em dezembro de 81"),
    Book(id=2,
         title='Corinthians',
         author='Socrates',
         release_year=2000,
         ISBN="-10001010",
         publisher="CBF",
         genre="Futebol",
         format="Paperback",
         description="Democracia corinthiana")
]


@app.get("/books", response_model=List[Book])
async def get_books():
    # Retrieve all books.
    return books


@app.post("/add_book", status_code=status.HTTP_201_CREATED)
async def add_book(book: Book):
    # Add a new book to the collection.
    books.append(book)
    return {"message": "Book added successfully!"}


@app.get("/books/id/{book_id}")
async def get_book_by_id(book_id: int):
    # Retrieve a book by ID.
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="id not found")


@app.get("/books/author/{author}")
async def get_book_by_author(author: str):
    # Retrieve a book by author name.
    for book in books:
        if book.author == author:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="author not found")


@app.delete("/books/{book_id}")
async def del_book_by_id(book_id: int):
    # Delete a book by ID.
    for book in books[:]:
        if book.id == book_id:
            books.remove(book)
            return {"message": f"Book id {book_id} deleted successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="id not found")


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    # Update a book by ID.
    for idx, book_obj in enumerate(books):
        if book_obj.id == book_id:
            books[idx] = book
            return {"message": f"Book with id {book_id} updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="id not found")
