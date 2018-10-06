# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:43:01 2018

@author: User
"""

import pymysql as sql
    
# prepare initial connection
def open_database_connection():
    try:
        db = sql.connect("localhost", "root", "1234", "web_scrap")
        return db
    except ConnectionError as ce:
        print("Connection Error: Check Database Connection. Detail", ce.strerror)

# creating database table
def create_new_table(db):
    cursor = db.cursor()
    try: 
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        query = """CREATE TABLE EMPLOYEE (
           FIRST_NAME  CHAR(20) NOT NULL,
           LAST_NAME  CHAR(20),
           AGE INT,  
           SEX CHAR(1),
           INCOME FLOAT )"""
        
        cursor.execute(query)
    except sql.Error as e:
        print("Problem in creating table. Details: ", e.args)
        
# insert data into the table
def insert_data(db):
    cursor = db.cursor()
    try: 
        query = """INSERT INTO EMPLOYEE(FIRST_NAME,
           LAST_NAME, AGE, SEX, INCOME)
           VALUES ('Mac', 'Mohan', 20, 'M', 2000), 
           ('Mark', 'Joel', 30, 'M', 3500)"""
        
        cursor.execute(query)
        db.commit()
    except sql.Error as e:
        db.rollback()
        print("Problem in creating table. Details: ", e.args)
        
def close_connection(db):
    db.close()
    
def retreive_data(database):
    cursor = database.cursor()
    try: 
        sql = "SELECT * FROM EMPLOYEE \
              WHERE INCOME > '%d'" % (1000)
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
          fname = row[0]
          lname = row[1]
          age = row[2]
          sex = row[3]
          income = row[4]
          # Now print fetched result
          print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
             (fname, lname, age, sex, income ))
    except sql.Error as e:
        print("Problem in creating table. Details: ", e.args)
## read databes data
    # fetch operation
    # fetchone() -  It fetches the next row of a query result set. 
    # fetchall() - It fetches all the rows in a result set. 
    # rowcount() - This is a read-only attribute and returns the number of rows that were affected by an execute() method.
        
# database operation
database = open_database_connection()
#create_new_table(database)
#insert_data(database)
retreive_data(database)
close_connection(database)


        
