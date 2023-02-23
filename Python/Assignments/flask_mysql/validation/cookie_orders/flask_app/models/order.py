from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        orders = []
        results = connectToMySQL('cookie_orders').query_db(query)
        for row in results:
            orders.append(cls(row))
        print("get all")
        return orders

    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders ( customer_name, cookie_type, num_of_boxes, created_at, updated_at ) VALUES ( %(customer_name)s, %(cookie_type)s, %(num_of_boxes)s, NOW() , NOW() );"
        return connectToMySQL('cookie_orders').query_db(query, data)

    @classmethod
    def get_one(cls, num):
        query = "SELECT id, customer_name, cookie_type, num_of_boxes, created_at, updated_at FROM orders WHERE id = {};" .format(
            num)
        results = connectToMySQL('cookie_orders').query_db(query)
        return cls(results[0])

    @classmethod
    def update_order(cls, data, num):
        print("updating order...")
        query = "UPDATE cookie_orders.orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, num_of_boxes = %(num_of_boxes)s, updated_at = now() WHERE (id = {});".format(
            num)
        return connectToMySQL('cookie_orders').query_db(query, data)

    @classmethod
    def delete_order(cls, num):
        query = "DELETE FROM cookie_orders.orders WHERE (id = {});".format(
            num)
        return connectToMySQL('cookie_orders').query_db(query)

    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['customer_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash("Cookie Type must be at least 2 characters.")
            is_valid = False
        if int(order['num_of_boxes']) < 1:
            flash("Please enter a valid number of boxes.")
            is_valid = False
        return is_valid
