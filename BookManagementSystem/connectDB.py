import os
import time

import mysql.connector
import pymongo
import pandas as pd
import sqlite3 as sq

'''Functions for interacting with excelDB and SqLiteDB'''

path = '/Main projects/BookManagementSystem/Database'
excelDbFilePath = path + "/booksDB.xlsx"
sqliteFilePath = path + "/books.db"
headColumns=['book_id','user', 'book_name', 'book_author', 'book_pages', 'book_type', 'book_saved']


#SQLite Database
#books.db
def connectSqLite():
    with sq.connect(sqliteFilePath) as connect:   # could be .db  .db3 .sqlite .sqlite3
        cursor = connect.cursor()    # create cursor instance
        print("* Connecting to 'books.db'... ")
        cursor.execute(''' CREATE TABLE IF NOT EXISTS books (    
                book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                user TEXT,
                book_name TEXT,
                book_author TEXT,
                book_pages TEXT,
                book_type TEXT,
                book_saved TEXT) ''')
        return connect, cursor
def saveToSqLite(data):
    connect, cursor = connectSqLite()
    cursor.execute('''INSERT INTO books (user,book_name, book_author, book_pages,
                      book_type, book_saved) VALUES(?, ?, ?, ?, ?, ?)  ''', data)
    connect.commit()
    connect.close()
    print("* Data saved to 'books.db' ")
def selectInSqlLite(query):
    connect,cursor = connectSqLite()
    data = cursor.execute(query)
    return data

def deleteAllrecordsInSqLite():
    connect, cursor = connectSqLite()
    cursor.execute('''DELETE FROM books''')
    connect.commit()
    connect.close()
    print("All data in 'books.db' have been deleted")


#Excel File Database
def callExcelDb():
    if not os.path.exists(excelDbFilePath):
        print("* File: 'booksDB.xlsx' does not exist...")
        excelBooksDB = pd.DataFrame(columns=headColumns)
        print("* File: 'booksDB.xlsx' created")
    else:
        print('* Reading file: "booksDB.xlsx"...')
        excelBooksDB = pd.read_excel(excelDbFilePath, index_col=0)
    return excelBooksDB
def saveToExcelDb(dataframe):
    excelBooksDB = callExcelDb()
    excelBooksDB = pd.concat([excelBooksDB, dataframe])
    excelBooksDB.to_excel(excelDbFilePath, index=False)
    print("* Data saved to 'booksDB.xlsx' ")





