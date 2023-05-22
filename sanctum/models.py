from sanctum import db


class Title(db.Model):
    # schema for Title model
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    reviews = db.relationship("Review", backref='title', cascade="all, delete",
                              lazy=True)
    authors = db.relationship("Author")

    def __repr__(self):
        return f"Title - #{self.book_title} #{self.author_id}".format(self.book_title, self.author_id)


class Author(db.Model):
    # schema for Author model
    id = db.Column(db.Integer, primary_key=True)
    author_fname = db.Column(db.String(50), nullable=False)
    author_lname = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Author - #{self.author_fname} #{self.author_lname}".format(self.author_fname, self.author_lname)


class Review(db.Model):
    # schema for Review model
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey("title.id",
                         ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"#Review - {self.review} | Rating - {self.rating}".format(self.review, self.rating)

