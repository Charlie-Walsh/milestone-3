from sanctum import db


class Title(db.Model):
    # schema for Title model
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(), nullable=False)
    average_rating = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return self.book_title


class Author(db.Model):
    # schema for Author model
    id = db.Column(db.Integer, primary_key=True)
    author_fname = db.Column(db.String(20), nullable=False)
    author_lname = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self


class Review(db.Model):
    # schema for Review model
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey(), nullable=False)

    def __repr__(self):
        return self



