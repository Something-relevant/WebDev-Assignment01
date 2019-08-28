from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from random import random
import time
app = Flask(__name__)

MENUDB = 'menu.db'
#table= wikipedia
#table = challengers

def fetchName(con):
    name=[]
    cur=con.cursor()
    db="SELECT name FROM challengers ORDER BY ID DESC LIMIT 1"
    cur.execute(db)
    last_entry = cur.fetchone()
    for lastname in last_entry:
        print(lastname)

    return name

def fetchChallenge(con):
    challenge=[]
    cur=con.cursor()
    db="SELECT challenge FROM challengers ORDER BY random() LIMIT 1"
    cur.execute(db)
    for challenge in cur:
        print(challenge)

    prevchallenger=[]
    cur=con.cursor()
    db="SELECT name FROM challengers ORDER BY random() LIMIT 1"
    cur.execute(db)
    for prevchallenger in cur:
        print(prevchallenger)

    return {'prevchallenger':prevchallenger, 'challenge':challenge}

#def Timer(seconds):
#    for i in range(seconds):

#        print(str(seconds) + "seconds remain")
#        seconds -= 1
#        time.sleep(1)

#    print("YOU FAILED")



@app.route('/')
def index():

    con = sqlite3.connect(MENUDB)
    lastuser = fetchName(con)
    con.close()
    return render_template('index.html', lastuser=lastuser)#remember to change

@app.route('/brief', methods=['POST'])
def brief():

    alias = {}
    for input in request.form:
        if input == 'name':
            alias[input] = request.form[input]


    print(request.form)
    con = sqlite3.connect(MENUDB)
    lastuser = fetchName(con)
    con.close()
    return render_template('brief.html', alias=alias,lastuser=lastuser)

@app.route('/challenge')
def challenge():
    con = sqlite3.connect(MENUDB)
    ch = fetchChallenge(con)
    con.close()
    #timer=Timer(240)
    return render_template('challenge.html', challenge=ch['challenge'], prevchallenger=ch['prevchallenger'])

@app.route('/submission')
def submission():
    print(request.form)
    con = sqlite3.connect(MENUDB)
    con.close()
    return render_template('submission.html')

@app.route('/Confirm', methods=['POST'])
def Confirm():
    alias = {}
    nxtchallenge={}
    for input in request.form:
        if input == 'name':
            alias[input] = request.form[input]

    for input in request.form:
        if input == 'nxtchallenge':
            nxtchallenge[input] = request.form[input]

    con = sqlite3.connect(MENUDB)
    name = fetchName(con)
    ch = fetchChallenge(con)
    cur = con.execute(
    'INSERT INTO challengers(name, challenge) VALUES(?, ?)',
    (alias['name'], nxtchallenge['challenge'])
    )
    con.commit()
    con.close()
    return render_template('index.html',alias=alias,nxtchallenge=nxtchallenge)
