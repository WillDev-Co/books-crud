CREATE TABLE IF NOT EXISTS books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    release_year INTEGER NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    publisher VARCHAR(255),
    genre VARCHAR(255),
    format VARCHAR(255),
    description TEXT
);
