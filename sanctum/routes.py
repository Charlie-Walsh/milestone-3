from flask import render_template, request, redirect, url_for
from sanctum import app, db
from sanctum.models import Title, Author, Review


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/authors", methods=['GET', 'POST'])
def authors():
    if request.method == 'POST':
        author = Author(author_fname=request.form.get('author_fname'),
        author_lname=request.form.get('author_lname'))
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('authors'))
    authors = list(Author.query.all())        
    return render_template("authors.html", authors=authors)

@app.route("/books")
def books():
    library = list(Title.query.order_by(Title.book_title).all())
    return render_template("books.html", books=library)


@app.route("/review", methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        author = Author(author_fname=request.form.get('author_fname'),
        author_lname=request.form.get('author_lname'))
        db.session.add(author)
        db.session.commit()
        book_title = Title(book_title=request.form.get('book_title'))
        db.session.add(book_title)
        rating = Review(rating=request.form.get('rating'))
        db.session.add(rating)
        book_review = Review(review=request.form.get('review'))
        db.session.add(book_review)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template("review.html")


@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
    books = list(Title.query.order_by(Title.book_title).all())
    reviews = list(Review.query.all())
    if request.method == 'POST':
        db.session.add(Review(review=request.form.get('review'), rating=request.form.get('rating'), title_id=request.form.get('book_id')))
        db.session.commit()
        return redirect(url_for('reviews'))
    return render_template("reviews.html", books=books, reviews=reviews)
