from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


# Book is a subclass of BaseModel, and it provides automatic validation of the input data
class Book(BaseModel):
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


# GET all books
@app.get("/books", response_model=List[Book])
async def get_books():
    return books


# POST (Create) a book
@app.post("/add_book", status_code=status.HTTP_201_CREATED)
async def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully!"}


# GET a book by id
@app.get("/books/id/{id}")
async def get_book_by_id(id: int):
    for book in books:
        if book.id == id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="id not found")


# GET a book by author
@app.get("/books/author/{author}")
async def get_book_by_author(author: str):
    for book in books:
        if book.author == author:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="author not found")


# DELETE a book by id
@app.delete("/books/{id}")
async def del_book_by_id(id: int):
    for book in books:
        if book.id == id:
            books.remove(book)
            return {"message": f"Book id {id} deleted successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="id not found")


# UPDATE a parameter of a book
@app.put("/books/{id}")
async def update_book(id: int, book: Book):
    for i, b in enumerate(books):
        if b.id == id:
            books[i] = book
            return {"message": f"Book with id {id} updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="id not found")
