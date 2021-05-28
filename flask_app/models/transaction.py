from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app import app       
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Transaction:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.amount = data['amount']
        self.project_id = data['project_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls,id):
        query = "SELECT * FROM transactions WHERE project_id = %(id)s;"
        data ={
            "id":id
        }
        result = connectToMySQL('budget_db').query_db(query,data)
        return result

    @classmethod
    def add_transaction(cls,data):
        query = "INSERT INTO transactions (name,catagory,amount,project_id) VALUES (%(name)s,%(catagory)s,%(amount)s,%(project_id)s);"
        user_id = connectToMySQL('budget_db').query_db(query,data)
        return user_id

    @classmethod
    def subtract(cls,data):
        return

    @classmethod
    def delete_transaction(cls,data):
        query = "DELETE FROM transactions WHERE id = %(id)s;"
        return connectToMySQL('budget_db').query_db(query,data)
