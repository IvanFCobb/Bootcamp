from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        print("get all")
        return ninjas

    @classmethod
    def get_ninjas_in_dojo(cls, num):
        query = "SELECT * FROM ninjas WHERE (dojos_id = {});".format(num)
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        print("get ninjas in dojos")
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojos_id, created_at, updated_at ) VALUES ( %(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def edit_ninja(cls, data, num):
        print("updating ninja...")
        query = "UPDATE dojos_and_ninjas_schema.ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, dojos_id = %(dojo_id)s, updated_at = now() WHERE (id = {});".format(
            num)
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete_ninja(cls, num):
        query = "DELETE FROM dojos_and_ninjas_schema.ninjas WHERE (id = {});".format(
            num)
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)

    @classmethod
    def get_one(cls, num):
        query = "SELECT id, first_name, last_name, age, dojos_id, created_at, updated_at FROM ninjas WHERE id = {};" .format(
            num)
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        return cls(results[0])
