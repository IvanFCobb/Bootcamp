from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books_who_favorited = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = connectToMySQL('books_schema').query_db(query)
        for row in results:
            authors.append(cls(row))
        print("get all")
        return authors

    @classmethod
    def get_authors_favorite_books(cls, num):
        query = "SELECT * FROM authors WHERE (books_id = {});".format(num)
        "SELECT * FROM authors LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        print("get authors in books")
        return authors

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def unfavorited_authors(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id from favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_schema').query_db(query, data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls, data):
        print("add favorite")
        query = "INSERT INTO favorites (author_id, book_id) VALUES ( %(author_id)s, %(book_id)s);"
        print("test")
        return connectToMySQL('books_schema').query_db(query, data), "hello"

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books On books.id = favorites.book_id WHERE authors.id = %(id)s"
        results = connectToMySQL('books_schema').query_db(query, data)

        authors = cls(results[0])

        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            authors.books_who_favorited.append(book.Book(data))

        return authors
