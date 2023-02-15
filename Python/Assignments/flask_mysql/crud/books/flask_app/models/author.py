from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        print("get all")
        return authors

    @classmethod
    def get_authors_in_book(cls, num):
        query = "SELECT * FROM authors WHERE (books_id = {});".format(num)
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        print("get authors in books")
        return authors

    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors ( first_name, last_name, age, books_id, created_at, updated_at ) VALUES ( %(fname)s, %(lname)s, %(age)s, %(book_id)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def edit_author(cls, data, num):
        print("updating author...")
        query = "UPDATE books_schema.authors SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, books_id = %(book_id)s, updated_at = now() WHERE (id = {});".format(
            num)
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def delete_author(cls, num):
        query = "DELETE FROM books_schema.authors WHERE (id = {});".format(
            num)
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def get_one(cls, num):
        query = "SELECT id, first_name, last_name, age, books_id, created_at, updated_at FROM authors WHERE id = {};" .format(
            num)
        results = connectToMySQL('books_schema').query_db(query)
        return cls(results[0])
