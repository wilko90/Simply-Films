import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import math

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/films')
def films():
    limit_per_page = 8
    
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.films.count()
    pages = range(1, int(math.ceil(total / limit_per_page)) + 1)
    films = list(mongo.db.films.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page))
    return render_template("films.html", films=films,
                           current_page=current_page,
                           pages=pages, total=total)


@app.route('/manage_films/<username>', methods=['GET', 'POST'])
def manage_films(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    my_films = list(mongo.db.films.find({
                          "created_by": username}).sort("film_name", 1))
    if session['user']:
        return render_template(
            "manage_films.html", username=username,
            my_films=my_films) 
    limit_per_page = 8
    current_page = int(request.args.get('current_page', 1))
    total = my_films.count()
    pages = range(1, int(math.ceil(total / limit_per_page)) + 1)
    films = my_films.sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)
    return render_template("manage_films.html", films=films,
                           current_page=current_page,
                           pages=pages, total=total, my_films=my_films)

                           

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    films = list(mongo.db.films.find({"$text": {"$search": query}}))
    return render_template("films.html", films=films)

@app.route("/")
@app.route("/home")
def home():
    trending_films = ([films for films in mongo.db.films.aggregate([{"$sample": {"size": 4}}])])
    return render_template('home.html', trending_films=trending_films)


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
                return redirect(url_for("home"))
            else:

                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


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


@app.route("/film_card/<film_id>")
def film_card(film_id):
    selected_film_card = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    selected_film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    return render_template("film_card.html",
                           selected_film_card=selected_film_card,
                           selected_film=selected_film)


@app.route("/edit_film/<film_id>", methods=["GET", "POST"])
def edit_film(film_id):
    if request.method == "POST":
        film_update = {
            "film_name": request.form.get("film_name"),
            "film_synopsis": request.form.get("film_synopsis"),
            "film_genre": request.form.get("film_genre"),
            "film_year": request.form.get("film_year"),
            "film_raiting": request.form.get("film_raiting"),
            "film_actors": request.form.get("film_actors"),
            "film_url": request.form.get("film_url"),
            "created_by": session["user"]
        }
        mongo.db.films.update({"_id": ObjectId(film_id)}, film_update)
        flash("Film Successfully Updated")  
    selected_film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    selected_film_card = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    return render_template("edit_film.html",
                           selected_film=selected_film,
                           selected_film_card=selected_film_card)


@app.route("/delete_film/<film_id>")
def delete_film(film_id):
    mongo.db.films.remove({"_id": ObjectId(film_id)})
    flash("Film Successfully Deleted")
    return redirect(url_for("films"))


@app.errorhandler(404)
def error_404(error):
    '''
    Handles 404 error (page not found)
    '''
    return render_template('errors/404.html', error=True,
                           title="Page not found"), 404


@app.errorhandler(500)
def error_500(error):
    '''
    Handles 500 error (internal server error)
    '''
    return render_template('errors/500.html', error=True,
                           title="Internal Server Error"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
