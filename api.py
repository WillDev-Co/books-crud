from fastapi import FastAPI

app = FastAPI()


# /hello
@app.get("/hello")
def hello():
    return "Hello, Will"


# /books
class Books:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author, releaseYear, ISBN, publisher, genre, format, description):
        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "releaseYear": releaseYear,
            "ISBN": ISBN,
            "publisher": publisher,
            "genre": genre,
            "format": format,
            "description": description
        }
        self.books.append(book)

    def get_books(self):
        return self.books


books = Books()
books.add_book(1, "Vasco da Gama", "Eurico Miranda", 2010,
               "978-0743273534", "CBF", "Document", "Paperback", "Como ser vice")
books.add_book(2, "Flamengo", "Zico", 2019, "10-10101010",
               "CBF", "Document", "Hardcover", "Flamengo sempre eu hei de ser")


@app.get("/books")
def get_books():
    return books.get_books()
