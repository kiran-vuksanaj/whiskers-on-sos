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
def hello_world():
    print(__name__)
    if 'username' in session:
        return redirect("/home")
    else:
        return redirect("/login")

# Login page
@app.route("/login")
def login():
    return render_template("login.html")

# Authentication page for login
# Flashes appropriate error messages
@app.route("/login/auth", methods = ["POST"])
def authenticateLogin():
    username = request.form["username"]
    password = request.form["password"]
    if db.authenticate(cursor, username, password):
        return redirect("/home")
    '''
    =====TEMPORARILY NOT FLASHING=====
    else if userExists?(username):
        flash("incorrect password")
        return redirect("/login")
    else:
        flash("username does not exist")
        return redirect("/login")
    '''
    flash("Error: something went wrong") # TEMP flash message placeholder
    return redirect("/login")

@app.route("/home")
def homePage():
    return render_template("home.html")



if __name__ == "__main__":
    app.debug = True
    app.run()

connector.commit() # save changes
connector.close()  # close database