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
from flask import Flask, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__)

# Set User Login Page and Route.
@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    return render_template('login.html', error=error)


# Set User Profile Page and Route
def profile():
	error = None
	return render_template('profile.html', error=error)


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
