from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/create/new")
def display_create():
    return render_template ("create.html")

@app.route("/create/project", methods = {'POST'})
def create_project():
    data = {
        "name": request.form["name"],
        "balance": request.form["balance"],
        "user_id": request.form["user_id"]
    }
    Project.create(data)
    return redirect ("/dashboard")

@app.route('/delete/project/<id>')
def delete_project(id):
    data = {
        'id': id,
    }
    Project.delete_project(data)
    return redirect('/dashboard')