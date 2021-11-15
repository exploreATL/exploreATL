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
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from near_places import NearPlaces

# Set React Route
app = Flask(__name__, static_folder="./build/static")
bp = flask.Blueprint("bp", __name__, template_folder="./build")

@bp.route("/index")
def index():
    return flask.render_template("index.html")

app.register_blueprint(bp)

# Set User Login Page and Route.
@app.route('/')
def first():
    return redirect('signup')

@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    return flask.redirect(flask.url_for("bp.index"))


# Set User Profile Page and Route
def profile():
	error = None
	return render_template('profile.html', error=error)


def bucket_list():
	error = None
	return render_template('pbucket_list.html', error=error)


# If launched from this file, run Flask app.
# if __name__ == '__main__':
# 	app.run(
# 		host=os.getenv('IP', '0.0.0.0'),
#     	port=int(os.getenv('PORT', 8080)),
#     	debug=True
#     )
@app.route("/nearby", methods=["POST"])
def nearby():
	location = request.json.get("location")
	type = request.json.get("type")
	nearby_places = NearPlaces.getNearPlace(location, type)
	return jsonify({"nearby_places": nearby_places})


@app.route("/")
def main():
    return flask.redirect(flask.url_for("bp.index"))


# If launched from this file, run Flask app.
app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8081)),
)