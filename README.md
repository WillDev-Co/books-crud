# Books API

## Description
This project provides an API to retrieve and add books to a collection. The API has two endpoints: GET /books to retrieve the list of books, and POST /add_book to add a new book to the collection.

## Dependencies
This project has two dependencies that need to be installed using pip:

`fastapi`
`uvicorn`

To install the dependencies, you can also run the following command:
`pip install -r requirements.txt`

The requirements.txt file lists the dependencies and their versions, and can be used to install them all at once.

## Local deployment
To run the api on a local server, use the following command:

`uvicorn api:app --reload `


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

## Running tests
The project includes a test suite to ensure the API is working correctly. To run the tests, run the `test_api.py` file. This will run two tests:

test_get_books: Tests that the `/books` endpoint returns a list of books.
test_add_book: Tests that the `/add_book` endpoint adds a new book to the collection.

To run the tests, use the following command:

`python test_api.py`

Make sure that the API is running before running the tests.
