
import json
from flask import Flask, redirect, render_template, request, session, url_for,flash
from BooksStoreProject.database import mydatabase
from BooksStoreProject.customers import customers
from BooksStoreProject.loans import loans
from BooksStoreProject.books import books
from datetime import date, datetime


api = Flask(__name__)
api.secret_key = "222"
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='bookstore.sqlite')

dbms.create_db_tables()

api.register_blueprint(books)
api.register_blueprint(customers)
api.register_blueprint(loans)




@api.route('/books',methods=['GET','POST'])
def home():
    if request=='GET':
        return render_template("index.html")
    else:return render_template("index.html")







