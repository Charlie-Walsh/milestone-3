<h1 style="text-align:center">The Sanctum</h1>

The Sanctum is a place for bookworms like myself to read and add reviews for sci-fi and fantasy novels. Anyone looking to find a new series or just a short story can find guidence here or provide a helpful review for someone looking for something new. This will help people make an informed decision when deciding whether or not to purchase a book they may have had their eye on for a while or discover a new author they will really enjoy. In my own personal experience I have mostly chosen what books i read by peer recommendation or word of mouth. This space will allow for that on a grander scale available to anyone and everyone.
<hr>

# User Experience

## User Stories

### Firts Time Visitors

- First time visitors will be able to see exactly what the site is about when they hit the landing page and will be able to easily navigate their way around the site to find what they need.
- I would like the site to have a clean design to help with easy navigation and to be easy to read.

### Returning Visitors

- Returning visitors should be able to quickly find their way to leaving a review of their own or look for something new. Or the next book the series they've started etc.
- They should be able to edit their previous reviews if they have changed their minds on a second read through, add anything they have forgotten or delete the review entirely.

## Design

I have decided to keep the design simple and clean in order to to make it easy for visitors to find their way around. This will also save me time when coding as I won't be putting too much time into the front end development and focusing on the backend.

### Color Palette

- I have chosen to go with a simple dark grey and off white reminiscent of the pages of a book. Buttons will be a soft green as to not be too bold, in keeping with the pages muted colours.

### Typography

- I will be keeping the default font as I think it suits the page and there is no real need to change it.

### Wireframes

Home Page
![Home Page](/sanctum/static/images/home.png)
Books Page
![Books Page](/sanctum/static/images/books.png)
Review Form
![Review Page](/sanctum/static/images/review.png)

### Models

![Models](/sanctum/static/images/models.png)

<hr>


# Code

## Languages

- HTML
- CSS
- JavaScript
- Python

## Libraries/Frameworks

 - Materialize
 - Font Awesome
 - Flask
 - postgresql
 - SQLAlchemy

<hr>

# Testing

## Bugs

 - Pylint bug encountered using flask-sqlAlchemy giving "Instance of 'SQLAlchemy' has no 'Column' member" error. This is a known issue and requires you to crash the plug in to remove it. I didn't want to risk messing with this too much so I am just ignoring it so far. I could put a #noqa comment on every one but that seems a bit redundant for now.

 - My server is not responding for the database locally. The error is something to do with the port 5432 being in use by gitpod. pg_lsclusters command is showing postgres as down. So far I have been unable to test the forms functionality and actually add any data to the database. *Solution* - I'd forgotten to set_pg.

 - After deploying to Heroku app crashes. According to the log it appears to be looking for a favicon.<br>
 'at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=the-sanctum-cw.herokuapp.com request_id=4285cfd9-7a50-4e16-8a67-f039d5b80761 fwd="92.233.104.68" dyno= connect= service= status=503 bytes= protocol=https'

 - db.creat_all() is throwing a RunTimeError: Working outside if application context. *Solution* - Installed previous version of flask-sqlalchemy psycopg2.

 - author-lname returning null value, causing an error due to null constraint. *Solution attempt* - I was commiting the form session to the database prematurely after each entry, causing author-lname to be a null value. Refactored POST code to commit at the end only. After testing, author_fname is now causing a null value. Further debug needed.
 

<hr>

# Deployment

