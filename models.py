""" Model Definitions """

from typing import Optional
from pydantic import BaseModel, validator

# pylint: disable=useless-option-value


class Book():
    def __init__(
        self,
        id,
        title,
        author,
        release_year,
        isbn,
        publisher,
        genre,
        format,
        description
    ):
        self.id = id
        self.title = title
        self.author = author
        self.release_year = release_year
        self.isbn = isbn
        self.publisher = publisher
        self.genre = genre
        self.format = format
        self.description = description

# pylint: disable=E0213


class CreateBookRequest(BaseModel):
    title: str
    author: str
    release_year: int
    isbn: str
    publisher: Optional[str] = None
    genre: Optional[str] = None
    format: Optional[str] = None
    description: Optional[str] = None

    @validator('title')
    def title_length(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError('Title must be between 1 and 100 characters')
        return value

    @validator('author')
    def author_length(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError('Author must be between 1 and 100 characters')
        return value

    @validator('release_year')
    def year_range(cls, value):
        if value < 0 or value > 3000:
            raise ValueError('Release year must be between 0 and 3000')
        return value

    @validator('isbn')
    def validate_isbn(cls, value):
        if not value.isdigit():
            raise ValueError('ISBN must be a string of digits')
        if len(value) != 10 and len(value) != 13:
            raise ValueError('ISBN must be 10 or 13 digits')
        return value


class UpdateBookRequest(BaseModel):
    title: str
    author: str
    release_year: int
    publisher: Optional[str] = None
    genre: Optional[str] = None
    format: Optional[str] = None
    description: Optional[str] = None

    @validator('title')
    def title_length(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError('Title must be between 1 and 100 characters')
        return value

    @validator('author')
    def author_length(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError('Author must be between 1 and 100 characters')
        return value

    @validator('release_year')
    def year_range(cls, value):
        if value < 0 or value > 3000:
            raise ValueError('Release year must be between 0 and 3000')
        return value
