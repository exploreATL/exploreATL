"""
Explore ATL
Michael Roussell
GSU CSC 4350 Software Engineering
Fall 2021

This is the app.py file used to run the program for the assignment.
Please run from this file as a class instance is created here and runs the operations.


Python 3.9.7 version of the python interpreter.

If there are any questions, please contact us at 'exploreatl.devs@gmail.com.
MIT Education License Preferred
"""
import os
import flask
from auth import User
from dbhandler import DBHandler
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from near_places import NearPlaces


# Set React Route and app blueprint
app = Flask(__name__, static_folder="./build/static")
bp = flask.Blueprint("bp", __name__, template_folder="./build")

# Create User and DBHandler
global user
user = User(None, None, None, None)
dbhandler = DBHandler


@bp.route("/index")
def index():
    return flask.render_template("index.html")


app.register_blueprint(bp)

# Set User Login Page and Route.
@app.route("/")
def first():
    return redirect("signup")


@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    if request.method == "POST":
        empty = []
        DBHandler.insert_user(
            dbhandler, request.form["username"], request.form["password"], empty
        )
        return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    error = None
    userinfo = DBHandler.lookup_user(
        dbhandler, request.form["username"], request.form["password"]
    )
    if userinfo:
        user = User(userinfo[0][0], userinfo[0][2], userinfo[0][3], userinfo[0][4])
        return flask.redirect(flask.url_for("bp.index"))
    return render_template("login.html", error="User Not Found")


# Set User Profile Page and Route
@app.route("/profile")
def profile():
    error = None
    return render_template("profile.html", error=error)


# Set User List Page and Route
@app.route("/index")
def bucket_list():
    error = None
    return render_template("pbucket_list.html", error=error)


@app.route("/nearby", methods=["POST"])
def nearby():
    location = request.json.get("location")
    type = request.json.get("type")

    """
	1. search if the database contains info with the same userid, location, type
	2. if true, then get data from database and return
	3. if not, then call the google places API to get the data and store into the database

    result = Table.query.filter_by(username=current_user.username, location=location, type=type).all()
	if result:
		places = result.LIST
		visited = result.BEEN
		return jsonify({"nearby_places": places, "visited": visited})
	else:
		nearby_places = NearPlaces.getNearPlace(location, type)
		visited =  [False for i in range(5)]
		db_data = {USER_ID: current_user.username, PASS: password, 
			TYPE: type, LIST: nearby_places, BEEN: visited, REVIEW text[5]..., PRIMARY KEY (USER_ID)...}
		insert db_data to database
		return jsonify({"nearby_places": places, "visited": visited})

	"""
    visited = [False for i in range(5)]
    nearby_places = NearPlaces.getNearPlace(location, type)
    return jsonify({"nearby_places": nearby_places, "visited": visited})


@app.route("/explore", methods=["POST"])
def explore():
    places = request.json.get("places")
    been = request.json.get("been")
    print(places)
    print(been)
    # update the database
	# add exception handle
    return flask.jsonify({"status": 200, "reason": "Success"})


@app.route("/")
def main():
    return flask.redirect(flask.url_for("bp.index"))


# If launched from this file, run Flask app.
app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8081)),
)
