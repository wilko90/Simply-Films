<h1 align="center"><img src="https://i.ibb.co/Lh8BjJr/5b8494bf96874e198f9d8658965f6a6c.png" alt="logo">

Data Centric Development Milestone Project - Simply Films </h1>




Simply Films is a full-stack MongoDB-based Flask project which is to create a database of films that allows users to create, read, update and delete (CRUD) films. Simply Films allows non registered users to browse our database to search for there favourite films. Users are given the opportunity to create an account and benifit from having access to all features of the website. Registered users can add new films, edit and delete there films.

The project was developed using HTML, CSS, JavaScript, and Python, and uses a NoSQL document-based database via MongoDB

 View Deployed site on Heroku here [Simply Films](https://simply-films.herokuapp.com/films)

 **This website is for educational purposes only**

 # Table of Contents
 1. [UX](#ux)
    * [Strategy](#sratergy-plane)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton-plane)
    * [Surface](#surface-plane)
2. [Features](#features)
3. [Technologies](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

<h1 align="center">UX</h1> <a name="ux"></a>

# Strategy <a name="sratergy-plane"></a>

## Research
### What are the most important aspects of movie reccomandation website?
"I would like to navigate with a user-friendly interface and find a certain film"<br>

"I would like to find a film that has an attractive Image that draws me in" <br>

"I would like to be able to share my own films to the database"<br>


### Similar film databases

[IMDB](https://www.imdb.com/s) <br>

IMDB, in full Internet Movie Database, Web site that provides information about millions of films and television programs as well as their cast and crew. The name is an acronym for Internet Movie Database.

[TMDB](https://www.themoviedb.org/?language=en-GB) <br>
The Movie Database (TMDb) is a community built movie and TV database. Every piece of data has been added by TMDB community dating back to 2008. The Movie Database Transforms uses the TMDB to search and pivot on movies, talent and directors names.

[Letter Boxed](https://letterboxd.com/) <br>
Letterboxd is an online social networking service. Letterboxed was launched as a social app focused on sharing opinions about, and love of film. Members can use it as a diary to record their opinions about films, keep track of films they have seen in the past, write reviews or make lists of films and showcase their favorite films

# Business Approach


### Mission Statment
 Help users to find interesting movies easier. Allow the user to search movies by typing in the key word of the movie, Allow the user to search movies by typing desired genre.
 


### Branding
* Branding defines you as your business
* Identify key values
* Consistency
* Clear focus that knows their target audience


### Content
* Simplify existing sites like IMDB
* Clear from the outset
* User Connection
* Intuative Content
* Interactive features 
 
### Aesthetics
* Deliberate use of colours to influence the user experience on a website.
* Make it easy for visitors to find what they are looking for. Multiple tools for accessing information
* keyword-rich content. Use headings and subheadings
* Consistent throughout so that a visitor navigating from page to page will always know where they are and how to get to the next item of interest.
* Elements to be visually connected and balanced


 ## User stories

* `As a visiting user I want to be able to understand the purpose of the website so I can decide if I want to continue navigating`
 
* `As an involved user I want the surface to be simple with an aesthetically pleasing design`

* `"As an unregistered user, I want to be able to view content on the site without having to register, so I can decide whether to make an account."`

* `As an unregistered user, I want to be able to make an account and log in, so that I can benefit from the features of a registered user.`

* `As a logged in user, I want to be able to add content to the database in a simple manner.`

* `As a logged in user, I want to be able to edit or delete content, so that I have control over the content I have stored on the platform.`

* `As a user I want to search movies by typing in the key word of the movie or specific genre`

* `As a mobile user I want to be able to have the same features as the desktop site so I can connect with films on the go`



## opportunities and problems to be solved from user stories
 
|Opportunities | Importance | Viability / Feasibility
|-----|:------:|:-----:|
|**Purpose Of Webpage Explained** | 5 | 5 |
|**Intuitive Design** | 5 | 5 |
|**Clear Instructions** | 5 | 5 |
|**Easy Point Of Contact** | 5 | 3 |
|**Database Access**| 5 | 5 |
|**CRUD Functionality** | 5 | 5 |


</div>

## Website Requirements
### Project Goal: 
Provide a platform on which users can add films to a database, allowing them to rate and add useful inforamtion to help other users locate desired films.
#### User Needs:
* To be able to navigate the site with ease.
* To be able to create an account and log in.
* To be able to create, edit, and delete a films to the database.
* To be able to for a film by name or genre.
* To be able to manage films that they have added to the database in an intuative way.

#### Project Objectives:
* To create a film database to help users search for current and past films
* To give the user a sesne of involvment with in a community 
* To allow the user to navigate and control the application with ease on all platforms and devices

# Scope <a name="scope"></a>

## Functional Requiremnts 
### Simple, Intuitive, and Engaging Interface

* Allow a user to navigate, and interact with, the site with ease.
* Take a minimalistic approach to layout, content, and structure, whilst always presenting.
* Ensure the layout and design is responsive to all media sizes.
* Sufficient and relevant information.

### User Managment
* Allow a user to create an account, log in, log out of there account.
* Add data to the database
* Allow user to update, edit and delete data
* Allow user to manage films added to database with ease

## Content Requierments
* Content of the webiste is primaraly generated by users within the database
* When creating an accocunt on simply films users will be advised to 'Add Film' to DB
   * Created By: Backend funcitonaltiy searches user database to allow user to create data
   * Film Name: This will be provided by the user which will be at the base of the film cards
   *  Film Synopsis: Provided by the user, a brief description of the film been added.
   *  Film Genre: A selection of inputs provided to the user to make a choice of what genre of film they are adding to the database.
   * Film Year: Provided by the user to add the year the film was made
   * Film Raiting: This will be set by the user out of 10 
   * Film Actors: Provided by the user, three top lead roles of the film been added
   * Film Image: Prvided by user in URL form which can be done by uploading an image to an external image hosting service.


# Structure <a name="structure"></a>

### The website uses Multiple pages with the content being Powered with Python, NoSQL, Javascript, HTML, CSS as the user navigates through the website.


### Header
The header of the page contains the NavBar and the Logo, It is a static element, and is fixed to the top of the page at all times.

### Navigation
On larger viewports, the navigational elements are separated into separate links within the NavBar. On medium viewports and lower, the navigational elements are collapsed into a SideNav, which can be activated with a toggler in the upper-left corner.

### logo
Logo is placed within the Header element to the left, unless on medium viewports where it is centered.

### Home/ Films/ Login / Register / Logout
Users can access these pages regardless of where they are on the webpage.

### Footer
The footer is positioned at the bottom of the page.this is not a sticky element, and when content exceeds the viewport of the device, the footer is pushed out of the viewport. The footer contains the name of the web page and social links to Github,Facebook,Youtube,Instagram.

### Films
A stylistic design of 8 results per page showing the films avalible for the user to read.

### Film Cards
Details descriptive information of specific film that is extracted from the database for users to read.

## Interactive
### Navbar
The navbar contains four pages for an unregistered user and five for registered users. Each page is highlighted when hoverd over. When viewed in medium to smaller devices a burger icon is active and navigation opens from the side.

### Login/Register/Logout
If a user is not logged in, the NavBar/SideNav provides the relevant Log In/Register links. When a user is logged in, the Logout link replaces the Log In/Register links.

### Add Film
Registered users are shows the 'Add Film' tab when logged in, this is a detailed form which prompts the user to add specific details which is then sent to the database and renders to the films tab if successful.

### Edit Film/Delete
Users that have added data to the database are highlighted with a choice to edit the data of that specific film and also have the option to delete

### Tooltips
Interactive Icons when trying to Add data via the form, gives the user hints to enter the correct inputs when uploading data.

### Modals
Used for defensive programming. Activated when user trys to delete data to confirm that is what they are trying to do.




 
# Skeleton Plane <a name="skeleton-plane"></a>

### Wireframes
During the development process, changes have been made. All wireframes are the core skeleton to aid in the planning process and are not the final look of the design. I recommend that the PNGs are downloaded to be viewed in your browser.


 [Homepage](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/only-films-homepage.png)<br>
  [Films](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/only-films-homepage.png)<br>
  [Film Card](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/only-films-filmdetails.png)<br>
 [Login](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/only-films-login.png)<br>
  [Register](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/only-films-register.png)<br> 
  [Add Film](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/only-films-addfilm.png)<br>
  [Mobile 1](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/mobile-home-film-login.png)<br>
   [Mobile 2](https://github.com/wilko90/Simply-Films/blob/master/static/wireframes/mobile-add-detials-register.png)<br>
  
## Database
 SImply films utalises a cloud based platform [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=Cj0KCQjw6NmHBhD2ARIsAI3hrM2hjaQUTv9xllyb3-NF69pKMRPU4st3mjFIaAsCYspGVAxQP06qyYUaAiIiEALw_wcB) for storing user credentials and film data. My project users two collections 'Users' and 'Films'.
 <img src="https://i.ibb.co/FDLzsD8/Screenshot-2021-07-20-at-16-55-19.png"><br>

# Surface Plane <a name="surface-plane"></a>

## Brand Image

<img src="static/img/logo1.png"><br>
The brand image/logo for "Simply Films" had to be simple, easy on the eye and be relevent to the webpage. It is located at the head of the page and when engaged navigates the user back to the home section.



## Colour Schemes
The project's design is to remain consistent throughout, the aim was to implement a livley palette that is eye catching for the user. This was designed with the main font [Roboto](https://fonts.google.com/specimen/Roboto) a smart and professional font.
<img src="https://i.ibb.co/cJBygpL/Screenshot-2021-07-20-at-16-15-47.png">

All colour choices were assessed within the guidelines of [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG20/). Each colour was used with [Contrast Ratio](https://contrast-ratio.com/#%23212121-on-%23F0F3F4) and graded within the guidelines of [W3](https://www.w3.org/TR/WCAG20/) .

## Text colours
#### White/Slate (##fffff4)(#232b2b)
predominantly all text is white on a slate background which I have added a slight oppacity to it for a visual effect, which displays a strong contrast between content.

<img src="https://i.ibb.co/9sFgXsn/Screenshot-2021-07-20-at-17-33-22.png"> <img src="https://i.ibb.co/ZK91pf4/Screenshot-2021-07-20-at-17-52-22.png">

## Typography
### Body
[Roboto](https://fonts.google.com/specimen/Roboto) was my font of choice due to its clean simplistic properties which adds professionlism. 

### Logo
[Bungee](https://fonts.google.com/specimen/Bungee) was used as the logo font which has a fun and friendly feel 
## Images
### Background images 
There are two sets of background images used, one for the login/registration/error pages and another for all remainding pages. Images are sourced from [Adobe Stock](https://stock.adobe.com/uk/)
### Image Placeholder
If a user does not add an image url when adding a film to the database a place holder will take that space. Image was sourced from [Adobe Stock](https://stock.adobe.com/uk/)
### Logo
The logo was made from a free editor called [Free Logo Design](https://editor.freelogodesign.org/)
### Favicon
Favicon was made from a free editor called [Icons8](https://icons8.com/icons/set/favicon)
### Film Imagery
All film images are added via a image hosting service and created by the users.


## Visual Interactions

## Opacity
I use opacity to really help important contant stand out with having background imagery on all pages. It also adds a sense of depth by layering different colours.

* Navbar
* Modals
* Film info
* Film Title
* Register
* Login

<img src="https://i.ibb.co/K6214pY/Screenshot-2021-07-20-at-18-42-47.png">

## navbar
The navbar is the main method of navigating throughout the site and is a key role in aiding in strong UX. When hovered over desired link an opaqe highlight is shown. 

<img src="https://i.ibb.co/gRk70Rk/Screenshot-2021-07-20-at-18-25-39.png">

### Call To Action Buttons
The point of contact needs to be appealing and interactive. for the main C2A points, I went into detail about styling which provides the user with a visual appearance. As C2A points are important in providing a good UX, I kept the consistent feel of freshness. When idal the C2A are white text with a slate background, once intiuated the colours change opposite. 

<img src="https://i.ibb.co/pn9shFW/Screenshot-2021-07-20-at-18-49-33.png">
<img src="https://i.ibb.co/CzQ66bK/Screenshot-2021-07-20-at-18-50-38.png">


# Features <a name="features"></a>

## Existing Features
### Home Page and Trending Films 
The home page contains a button that redirects a user to the "Films" page. It also displays 4 random images from the database using the $sample function of MongoDB.
<img src="https://i.ibb.co/ThPhhD2/Screenshot-2021-07-20-at-18-57-59.png">

### Films Page

The films page displays film cards sorted from the oldest to the most recently added. All film cards are clickable and redirect a user to the individual film page with detailed information. The pagination at the bottom of the page allows to display 8 films per page.

<img src="https://i.ibb.co/crRh8XJ/Screenshot-2021-07-20-at-19-04-26.png">

### Film Information

The film_card page renders when user clicks on the film card. It displays information about the selected film: Name, Synopsis, Genre, Raiting, Year, Actor and film image (or film placeholder if no image was added by user). If the user created the film, there are buttons "Edit" and "Delete", that redirect to the edit and delete film pages.

<img src="https://i.ibb.co/4KxTb1Z/Screenshot-2021-07-20-at-19-11-22.png">

### Register
The register page allows a user to create a new account. The user is asked to fill the fields "username", "password" and "confirm password". When adding a username, the code compares it against existing usernames to ensure that it is unique. A username must be 5-15 characters long containg a captial and a number. The same requirement applies to the password field. The "confirm password" field must match the original password. All passwords are hashed for security purposes. If user's input does not meet requirements, flash messages will inform a user about the error. When the form is submitted successfully, a user is redirected to the home page and informed that account was created. There is also a link to the login page for existing users at the bottom of the form.

 <img src="https://i.ibb.co/tK05NST/Screenshot-2021-07-20-at-19-18-51.png">

### Login
The login page features the form with "username" and "password" fields, allowing registered users to log into their account. If the entered username and hashed password match the ones in the database, a user is redirected to the home page and informed that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input. There is also a link to the register page for new users at the bottom of the form.

<img src="https://i.ibb.co/L0fvj1t/Screenshot-2021-07-20-at-19-22-13.png">

### Log Out
"logout" button by the logged in users ends their session and redirects to the login page.

### Manage Films
Manage Films page allows registered users to view all their Films that they added to the database. Next to the users login name there is a button "Add button" that redirects a user to the "Add films" page. If user has not created any films yet, there's a message that asks a user to create one.

<img src="https://i.ibb.co/yFXFkY6/Screenshot-2021-07-20-at-19-29-10.png">

### Add Film

Registered users can add new Films through the form. There are some validations in place - all the fields except "Image URL" are required. For the "Film Name" and "Film Synopsis" fields, limit of characters is set. If user does not provide a URL to the film image, the film placeholder will be assigned for that film. There is also a Tooltip-instruction saying that a user can upload an image to a free image hosting website.
After the succsessful addition, a user is redirected to the films page.

<img src="https://i.ibb.co/yhgn2rV/Screenshot-2021-07-20-at-19-36-51.png">

### Edit Film
Edit film page allows the logged in user to update information about the film. The "Edit" button will appear by the created user.
As well as that, the defensive design (against brute-forcing) in place allows only created user of the recipe to make changes. The form is pre-populated with the original recipe's details. After clicking "Edit recipe" button, the recipe is updated in the database and a user is prompted with a successful flash image.
There is also a button "Cancel" that simply redirects a user to the home page (in order to avoid to hit "back" button in a browser)
<img src="https://i.ibb.co/105g7TN/Screenshot-2021-07-20-at-19-41-28.png">

### Search
The search film function is based on the Film name or by specific genre, allowing user to search for a desired film. This will filter all films listed by specific genre or if the user was searching for a specific film name. this allows for a more detailed search. If the search does not show any results the user is prompted and a 'back to all films' button is shown.

<img src="https://i.ibb.co/k0TkVPN/Screenshot-2021-07-21-at-07-44-05.png">
<img src="https://i.ibb.co/zVqwVBv/Screenshot-2021-07-21-at-07-44-45.png">


### Delete Film
The delete film function allows only created user of the film to delete it. After a user clicks the "delete" button in the film card page, the modal will be opened. It asks a user to confirm if the film needs to be removed. If so, upon clicking "delete" button the film will be removed from the database as well as from the "films" field of the films created_by in "users" collection. There is also a button "cancel" that closes the modal when it's clicked.

<img src="https://i.ibb.co/HDpZ8HK/Screenshot-2021-07-20-at-19-44-49.png">

### 404 and 500 error pages
404 and 500 pages contain short information about the error and a button "Back Home". As well as that, they display navbar that allows users to come back easily to any page if they got lost.

<img src="https://i.ibb.co/c1SJkkN/Screenshot-2021-07-20-at-20-00-34.png">


## Features To Implement
### Watchlist 
Watchlist feature which allows you to track upcoming movies that you want to watch.

### News
A news section to keep users up to date with upcoming film relelases or for other kinds of related industry news.

### User Settings Page
Due to time constraints I could not implement a settings page. I would add functionality for users to be able to change there username, password or delete an account 


# Technologies Used <a name="technologies-used"></a>

### Development
* [GitPod](https://www.gitpod.io/) / [VS Studio](https://code.visualstudio.com/) - an online IDE for developing this project .
* [Git](https://git-scm.com/) - for version control.
* [GitHub](https://git-scm.com/) - for remotely storing project's code.
* The project was debugged using [Google Chrome Dev](https://developer.chrome.com/docs/devtools/) tools.
* The template I used as a guide made from [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template).

# Python
This project uses Python version 3.8.10 for a back-end high level programming language
#### Packages
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) a web Application Microframework
* [PyMongo](https://api.mongodb.com/python/current/) - for Python to get access to the MongoDB database
* [Werkzeug 2.0.1](https://werkzeug.palletsprojects.com/en/0.16.x/) - to generate and verify password hashing.
* [Jinja 3.0.1](https://jinja.palletsprojects.com) - templating language for Python, to display back-end data in HTML.
### Database
* The project uses [MongoDB](https://www.mongodb.com/), a document-based NoSQL Database, for data storage.
### Hosting
This website is hosted through [Heroku](https://dashboard.heroku.com/).
### Libraries
* [Materialize 1.0.0](https://materializecss.com/) - main responsive modern front-end framework used for grid and responsivesness.
* [Google Fonts](https://fonts.google.com/) - To import fonts.
* [FontAwesome](https://fontawesome.com/) - Icons used across the project. 
* [JQuery 3.6.0](https://jquery.com/) - to simplify DOM manipulation and to initialize Materialize functions.
### Other Languages Used
* [HTML](https://en.wikipedia.org/wiki/HTML) was used as the standard mockup language to build my project.
* [CSS](https://en.wikipedia.org/wiki/CSS) was used to style my website and implement my ideas from the surface plane.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)was used to implement interactive features.

### Design

* [ImgBB](https://imgbb.com/) - to host images used in README
* [Techsini](https://techsini.com/multi-mockup/index.php) A tool I used to show that my design is responsive.
*  My projects [Favicon-generator](https://www.favicon-generator.org/) to convert the Favicon to the appropriate format.
* The wireframes were made with a programme called [balsamiq](https://balsamiq.com/).
* CSS code beautified with [minifycocde](http://minifycode.com/css-beautifier/).
* HTML code formatted using [Github](https://www.gitpod.io/docs/tips-and-tricks/#format-document) formating tool 

### Validators
* My projects colour ratio was tested with [webaim](https://webaim.org/resources/contrastchecker/).
* My projects logo and typography was graded with [W3](https://www.w3.org/TR/WCAG/#contrast-minimum) guidelines.
* The project’s HTML was validated using [W3C](https://validator.w3.org/) HTML Markup Validator.
* The project’s CSS was validated using W3C [Jigsaw](https://jigsaw.w3.org/css-validator/) CSS Validator.
* The project’s JS was validated using [JSHint](https://jshint.com/).



# Testing <a name="testing"></a>
<img src="https://i.ibb.co/0pNwW1c/Screenshot-2021-07-21-at-10-29-13.png">

For full testing section [click here](TESTING.md) 


# Deployment <a name="deployment"></a>

## How my project was deployed
This project was deployed to Heroku via the following steps:

* Navigate to Heroku.
* Log in or Sign Up for an account.
* If Creating an account, select Python as the Primary development language.
* Activate the account via the confirmation email.
* Accept the Terms of Service.
* Click on Create new app.
* Enter a suitable App Name and Region.
* Click Create App.
* Under the Deploy tab, under the heading Deployment Method, click the GitHub icon, and proceed * to click the button which states Connect to GitHub.
* Enter your credentials for GitHub.
* Search for the repository required, and click Connect.

## Automatic Deployment

This project was set up to automatically re-deploy with any changes made to the Master Branch. The following steps were taken to enable this.

* Navigate to the Automatic deploys section within the Deploy tab.
* Select the branch you would like to link to automatic deployment.
  * the master branch was chosen for automatic deployment.
* Click Enable Automatic Deploys.

## Environment Variables

The following environment variables must be set within your Heroku Server for the site to deploy and function correctly. Navigate to the **Settings** tab, and under the heading **Config Vars**, select **Reveal Config Vars,** and add the following variables:

*  **IP** : 0.0.0.0
* **PORT** : 5000
* **MONGO_URI**
  * This variable can be obtained from **MongoDB** through the following steps:
  * Log in to [MongoDB](https://www.mongodb.com/).
  * Under **Data Storage** click on **Clusters**.
  * For the Cluster that you would like to connect to, click the **Connect** button.
  *  Click on **Connect your Application.**
  *  Select **Python**, and Version **3.6 or Later.**
  * Copy the connection string, replacing `<password>` with your MongoDB password, and `myFirstDatabase` with the name of the **MongoDB Collection** (Database) you would like to connect to.
* **MONGO_DBNAME**
  * The name of the Database you are connecting to (in the above example, the default would be `myFirstDatabase`.
* **SECRET_KEY**
  * A random sequence of characters, required for maintaining session security in Flask. One method of obtaining a Secret Key is through [RandomKeygen](https://randomkeygen.com/).
* Press Save

## Running this project from your Browser/Locally

 The `Master` branch is in production mode, which means debugging is disabled in the `app.py`.

### Environment Variables

* When running this project locally, the **Environment Variables** must be set in order for it to function as intended.
*  Once you have completed any of the upcoming steps to run/deploy the project in your browser or locally, please create a new python file in your root directory called `envy.py`.
*  Within this file, declare the environment variables described above, in the following format, replacing the `<variable>` with the required variables:

```python
import os

os.environ.setdefault("IP", "<variable>")
os.environ.setdefault("PORT", "<variable>")
os.environ.setdefault("SECRET_KEY", "<variable>")
os.environ.setdefault("MONGO_URI", "<variable>")
os.environ.setdefault("MONGO_DBNAME", "<variable>")
```

The project will automatically locate this file, and read the required environment variables as and when necessary.

### Running this project in your Browser

1. Install [Google Chrome](https://www.google.co.uk/chrome/)
2. Install [GitPod](https://www.gitpod.io/docs/browser-extension/) Browser Extensions for your chosen browser.
3. Create a [GitHub](https://github.com/join) account.
4. Log in to [Gitpod](https://gitpod.io/login/) using your GitHub account.
5. Visit **Simply Films** [GitHub Repository](https://github.com/wilko90/Simply-Films).
6. To run the `Master` branch, ensure the `Master` branch is selected next to the **branches** and **tags** subheadings.
7. Open the repository in Gitpod:
8. Click the green "Gitpod" icon at the top of the Repository
9. A new workspace will open with the current state of the `master` branch. Any changes made to the requested branch after this point will not be automatically updated in your Gitpod Workspace.
10. Create the env.py file in your root directory and declare the environment variables.
11. Type `pip install requirements.txt` into the GitPod terminal to install all the required Python packages.
12. To host the project from Gitpod, type `python app.py` in the terminal.

### Running this project locally

#### Cloning the Repository

1. Visit **Simply Films** [GitHub Repository](https://github.com/wilko90/Simply-Films).
2. Click the "Code" dropdown box above the repository’s file explorer.
3. Under the "Clone" heading, click the "HTTPS" sub-heading.
4. Click the clipboard icon, or manually copy the text presented: `https://github.com/wilko90/Simply-Films.git`
5. Open your preferred IDE (VSCode, Atom, PyCharm, etc).
6. Ensure your IDE has support for Git, or has the relevant Git extension.
7. Open the terminal, and create a directory where you would like the Repository to be stored.
8. Type git clone and paste the previously copied text (`https://github.com/wilko90/Simply-Films.git`) and press enter.
9. The Repository will then be cloned to your selected directory.

#### Manually Downloading the Repository

1. Visit **Simply Films** [GitHub Repository](https://github.com/wilko90/Simply-Films).
2. Click the "Code" dropdown box above the repository’s file explorer.
3. Click the "Download ZIP" option; this will download a copy of the selected branch’s repository as a zip file.
4. Locate the ZIP file downloaded to your computer, and extract the ZIP to a designated folder which you would like the repository to be stored.

#### Opening the Repository

1. Open your preferred IDE (VSCode, Atom, PyCharm, etc).
2. Navigate to the chosen directory where the Repository was Cloned/Extracted.
3. Type `pip install requirements.txt` to install all the required packages.
4. Type `python app.py` in the terminal, whilst in the project’s root directory.
5. You will now be hosting the repository from your IDE.


# Credits <a name="credits"></a>

## Written Content
* I started out by adding content my self under my username, all information on films are taken from [IMDB](https://www.imdb.com/)
* All other content will be added by the users
* All other content is written by me 


 
## Images
* Content images come from the users and can be sourced from mulitple places. For the boiler plate content I created a user and added content myself, Images for the film placholders came from [IMDB](https://www.imdb.com/)
* Background images are sourced from [Adobe Stock](https://stock.adobe.com/uk/)
* Image PlaceholderImage was sourced from [Adobe Stock](https://stock.adobe.com/uk/)
* logo was made from a free editor called [Free Logo Design](https://editor.freelogodesign.org/)
* Favicon was made from a free editor called [Icons8](https://icons8.com/icons/set/favicon)
* Film images are added via a image hosting service and created by the users.

## Code

1. The CRUD instructional videos from the code institute lessons were extremely helpful as I used a lot of refrenceing from there.
2. Pagination Idea came from a project that I found on github and edited by my self [Link](https://github.com/ShaneMuir/Cookbook-Recipe-Manager/blob/master/main.py) 
3. Confirming passwords on registration page [pallet projects](https://flask.palletsprojects.com/en/2.0.x/patterns/wtforms/)
4. Error pages [pallet projects](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)


# Acknowledgements <a name="acknowledgements"></a>

* The Inspiration for this project came from a movie database website called IMDB

* Thank you to the slack community for guiding me in the right direction.

* Thank you to my girlfriend for supporting me throughout my projects. 

* Thank you to the tutors at Code Institute.
 

