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
    seeds = list(mongo.db.seeds.find().sort('_id', 1).limit(5))
    recents = list(mongo.db.seeds.find().sort('_id', -1).limit(3))
    return render_template("index.html",
                            seeds=seeds,
                            recents=recents)


@app.route("/seeds")
def seeds():
    seeds = mongo.db.seeds.find()
    categories = mongo.db.categories.find().sort(
        "category_name", 1)

    return render_template("seeds.html",
                            seeds=seeds,
                            categories=categories)


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
        return redirect(url_for(
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


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # Grab the session users username form the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    seeds = list(mongo.db.seeds.find(
        {"created_by": session["user"]}).sort("_id", -1))

    if session["user"]:
        return render_template("profile.html",
                                username=username,
                                seeds=seeds)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # If user is not logged in
    if "user" not in session:
        flash("You are already logged out")
        return redirect(url_for("home"))

    else:
        # Remove user from session cookies
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("login"))


@app.route("/seed/add", methods=["GET", "POST"])
def add_seed():
    if "user" not in session:
        flash("You need to be logged in to do that")
        return redirect(url_for("login"))

    elif request.method == "POST":
        seed = {
            "seed_name": request.form.get("seed_name").capitalize(),
            "category_name": request.form.get("category_name").capitalize(),
            "seed_description": request.form.get("seed_description"),
            "seed_image": request.form.get("seed_image"),
            "sowing_instructions": request.form.get(
                "sowing_instructions"),
            "growing_instructions": request.form.get(
                "growing_instructions"),
            "harvesting_instructions": request.form.get(
                "harvesting_instructions"),
            "created_by": session["user"]
        }
        mongo.db.seeds.insert_one(seed)
        flash("Seed Successfully Added")
        return redirect(url_for("seeds"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_seed.html", categories=categories)


@app.route("/seed/<seed_id>/edit", methods=["GET", "POST"])
def edit_seed(seed_id):

    seed = mongo.db.seeds.find_one({"_id": ObjectId(seed_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    seed_owner = seed["created_by"]

    if "user" not in session:
        flash("You need to be logged in to do that")
        return redirect(url_for("login"))

    elif session["user"] != "admin" and session["user"] != seed_owner:
        flash("This seed does not belong to you")

        return redirect(url_for("seeds"))

    elif request.method == "POST":
        edit = {"$set": {
            "seed_name": request.form.get("seed_name").capitalize(),
            "category_name": request.form.get("category_name").capitalize(),
            "seed_description": request.form.get("seed_description"),
            "seed_image": request.form.get("seed_image"),
            "sowing_instructions": request.form.get(
                "sowing_instructions"),
            "growing_instructions": request.form.get(
                "growing_instructions"),
            "harvesting_instructions": request.form.get(
                "harvesting_instructions"),
            "created_by": seed_owner
        }}
        mongo.db.seeds.update({"_id": ObjectId(seed_id)}, edit)
        flash("Seed Successfully Updated")
        return redirect(url_for("get_seed", seed_id=ObjectId(seed_id)))

    seed = mongo.db.seeds.find_one({"_id": ObjectId(seed_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_seed.html", seed=seed, categories=categories)


@app.route("/seed/<seed_id>/delete")
def delete_seed(seed_id):
    seed = mongo.db.seeds.find_one({"_id": ObjectId(seed_id)})
    seed_owner = seed["created_by"]

    if "user" not in session:
        flash("You need to be logged in to do that")
        return redirect(url_for("login"))

    elif session["user"] != "admin" and session["user"] != seed_owner:
        flash("This seed does not belong to you")

        return redirect(url_for("seeds"))

    else:
        mongo.db.seeds.remove({"_id": ObjectId(seed_id)})
        flash("Seed Successfully Deleted")
        return redirect(url_for("seeds"))


@app.route("/seed/<seed_id>/view")
def get_seed(seed_id):
    seed = mongo.db.seeds.find_one({"_id": ObjectId(seed_id)})

    return render_template("grow_seed.html", seed=seed)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    seeds = list(mongo.db.seeds.find({"$text": {"$search": query}}))
    return render_template("seeds.html", seeds=seeds)


@app.route("/filter", methods=["POST"])
def filter():
    category_name = request.form.get("category_name").capitalize()
    if category_name == "Herbs":
        seeds = list(mongo.db.seeds.find({"category_name": "Herbs"}))
    elif category_name == "Vegetables":
        seeds = list(mongo.db.seeds.find({"category_name": "Vegetables"}))
    elif category_name == "Houseplants":
        seeds = list(mongo.db.seeds.find({"category_name": "Houseplants"}))
    elif category_name == "Fruit":
        seeds = list(mongo.db.seeds.find({"category_name": "Fruit"}))
    elif category_name == "Flowers":
        seeds = list(mongo.db.seeds.find({"category_name": "Flowers"}))
    elif category_name == "All":
        seeds = mongo.db.seeds.find()

    return render_template(
                            "seeds.html",
                            seeds=seeds,
                            category_name=category_name)


# 404 ERROR
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', error=error), 404


# 500 ERROR
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
