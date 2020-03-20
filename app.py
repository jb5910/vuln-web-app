#!/usr/bin/env python3

from flask import Flask, request, abort, render_template_string
import pymysql.cursors
import os.path

conn = pymysql.connect(host='localhost',
                       port = 3306,
                       user='root',
                       password='',
                       db='vuln_app',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    h = request.args.get("hello")
    if h:
        return render_template_string(open("templates/home.html").read().format(hey=h, error='', note=''))
    return render_template_string(open('templates/home.html').read().format(hey='you have not said anything previously', error='', note=''))

@app.route("/login")
def login():
    uname = request.args.get('username')
    pwd = request.args.get('pwd')
    ins = "SELECT * FROM users WHERE username = \'" + uname + "\' AND password = \'" + pwd + "\'"
    cursor = conn.cursor()
    cursor.execute(ins)
    user = cursor.fetchall()
    cursor.close()
    if user:
        return render_template_string(open('templates/index.html').read().format(user))
    else:
        return render_template_string(open("templates/home.html").read().format(hey='', error='', note='Invalid Login'))

@app.route('/register')
def register():
    uname = request.args.get('username')
    pwd = request.args.get('pwd')
    pwd2 = request.args.get('pwd2')
    ins = "SELECT * FROM users WHERE username = \'" + uname + "\'"
    cursor = conn.cursor()
    cursor.execute(ins)
    user = cursor.fetchall()
    cursor.close()
    if user:
        return render_template_string(open('templates/home.html').read().format(hey='', error="User already exists. Please login.", note=''))
    else:
        if pwd != pwd2:
            return render_template_string(open('templates/home.html').read().format(hey='', error="Passwords not equal. Please try again.", note=''))
        else:
            ins = "INSERT INTO users VALUES (%s, %s)"
            cursor = conn.cursor()
            cursor.execute(ins, (uname, pwd))
            cursor.close()
            return render_template_string(open('templates/home.html').read().format(hey='', error="", note = "Thanks! You can log in now"))


app.secret_key = 'superdupersecretkey'
if __name__ == "__main__":
    app.run("localhost", 2520, debug=True)