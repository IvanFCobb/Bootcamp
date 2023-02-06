from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        print(users)
        return users

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def edit_user(cls, data, num):
        query = "UPDATE users_schema.users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = now() WHERE (id = {});".format(
            num)
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_user(cls, num):
        query = "DELETE FROM `users_schema`.`users` WHERE (id = {});".format(
            num)
        return connectToMySQL('users_schema').query_db(query)

    @classmethod
    def get_one(cls, num):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id = {};" .format(
            num)
        results = connectToMySQL('users_schema').query_db(query)
        return cls(results[0])
