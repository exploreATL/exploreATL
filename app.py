'''
Explore ATL
Michael Roussell
GSU CSC 4350 Software Engineering
Fall 2021

This is the app.py file used to run the program for the assignment.
Please run from this file as a class instance is created here and runs the operations.


Python 3.9.7 version of the python interpreter.

If there are any questions, please contact us at 'exploreatl.devs@gmail.com.
MIT Education License Preferred
'''
import os
import flask
from auth import User
from dbhandler import DBHandler
from flask import Flask, render_template, request, redirect, session, url_for, jsonify

global user
user = User(None, None, None, None)
dbhandler = DBHandler
app = Flask(__name__)

# Set User Login Page and Route.
@app.route('/')
def first():
    return redirect('signup')

@app.route("/signup")
def signup():
	return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
	if request.method == 'POST':
		empty = []
		DBHandler.insert_user(dbhandler, request.form['username'], request.form['password'], empty)
		return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
	return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
	error = None
	userinfo = DBHandler.lookup_user(dbhandler, request.form['username'], request.form['password'])
	if userinfo:
		user = User(userinfo[0][0], userinfo[0][2],  userinfo[0][3], userinfo[0][4])
		return flask.redirect(flask.url_for("profile"))
	return render_template('login.html', error='User Not Found')


# Set User Profile Page and Route
@app.route("/profile")
def profile():
	error = None
	return render_template('profile.html', error=error)

# Set User List Page and Route
@app.route("/index")
def bucket_list():
	error = None
	return render_template('pbucket_list.html', error=error)


# If launched from this file, run Flask app.
if __name__ == '__main__':
	app.run(
		host=os.getenv('IP', '0.0.0.0'),
    	port=int(os.getenv('PORT', 8080)),
    	debug=True
    )
