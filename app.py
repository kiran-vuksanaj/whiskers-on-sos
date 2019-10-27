# Matthew Chan (PM), Hannah Fried, Coby Sontag, Jionghao Wu [Team SOS]
# SoftDev1 pd2
# P00 -- Da Art of Storytellin'
# 2019-10-28

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import sqlite3
import os
import utl.db as db

#=====SQLITE3 INITIALIZING CODE==================================
connector = sqlite3.connect("smallpox.db", check_same_thread=False)
cursor = connector.cursor()
# create table of users with a username and password tab
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT UNIQUE PRIMARY KEY, Password TEXT);")
# create stories table with title, entries and author columns
cursor.execute("CREATE TABLE IF NOT EXISTS stories(Title TEXT UNIQUE PRIMARY KEY, Entries TEXT, Author TEXT);")
#================================================================

app = Flask(__name__)
app.secret_key = os.urandom(32) # secret key set to randomly generated string

# Landing page
# Checks if user is logged in and redirects to either /home or /login
@app.route("/")
def root():
    print(__name__)
    if 'username' in session:
        return redirect("/home")
    else:
        return redirect("/login")

#=====RENDERING BASIC PAGES======================================

# Login page
@app.route("/login")
def login():
    print(__name__)
    return render_template("login.html")

# Home page
@app.route("/home")
def home():
    print(__name__)
    return render_template("home.html")

# Register page
@app.route("/register")
def register():
    print(__name__)
    return render_template("register.html")

# Creation page
@app.route("/create")
def create():
    print(__name__)
    return render_template("create.html")

# Browsing page
@app.route("/browse")
def browse():
    print(__name__)
    return render_template("browse.html")

# Contribution page
@app.route("/contribute")
def contribute():
    print(__name__)
    return render_template("contribute.html")

#=====RENDERING LOGIC PAGES======================================

# Authentication page for login
# Adds username to session
# Flashes user nonexistent and incorrect password error messages
@app.route("/login/authenticate", methods = ["POST"])
def authenticateLogin():
    print(__name__)
    username = request.form["username"]
    password = request.form["password"]
    if db.authenticate(cursor, username, password):     #Successful login goes /home
        session['username'] = username
        return redirect("/home")
    elif db.uniqueUsername(cursor, username):           #Unique username means they need to register
        flash("username does not exist")
        return redirect("/login")
    else:                                               #Last possible error, wrong password
        flash("incorrect password")
        return redirect("/login")

# Authentication page for register
# Adds username to session if unique
# Flashes existing user error message
@app.route("/register/authenticate", methods = ["POST"])
def authenticateRegister():
    print(__name__)
    username = request.form["username"]
    password = request.form["password"]
    if db.uniqueUsername(cursor, username):             #If new user, make their account and go home
        db.addUser(cursor, username, password)
        session['username'] = username
        return redirect("/home")
    else:                                               #Non unique username, try again
        flash("username already exists")
        return redirect("/register")

# Authentication page for create
# Addes story to DB if unique title
# Flashes success or non unique title error
@app.route("/create/authenticate", methods = ["POST"])
def authenticateCreate():
    print(__name__)
    if 'username' not in session:
        return redirect("/login")
    title = request.form["title"]
    text = request.form["text"]
    author = session['username']
    if db.uniqueTitle(cursor, title):                   #Unique title, make entry
        db.addEntry(cursor, title, text, author)
        flash("Story created")
        return redirect("/home")
    else:                                               #Non unique title, try again
        flash("title not unique")
        return redirect("/create")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

connector.commit() # save changes
connector.close()  # close database
