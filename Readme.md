 Author: idan hilel
 age:23
 contry:israel

 about me: lernin in jhon bryce python web develpomen
 about the project: SQL alchemy with conection to flask 
 web to library worked with data

# HOW TO USE
 1. run wsgi.py file
 2. copy the path from the terminal and copy to brwoser
 3. now all action you will do you can see in the terminal what happend.
 4. OR you can go to this URL:https://librarysqlalchemy.herokuapp.com/ 
    if you dont want to sing up - email: roni@gmail.com  password: 1234 

  
  
  # In this project you will implement a simple system to manage books library 

   1. Create a simple sqlite database with 3 tables: -DONE ALL
    # Books 
    Id (PK)
    Name  
    Author 
    Year Published 
    Type (1/2/3) 
    
    # Customers 
     Id (PK)
     Name  
     City  
     Age 
      
    # Loans 
    CustID   
    BookID 
    Loandate  
    Returndate 
    
    2. The book type set the maximum loan time for the book: - DONE All
     1. – up to 10 days 
     2. – up to 5 days
     3. – up to 2 days 
     
    3. 
    1. Create the DAL: Build a class for each entity  -DONE
    2. Create a separate module for each class -DONE
    3. Build unit tests -DONE - if you run the program from the terminal Any        action will be printed in the terminal.


    # Build a client application to use the DAL. 
    1. Add the following operations (display a simple menu) -DONE
    2. Add a new customer -DONE
    3. Add a new book  -DONE
    4. Loan a book  - DONE
    5. Return a book -DONE
    6. Display all books -DONE
    7. Display all customers - DONE
    8. Display all loans  -DONE
    9. Display late loans -DONE
    10. Find book by name - DONE
    11. Find customer by name -DONE
    12. Remove book  -DONE
    13. Remover customer -DONE