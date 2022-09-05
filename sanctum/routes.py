from flask import render_template
from sanctum import app, db
from sanctum.models import Title, Author, Review


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/books")
def books():
    return render_template("books.html")


@app.route("/review")
def review():
    return render_template("review.html")
