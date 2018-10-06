# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:12:05 2018

@author: User
"""

# Database connection
import pymysql as sql

# open a database connection
db = sql.connect("localhost", "root", "1234", "web_scrap")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute a sql query using execute() method
cursor.execute("SELECT * FROM web_scrap.sitenames")

# fetch row from databases
datas = cursor.fetchall()

# print datas
for data in datas:
     print("url: ",data[1],", category: ",data[2])  




