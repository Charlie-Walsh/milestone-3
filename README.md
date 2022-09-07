<h1 style="text-align:center">The Sanctum</h1>

The Sanctum is a place for bookworms like myself to read and add reviews for sci-fi and fantasy novels. Anyone looking to find a new series or just a short story can find guidence here or provide a helpful review for someone looking for something new. This will help people make an informed decision when deciding whether or not to purchase a book they may have had their eye on for a while or discover a new author they will really enjoy. In my own personal experience I have mostly chosen what books i read by peer recommendation or word of mouth. This space will allow for that on a scale available to anyone and everyone.
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

 - My server is not responding for the database locally. The error is something to do with the port 5432 being in use by gitpod. pg_lsclusters command is showing postgres as down.

<hr>

# Deployment

