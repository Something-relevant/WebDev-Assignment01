from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from random import random

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

def fetchChallenge(con):
    challenge=[]
    cur=conn.cursor()
    db="SELECT challenge FROM challengers ORDER BY random() LIMIT 1"
    cur.execute(db)
    for challenge in cur:
        print(challenge)

    return challenge



@app.route('/', methods=['POST'])
def index():

    alias = {}
    for input in request.form:
        if input == 'name':
            alias[input] = request.form[input]


    con = sqlite3.connect(MENUDB)
    lastuser = fetchName(con)
    con.close()
    return render_template('index.html',alias=alias,lastuser=lastuser)#remember to change

@app.route('/brief')
def brief():
    print(request.form)
    con = sqlite3.connect(MENUDB)
    lastuser = fetchName(con)
    con.close()
    return render_template('brief.html', alias=alias,name=name)

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
