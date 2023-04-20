# Books API

## Description
This project provides an API to retrieve, add, update, and delete books in a collection. The API has the following endpoints:

* GET /books: Retrieves the list of books.
* POST /add_book: Adds a new book to the collection.
* GET /books/id/{book_id}: Retrieves a book by its ID.
* GET /books/author/{author}: Retrieves a book by its author.
* DELETE /books/{book_id}: Deletes a book by its ID.
* PUT /books/{book_id}: Updates a parameter of a book.


## Dependencies
This project has three dependencies that need to be installed using pip:

`fastapi`
`uvicorn`
`pytest`
`pylint`
`psycopg2`

To install the dependencies, you can also run the following command:
`pip install -r requirements.txt`

The requirements.txt file lists the dependencies and their versions, and can be used to install them all at once.

## Local deployment
To run the api on a local server, use the following command:

`uvicorn api:app --reload`


## How to access the endpoint GET /books and retrieve the list of books
To retrieve the list of books, send a GET request to the /books endpoint. The API will return a JSON response with the list of books in the collection.

## How to access the endpoint POST /add_book to add a new book
To add a new book to the collection, send a POST request to the /add_book endpoint with a JSON payload containing the parameters for the new book.

The parameters that can be included are:

* title (required)
* author (required)
* releaseYear (required)
* ISBN (required)
* publisher (optional)
* genre (optional)
* format (optional)
* description (optional)


## How to access the endpoint GET /books/id/{book_id} to retrieve a book by its ID
To retrieve a book by its ID, send a GET request to the /books/id/{book_id} endpoint. The {book_id} parameter in the endpoint URL should be replaced with the ID of the book you want to retrieve.


## How to access the endpoint GET /books/author/{author} to retrieve a book by its author
To retrieve a book by its author, send a GET request to the /books/author/{author} endpoint. The {author} parameter in the endpoint URL should be replaced with the name of the author you want to retrieve.


## How to access the endpoint DELETE /books/{book_id} to delete a book by its ID
To delete a book by its ID, send a DELETE request to the /books/{book_id} endpoint. The {book_id} parameter in the endpoint URL should be replaced with the ID of the book you want to delete.


## How to access the endpoint PUT /books/{book_id} to update a parameter of a book
To update a parameter of a book, send a PUT request to the /books/{book_id} endpoint with a JSON payload containing the updated parameters for the book.

The parameters that can be included are:

* title 
* author 
* releaseYear 
* ISBN 
* publisher 
* genre 
* format 
* description 

The {book_id} parameter in the endpoint URL should be replaced with the ID of the book you want to update.


## Running tests
The project includes a test suite to ensure the API is working correctly. To run the tests, run the `test_api.py` file. This will run the following tests:

`test_add_book`: Tests that the `/add_book` endpoint adds a new book to the collection.
`test_get_all_books`: Tests that the `/books` endpoint returns a list of books.
`test_get_book_by_id`: Tests that the `/books/book_id/{book_id}` endpoint retrieves a book by its ID.
`test_get_book_by_author`: Tests that the `/books/author/{author}` endpoint retrieves books by author.
`test_update_book`: Tests that the `/books/{book_id}` endpoint updates an existing book in the collection.
`test_delete_book_by_id`: Tests that the `/books/{book_id}` endpoint deletes a book by its ID.

To run the tests, follow these steps:

1. Make sure the API is not running.
2. Open a terminal and navigate to the project directory.
3. Run the following command:

`pytest test_api.py`

The `pytest` command will run all the tests in the `test_api.py` file. The output will indicate whether each test passed or failed, along with any error messages that were raised.

[![CI](https://github.com/WillDev-co/books-crud/actions/workflows/ci.yml/badge.svg)](https://github.com/WillDev-co/books-crud/actions/workflows/ci.yml)

