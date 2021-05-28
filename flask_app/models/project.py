from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app import app       
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Project:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.balance = data['balance']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO projects (name,balance,user_id) VALUES (%(name)s,%(balance)s,%(user_id)s);"
        user_id = connectToMySQL('budget_db').query_db(query,data)
        return user_id

    @classmethod
    def get_all_projects(cls):
        query = "SELECT * FROM projects;"
        results = connectToMySQL('budget_db').query_db(query)
        projects = []
        for project in results:
            projects.append(cls(project))
        return projects
    
    @classmethod
    def get_by_id(cls,id):
        query = "SELECT * FROM projects WHERE id = %(id)s;"
        data ={
            "id":id
        }
        result = connectToMySQL('budget_db').query_db(query,data)
        return result

    @classmethod
    def join_tables(cls,id):
        query = "SELECT transactions.name as trans_name, transactions.amount as trans_amount, projects.name as proj_name, projects.balance as proj_balance FROM projects LEFT JOIN transactions ON projects.id = transactions.project_id WHERE projects.user_id = %(id)s;"
        data = {
            "id": id
        }
        results = connectToMySQL('budget_db').query_db(query,data)
        return results


    @classmethod
    def delete_project(cls,data):
        query = "DELETE FROM projects WHERE id = %(id)s;"
        return connectToMySQL('budget_db').query_db(query,data)