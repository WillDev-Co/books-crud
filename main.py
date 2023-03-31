from fastapi import FastAPI
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


@ app.get("/books", response_model=List[Book])
async def get_books():
    return books


@ app.post("/add_book", status_code=201)
async def add_book(book: Book):
    books.append(book)
