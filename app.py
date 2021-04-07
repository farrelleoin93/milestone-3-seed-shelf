import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
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
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/seeds")
def seeds():
    seeds = mongo.db.seeds.find()
    return render_template("seeds.html", seeds=seeds)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("I'm sorry, this username is taken.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Your registation was sucessfull")
        return render_template(url_for(
            "profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username is already in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user[
                    "password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session users username form the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_seed", methods=["GET", "POST"])
def add_seed():
    if request.method == "POST":
        seed = {
            "seed_name": request.form.get("seed_name"),
            "category_name": request.form.get("category_name"),
            "seed_description": request.form.get("seed_description"),
            "seed_image": request.form.get("seed_image"),
            "sowing_instructions": request.form.get(
                "sowing_instructions").splitlines(),
            "growing_instructions": request.form.get(
                "growing_instructions").splitlines(),
            "harvesting_instructions": request.form.get(
                "harvesting_instructions").splitlines(),
            "created_by": session["user"]
        }
        mongo.db.seeds.insert_one(seed)
        flash("Seed Successfully Added")
        return redirect(url_for("seeds"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_seed.html", categories=categories)


@app.route("/get_seed/<seed_id>")
def get_seed(seed_id):
    seed = mongo.db.seeds.find_one({"_id": ObjectId(seed_id)})

    return render_template("grow_seed.html", seed=seed)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    seed = list(mongo.db.seeds.find_one({"$text": {"$search": query}}))
    return render_template("seeds.html", seed=seed)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
