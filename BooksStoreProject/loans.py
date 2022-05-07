from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from BooksStoreProject.database import mydatabase
from datetime import date

loans = Blueprint('loans',__name__, url_prefix='/loans')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='bookstore.sqlite')



#loans section

@loans.route('/get_buti', methods=['GET'])
def get_loans():
    res = dbms.get_all_data(mydatabase.LOANS)
    if res ==[]:flash('No results')
    return render_template('get_buti_loan.html',res=res)

@loans.route('/get/<b>', methods=['GET'])
def getDetails(b):
    try:
        var=dbms.get_data_by('custID',mydatabase.CUSTOMERS,'email',session['email'])
        for x in var:
            a = str(x).strip('(').strip(')').strip(',')
        custID = a
        bookID = str(b).strip("'")
        loandate = date.today()
        returndate ='Not yet'
        dbms.insert_loan(custID,bookID,loandate,returndate)
        flash('SUCSSES')
        return redirect('/loans/get_buti')
    except Exception as x:
        print(x)    

        return render_template('booksDisplay.html')





#LATE LOANS ROUTE
@loans.route('/display/late_loans')
def display_late_loans():
    all_loans = dbms.get_all_data(mydatabase.LOANS)

    type1 = 10
    type2 = 5
    type3 = 2
    
    try:
        # BOOK TYPE
        loan_book_type = dbms.get_all_data( query='select "book_type" from Books inner join loans on books.id = loans.bookID and loans.returndate ="Not Yet"')
        for book in loan_book_type:
            book_type  = str(book).strip('(').strip(')').strip(',')

        # LOAN DAYS
        loan_date = dbms.get_all_data( query='select "loandate" from loans  inner join Books on books.id = loans.bookID and loans.returndate ="Not Yet"')
        for dat in loan_date:
            date_str  = str(dat).strip('(').strip(')').strip(',').strip("'")
            splited_date = date_str.split('-')
            y = int(splited_date[0])
            m = int(splited_date[1])
            d = int(splited_date[2])
            loan_date_fin = date(y,m,d)
            today_date = date.today()
            loan_days = (today_date-loan_date_fin).days
            


        if int(book_type) == 1:
            if type1 < loan_days:
                print(f'book_type1 = {book_type}')
                cont = {"all_loans":all_loans, "late":f'{type1 - loan_days} days late'  }
                return render_template("late_loans.html",cont= cont)

        if int(book_type) == 2:
            if type2 < loan_days:
                cont = {"all_loans":all_loans, "late":f'{type2 - loan_days} days late'  }
                
                return render_template("late_loans.html",cont = cont)       
        if int(book_type) == 3:
            if type3 < loan_days:
                cont = {"all_loans":all_loans, "late":f'{type3 - loan_days} days late'  }
                return render_template("late_loans.html",cont= cont)
        else:
            flash('No results')
            cont = {"all_loans":all_loans, "late":'None'  }
            return render_template("late_loans.html",cont= cont)

    except Exception as e:
        print(e)
        flash('No results')
        return render_template("late_loans.html",cont= {"all_loans":all_loans, "late":'None'  })