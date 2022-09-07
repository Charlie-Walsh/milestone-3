from flask import render_template, request, redirect, url_for
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


@app.route("/review", methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        author_fname = Author(author_fname=request.form.get('author_fname'))
        db.session.add(author_fname)
        db.session.commit()
        author_lname = Author(author_lname=request.form.get('author_lname'))
        db.session.add(author_lname)
        db.session.commit()
        book_title = Title(book_title=request.form.get('book_title'))
        db.session.add(book_title)
        db.session.commit()
        rating = Title(rating=request.form.get('rating'))
        db.session.add(rating)
        db.session.commit()
        book_review = Review(review=request.form.get('review'))
        db.session.add(book_review)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template("review.html")
