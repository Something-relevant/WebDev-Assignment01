from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import random

app = Flask(__name__)

MENUDB = 'menu.db'
#table= wikipedia
#table = challengers

def fetchName(con):
    name=[]
    cur=conn.cursor()
    db="SELECT name FROM challengers ORDER BY ID DESC LIMIT 1"
    cur.execute(db)
    last_entry = cur.fetchone()
    for lastname in last_entry:
        print(lastname)

    return name



@app.route('/')
def index():

    #alias = {}
    #for input in request.form:
    #    if input == 'name':
    #        alias[input] = request.form[input]


    #con = sqlite3.connect(MENUDB)
    #name = fetchName(con)
    #con.close()
    return render_template('index.html', disclaimer='used for educational purposes')#remember to change

@app.route('/brief')
def brief():
    #con = sqlite3.connect(MENUDB)
    #name = fetchName(con)
    #con.close()
    return render_template('brief.html')

@app.route('/challenge')
def challenge():
    #con = sqlite3.connect(MENUDB)
    #menu = fetchMenu(con)
    #con.close()
    return render_template('challenge.html')

@app.route('/submission')
def submission():
    #con = sqlite3.connect(MENUDB)
    #name = fetchName(con)
    #con.close()
    return render_template('submission.html')
