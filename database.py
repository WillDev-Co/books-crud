"""Database connection module."""

import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_conn():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='books-crud',
            user='user',
            password='password',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        return conn, cursor

    except psycopg2.Error as error:
        print('error connecting to the database: ', error)
        return None
