'''All functions that necessary for application'''
import datetime

import flask
import pandas as pd

from connectDB import callExcelDb
from flask import Flask, render_template, request



def collectData():
    today = str(datetime.date.today())
    name = request.form.get('name')
    author = request.form.get('author')
    pages = request.form.get('pages')
    booktype = request.form.get('type')
    if name == '':
        name = 'name'
        flask.flash("name is empty", category='error')
    if author == "":
        author = 'author'
    if pages == "":
        pages = '0'
        flask.flash("0 pages",category='error')
    pages = pages + ' pages'
    return name, author, pages, booktype, today

def createDf(name, author, pages, booktype, today):
    excelBooksDB = callExcelDb()
    data = pd.DataFrame([{
        'book_id':     1 + len(excelBooksDB),
        'user': 'Bohdan',
        'book_name':   name,
        'book_author': author,
        'book_pages':  pages,
        'book_type':   booktype,
        'book_saved':  today
    }])
    return data

