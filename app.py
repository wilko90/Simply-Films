import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/films")
def films():
    films = list(mongo.db.films.find())
    return render_template("films.html", films=films)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get("password") != request.form.get(
                "confirm-password"):
            flash("Passwords do not match!")
            return redirect(url_for("login"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            else:

                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("account.html", username=username)

    return redirect(url_for("login"))


@app.route('/logout')
def logout():
    """
    Logs user out.
    """
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for("login"))


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    if request.method == "POST":
        films = {
            "film_name": request.form.get("film_name"),
            "film_synopsis": request.form.get("film_synopsis"),
            "film_genre": request.form.get("film_genre"),
            "film_year": request.form.get("film_year"),
            "film_raiting": request.form.get("film_raiting"),
            "film_actors": request.form.get("film_actors"),
            "film_url": request.form.get("film_url"),
            "created_by": session["user"]
        }
        mongo.db.films.insert_one(films)
        flash("Film Successfully Added")
        return redirect(url_for("films"))
    return render_template("add_film.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
