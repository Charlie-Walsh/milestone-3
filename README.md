<h1 style="text-align:center">The Sanctum</h1>

The Sanctum is a place for bookworms like myself to read and add reviews for sci-fi and fantasy novels. Anyone looking to find a new series or just a short story can find guidence here or provide a helpful review for someone looking for something new. This will help people make an informed decision when deciding whether or not to purchase a book they may have had their eye on for a while or discover a new author they will really enjoy. In my own personal experience I have mostly chosen what books I read by peer recommendation or word of mouth. This space will allow for that on a grander scale available to anyone and everyone.
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


### Changes

As I've gotten deeper into the creation of this site I have had to make a few changes to my original vision. I intended to have the form for submitting a review all on one page but that has felt clunky and a slog for the user. Instead I have decided to go with a more guided path for submiting data into the database, requiring the user to browse and either add to or create a new entry in the library. As the database grows this will be less of a factor as the number of authors and books increase and reviews can be added to existing entries.

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

 - db.creat_all() is throwing a RunTimeError: Working outside of application context. *Solution* - Installed previous version of flask-sqlalchemy psycopg2.
 
### Test Table

| **Subject**    | **Criteria/Issues**                          | **Test**                                                                  | **Outcome**                                                                                                                                                                                     | **Action Taken**                                                                                                                                                                               |
|----------------|----------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Responsiveness | How responsive is the game screen (HTML/CSS) | Use inspect tools to test responsiveness at each breakpoint listed below. |                                                                                                                                                                                                 |                                                                                                                                                                                                |
|                |                                              | >1200px                                                                   | Preview browser is over 1200px.                                                                                                                                                                 | N/A                                                                                                                                                                                            |
|                |                                              | <1200px                                                                   | Looks great at this width.                                                                                                                                                                      | N/A                                                                                                                                                                                            |
|                |                                              | <992px                                                                    | Materialize is doing the majority of the heavy lifting. No change needed.                                                                                                                       | N/A                                                                                                                                                                                            |
|                |                                              | <768px                                                                    | As above.                                                                                                                                                                                       | N/A                                                                                                                                                                                            |
|                |                                              | <576px                                                                    | Author input fields too small at col s6. Buttons and headings feel off when set to the left.                                                                                                    | Changed to col s12 to give them their own line. Buttons and headings centered.                                                                                                                 |
| Usability      | Are all links working?                       | Click links                                                               | All links point to the appropriate page.                                                                                                                                                        | N/A                                                                                                                                                                                            |
|                | Page performance                             | Use Chrome's lighthouse to assess performance.                            | All scores 90+.                                                                                                                                                                                 | N/A                                                                                                                                                                                            |
| Database       | Database accepting user input (C)            | Fill out form                                                             | author_fname registering as null                                                                                                                                                                | Multiple attempts to fix failed. I was submitting after every entry which was giving the author_fname a null value.                                                                            |
|                |                                              | Fill out form                                                             | autohr_lname registering as null                                                                                                                                                                | Could not find the route of the issue. Decided to break form up into separate sections, which would create less work for users as more entries are added and less chance of duplicate entries. |
|                |                                              | Fill out forms                                                            | New forms work well and accept entries                                                                                                                                                          | N/A                                                                                                                                                                                            |
|                | Able to see user input on relavent page (R)  | Check for entries on relevant pages                                       | Authors, books and reviews are all appearing where they should with the correct information                                                                                                     | N/A                                                                                                                                                                                            |
|                | Able to edit review (U)                      | Click edit link                                                           | Edit link takes the user to the edit page and allows them to edit the entry.                                                                                                                    | N/A                                                                                                                                                                                            |
|                |                                              | Check edited entry                                                        | Edit has stuck and appears as expected.                                                                                                                                                         | N/A                                                                                                                                                                                            |
|                | Able to delete review (D)                    | Delete entry                                                              | Information is deleted and removed from the page as expected.                                                                                                                                   | N/A                                                                                                                                                                                            |
| Code           | HTML Verified                                | Run through W3 validation                                                 | Ran through validation, however validator doesn't recognise Flask functionality. All errors are related to endblocks and Flask syntax for links etc. Also missing <head> info and no <!doctype> | N/A                                                                                                                                                                                            |
|                |                                              |                                                                           | HTML Validated.                                                                                                                                                                                 | N/A                                                                                                                                                                                            |
|                | CSS Verified                                 | Run through W3 validation                                                 | CSS Validated.                                                                                                                                                                                  | N/A                                                                                                                                                                                            |
|                | Python PEP8 compliant                        | Python files put through pythonchecker.com                                | Meets PEP8 standards for Python                                                                                                                                                                 | N/A              
### W3 Validation Example

![Validation Example](/sanctum/static/images/w3-html-validation.png)

### Lighthouse Score

![Lighthouse Score](/sanctum/static/images/lighthouse-score.png)

<hr>

# Deployment

### Deploying the Website

ElephantSQL

You will need a database instance to host your database.

1. Create and sign in to your ElephantSQL account at [ElephantSQL](https://www.elephantsql.com/).
2. Once logged in, click the "Create new instance" button to create a new PostgreSQL database instance.
3. Choose a plan that suits your needs (e.g., Free Tiny Turtle or any other plan).
4. Select a region and a name for your database instance.
5. Click "Create ElephantSQL" to create your database instance.
6. After your database instance is created, you'll receive a connection string. Make a note of this string as you'll need it to connect to your database.

Render

1. Create an account at [Render](https://render.com/). You can sign in with your GitHub account to make things easier.
2. Navigate to the 'Get started in minutes' page and choose 'New Web Service'.
3. Here you want to 'Build and Deploy from a Git Repository'.
4. Copy and paste the address of your repository in the box for 'Public Git Repository' and click continue.
5. Fill out the information in the form. Name your web service, and make sure the start command is correct '$ gunicorn run:app'.
6. Go to the advanced options below and add you DEVELOPMENT variable, set to false, and your DATABASE_URL variable, which will be the connection string from your ElephantSQL instance.
7. Click the Create Web Servicde button.
8. Once built you will see your web service is live and you will be able to access it with the link at the top of the page.


### Forking the Repository
By forking the repository you will create a copy to your own Github account. Here you will be able to view or edit code without changing the original repository.

1. Start by logging in to GitHub and finding my repository.
2. In the top right hand corner of the window you will find the fork button.
3. You should now have your own copy of the repository.

### Cloning the Repository
You can also clone the repository to use locally.

1. Start by logging in to GitHub and finding [my repository](https://github.com/Charlie-Walsh/rock-paper-scissors).
2. To the left of the green Gitpod button is the Code dropdown button.
3. To clone using HTTPS copy the link under HTTPS.
4. Open Git Bash.
5. Make sure you change the working directory to the location you want the cloned directory to go.
6. Type "git clone" and paste the url you copied after it.
7. Press enter and your clone will be created.