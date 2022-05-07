# -----------------------------------
#      Database Model
# -----------------------------------

from datetime import datetime
from email.policy import default
import json
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,DateTime

# Global Variables
SQLITE = 'sqlite'

# Table Names
CUSTOMERS = 'customers'
BOOKS = 'books'
LOANS = 'loans'


class MyDatabase:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)

        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        # address = Table(ADDRESSES, metadata,
        #                 Column('id', Integer, primary_key=True),
        #                 Column('user_id', None, ForeignKey('users.id')),
        #                 Column('email', String, nullable=False),
        #                 Column('address', String)
        #                 )

        books = Table(BOOKS, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String),
                      Column('author', String),
                      Column('yearPublished', Integer),
                      Column('type', Integer)
                      )

        customers = Table(CUSTOMERS, metadata,      
  
                         Column('custID', Integer, primary_key=True),
                         Column('email', String),
                         Column('password', String),
                         Column('name', String),
                         Column('city', String),
                         Column('age', Integer)
                      )              

        loans = Table(LOANS, metadata,          

  
                      Column('custID', Integer),
                      Column('bookID', Integer),
                      Column('loandate', String),
                      Column('returndate', String)
                      )              
              

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '':
            return

        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def get_all_data(self, table='', query=''):
        query = query if query != '' else f"SELECT * FROM '{table}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append(row)
                result.close()
        return res

    # Use for all tables
    def delete_by_id(self, table, id):
        # Delete Data by Id
        query = f"DELETE FROM {table} WHERE id={id}"
        self.execute_query(query)

    def insert_book(self, name, author, year_published, return_type):
        # Insert Data
        query = f"INSERT INTO {BOOKS}(name, author, yearPublished, type) " \
                f"VALUES ( '{name}','{author}', {year_published}, {return_type});"
        self.execute_query(query)
        # self.get_all_data(BOOKS)

    def insert_customer(self, name, email,password,city, age):
        # Insert Data
        query = f"INSERT INTO {CUSTOMERS}(name, email, password,city,age) " \
                f"VALUES ( '{name}','{email}', '{password}','{city}',{age});"
        self.execute_query(query)

           


    def get_book_by_name(self, name):
        
        query = f"SELECT * FROM {BOOKS} WHERE name LIKE '{name}';"
        
        result = self.db_engine.connect().execute(query)
        return result.fetchone()

    

#loans

    def insert_loan(self,custID,bookID,loandate,returndate):
        query = f"INSERT INTO {LOANS}(custID, bookID,loandate,returndate) " \
                    f"VALUES ( {custID},{bookID},'{loandate}','{returndate}')"
        self.execute_query(query)
        
    def get_loan(self,book_id):
       query = f"SELECT name FROM {BOOKS} FULL OUTER JOIN loans ON {BOOKS.name} = {LOANS.book_id} WHERE condition;'"
        
       result = self.db_engine.connect().execute(query)
       return result.fetchone()

# LOGIN CHECK
    def check_login(self,email,password):
        query = f"SELECT password FROM customers WHERE email = '{email}'  and password = '{password}'"
        self.execute_query(query=query)
        return self.get_all_data(query=query)

    # GET DATA BY
    def get_data_by(self,some,tab,value,like):
        
        query = f"SELECT {some} FROM {tab} WHERE {value} = '{like}';"
        self.execute_query(query=query)
        return self.get_all_data(query=query)        

    # UPDAT
    def update(self,tab,set,data,where,data2):
            
            query = f"UPDATE {tab} set {set}='{data}' WHERE {where}='{data2}'" 
            self.execute_query(query)    

    #DELETE BY ID
    def delete_by_id(self, table, del_ID,id):
        
        
        query = f"DELETE FROM {table} WHERE {del_ID}={id}"
        self.execute_query(query)    