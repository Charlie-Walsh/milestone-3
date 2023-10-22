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


@app.route("/books", methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        db.session.add(Title(book_title = request.form.get('book_title'), author_id = request.form.get('author_id')))
        db.session.commit()
        return redirect(url_for('books'))
    books = list(Title.query.order_by(Title.book_title).all())
    authors = list(Author.query.all())       
    return render_template("books.html", books=books, authors=authors)


@app.route("/reviews/edit/<int:review_id>", methods=['GET','POST'])
def edit_review(review_id):
    review = Review.query.get(review_id)
    if request.method == 'POST':
        review.review = request.form.get('review')
        review.rating = request.form.get('rating')
        db.session.commit()
        return redirect(url_for('reviews'))
    return render_template("edit-review.html", review=review )



@app.route("/reviews/delete/<int:review_id>", methods=['GET','POST'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    print(review)
    if request.method == 'POST':
        db.session.delete(review)
        db.session.commit()
        return redirect(url_for('reviews'))
    return render_template("delete-review.html", review=review )


@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
    books = list(Title.query.order_by(Title.book_title).all())
    reviews = list(Review.query.all())
    if request.method == 'POST':
        db.session.add(Review(review=request.form.get('review'), rating=request.form.get('rating'), title_id=request.form.get('book_id')))
        db.session.commit()
        return redirect(url_for('reviews'))
    return render_template("reviews.html", books=books, reviews=reviews)


@app.route("/reviews/view/<int:review_id>", methods=['GET'])
def review(review_id):
    review = Review.query.get(review_id)
    return render_template("view-review.html", review=review )