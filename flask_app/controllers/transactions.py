from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_app.models.transaction import Transaction
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/view/<id>')
def view_project(id):
    data = {
        'id':id
    }
    return render_template('transactions.html',transactions = Transaction.get_by_id(id))

@app.route('/add/transaction')
def view_transaction():
    context = {
        'logged_in_user': User.get_one(session['uuid'])
    }
    return render_template ("add.html", projects = Project.get_all_projects(), **context)

@app.route('/add', methods = ["POST"])
def add_transaction():
    data = {
        "name": request.form["name"],
        "catagory": request.form["catagory"],
        "amount": request.form["amount"],
        "project_id": request.form["project_id"]
    }
    project =  request.form["project_id"]
    Transaction.add_transaction(data)
    return redirect ("/view/" + str(project))

@app.route('/delete/<id>')
def delete_message(id):
    data = {
        'id': id,
    }
    Transaction.delete_transaction(data)
    return redirect('/dashboard')