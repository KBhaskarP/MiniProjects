import sqlite3

conn=sqlite3.connect("books.sqlite") #To creqate a connection
cursor=conn.cursor()#To create a cursor through which sql commands can be executed

sql_query=""" CREATE TABLE book(
    
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
    
)"""
    
cursor.execute(sql_query)