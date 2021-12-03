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
import json
from flask.helpers import flash
import flask_login
from dotenv import load_dotenv
from auth import User
from dbhandler import DBHandler
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for,
    jsonify,
    flash,
)
from flask_login import login_user
from near_places import NearPlaces

# Set React Route and app blueprint
app = Flask(__name__, static_folder="./build/static")
bp = flask.Blueprint("bp", __name__, template_folder="./build")
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")


# Create DBHandler Object
dbhandler = DBHandler

# Create Flask-Login User
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
global user
user = User(None, None, None, None, None, None)

# Create User Loader
@login_manager.user_loader
def load_user(id):
    return User.get(id)


# Used for error handling and sercurity so that unsigned in users are redirected.
@bp.route("/index")
def index():
    error = None
    if not user.id:
        return redirect(url_for("login"))
    data = json.dumps({"username": user.id})
    return flask.render_template("index.html", data=data)


# Load Blueprint for React
app.register_blueprint(bp)

# # Set Landing Page as the default page.
@app.route("/")
def first():
    return redirect("landpage")

# @app.route("/")
# def first():
#     return redirect("index")


# Landing Page Routing.
@app.route("/landpage")
def landpage():
    return flask.render_template("landpage.html")


# Sign up page rendering.
@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


# Sign up page logic for unregistered user.
@app.route("/signup", methods=["POST"])
def signup_post():
    if request.method == "POST":
        error = None
        empty = []
        try:
            result = DBHandler.insert_user(
                dbhandler, request.form["username"], request.form["password"], empty
            )
        except ValueError:
            result = 1
        if result == 0:
            return flask.redirect(flask.url_for("login"))
        flash("User Already Exists. Try logging in instead!")
        return flask.render_template("signup.html", error="User Already Exists")


# Login page rendering.
@app.route("/login")
def login():
    return flask.render_template("login.html")


# Login Page Logic for registered users.
@app.route("/login", methods=["POST"])
def login_post():
    error = None
    userinfo = DBHandler.lookup_user(
        dbhandler, request.form["username"], request.form["password"]
    )
    if userinfo == 1:
        flash("User Not Found. Try creating an account!")
        return render_template("login.html", error="User Not Found")
    if userinfo:
        global user
        user = User(
            userinfo[0][0],
            userinfo[0][2],
            userinfo[0][3],
            userinfo[0][4],
            userinfo[0][5],
            userinfo[0][6],
        )
        flask_login.login_user(user, force=True, remember=True)
        return flask.redirect(flask.url_for("bp.index"))
    return render_template("login.html", error="User Not Found")


# Near by logic for React Component
@app.route("/nearby", methods=["POST"])
def nearby():

    location = request.json.get("location")
    type = request.json.get("type")
    global user

    # If user goes to same location and location type
    if user.id != None and location == user.location and type == user.loc_type:
        # Load User's dat from User Object attributes.
        location = user.location
        type = user.loc_type
        visited = user.check_list
        nearby_places = user.user_list
        review = ""
        print(f"User '{user.id}' not found")
    else:
        visited = [False for i in range(3)]
        nearby_places = NearPlaces.getNearPlace(
            location,
            type,
        )
        review = ""

        # store info for user into database
        DBHandler.update_list(
            dbhandler, user.id, location, type, nearby_places, visited, review
        )
        print(f"User '{user.id}' data updated and stored")

    return jsonify(
        {"nearby_places": nearby_places, "visited": visited, "review": review}
    )

# @app.route("/nearby", methods=["POST"])
# def nearby():
#     location = request.json.get("location")
#     type = request.json.get("type")
#     # global user
#     visited = [False for i in range(3)]
#     nearby_places = NearPlaces.getNearPlace(
#         location,
#         type,
#     )
#     review = ""

#     return jsonify(
#         {"nearby_places": nearby_places, "visited": visited, "review": review}
#     )




# Route and logic for explore
@app.route("/explore", methods=["POST"])
def explore():
    places = request.json.get("places")
    been = request.json.get("been")
    review = request.json.get("review")
    global user
    print(places)
    print(been)
    print(review)
    print(user.id)
    
    # update the database

    DBHandler.update_review(dbhandler, user.id, been, review)
	  # add exception handle

    return flask.jsonify({"status": 200, "reason": "Success"})


# redirects to  blueprint
@app.route("/")
def main():
    return flask.redirect(flask.url_for("bp.index"))


# If launched from this file, run Flask app.
app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
)
