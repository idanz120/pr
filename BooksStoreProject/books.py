from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from BooksStoreProject.customers import customers
from BooksStoreProject.database import mydatabase
from datetime import date

books = Blueprint('books',__name__, url_prefix='/books')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='bookstore.sqlite')
books.register_blueprint(customers)

#BOOKS SECTION


@books.route('/display',methods=['GET'])
def books_display():
    res = dbms.get_all_data(table= mydatabase.BOOKS)
    return render_template('booksDisplay.html',book=res)
    


@books.route('/add_form', methods=['GET'])
def get_book_form():
    return render_template("add_book.html",)



#FIND BOOK BY NAME ROUTE
@books.route('/get_book_form', methods=["POST",'GET'])
def book_by_name():
    if request.method == "POST":
        data = request.form['search']
        res = dbms.get_data_by('*',mydatabase.BOOKS,'name',data)
        print(res)
        if res ==[]:flash('Not Found')
        return render_template('get_book_by_name.html',res=res)
    
    return render_template('get_book_by_name.html')
 


@books.route('/add', methods=['POST'])
def add_book():
    name = request.form.get('name')
    author = request.form.get('author')
    year = request.form.get('yearPublished')
    return_type = request.form.get('type')
    dbms.insert_book(name=name, author=author, year_published=year, return_type=return_type)
    return redirect('/books/display')

@books.route('/return/<i>')
def return_book(i):
    today_date = date.today()
    dbms.update(mydatabase.LOANS,'returndate',today_date,"bookID",i )
    flash('success')
    return redirect('/books/display')

#DELETE BOOK ROUTE
@books.route('/delete/<i>')  
def del_book_by_id(i):
    print(i)
    dbms.delete_by_id(mydatabase.BOOKS,'id',i)
    return redirect('/books/display')    