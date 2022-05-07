from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from BooksStoreProject.database import mydatabase
customers = Blueprint('customers',__name__, url_prefix='/customers')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='bookstore.sqlite')



#CUSTOMER SECTION
@customers.route('/add_form', methods=['GET'])
def add_form():
  
    return render_template("add_customer.html") 

# SING UP ROUTE
@customers.route('/singup', methods = ['POST','GET'])
def add_new_customer():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        city = request.form['city']
        age = request.form['age']
        var = dbms.get_data_by('email',mydatabase.CUSTOMERS,'email',email)
        print(var)
        if var == []:
            dbms.insert_customer(name,email,password,city,age)
            return redirect(url_for('customers.login'))
        else: flash(' Email Already Exists')
              
    return render_template('singup.html')  


# LOG IN ROUTE
@customers.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        check = dbms.check_login(email,password)

        print(f'the result is {check}')
        if check != [] :
            session['email'] = email
            session['password'] = password
            print(session)
            name = dbms.get_data_by('name',mydatabase.CUSTOMERS,'email',email)
            for n in name:
                var = str(n).strip('(').strip(')').strip("'").strip(',').strip("'")
            session['name'] = var
            return redirect(url_for('books.books_display'))

        else: 
            flash('Not Correct! Try again','info')
            return render_template('login.html')       
    else:
        return render_template('login.html')    


# LOG OUT ROUTE
@customers.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect(url_for('customers.login'))

@customers.route('/delete', methods=['POST'])
def delete_customer():
    customer_id = request.form.get('customer_id')
    dbms.delete_by_id(table=mydatabase.CUSTOMERS, id=customer_id)
    return "success"



# FIND CUST BY NAME
@customers.route('/find', methods=["POST",'GET'])
def find_customer():
    
    if request.method == "POST":
        data = request.form['search']
        res = dbms.get_data_by('*',mydatabase.CUSTOMERS,'name',data)
        if res ==[]:flash('No results')
        return render_template('cust_by_name.html',res=res)
    return render_template('cust_by_name.html')

@customers.route('/display')
def display_customers():
    res = dbms.get_all_data(mydatabase.CUSTOMERS)
    if res ==[]:flash('No results')
    return render_template('customers_display.html',res=res)  

#DELETE CUSTOMER ROUTE
@customers.route('/delete_cust/<i>')
def del_cust_by_id(i):
    print(i)
    dbms.delete_by_id(mydatabase.CUSTOMERS,'custID',i)
    return redirect('/customers/display')      