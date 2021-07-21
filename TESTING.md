
<h1 align="center">Data Centric Development Milestone Project - Simply Scrans</h1>

For full readme [click here](README.md)

# Table of Contents

1. [User Story Testing](#user-story)
2. [Features Testing ](#manual-testing)
3. [Further Testing](#further-testing)
4. [Browser Testing](#browser-testing)
5. [Validation Testing](#validation-testing)
6. [Bugs](#bugs)



# User Story Testing <a name="user-story"></a>

# As a visiting user I want to be able to understand the purpose of the website so I can decide if I want to continue navigating

### Benchmark - A user must be able to understand the main purpose of the website's goals.

* On initial contact the user is welcomed by the logo that remains in its container and is visible to the user at all times.
* On initial contact the user is greeted with an H1 introduction and a call to action 'Browse our Films'
* On initial contact the user is greeted with a list of engageable features which will navigate the user throughout the page

#### Outcome - Successful 
<img src="https://i.ibb.co/x6q72Kd/Screenshot-2021-07-21-at-11-09-20.png">

# As an involved user I want the surface to be simple with an aesthetically pleasing design

### Benchmark - The website should be intuitive and be consistent with colour throughout

* On initial contact, the user is greeted with a heading that summarizes the website's purpose
* Consistency in colours throughout chosen by initial colour palette.
* All interactive features match with aesthetics and are descriptive of purpose
* Surface is simple and easy to navigate

#### Outcome - Successful 

<img src="https://i.ibb.co/Hp8NWGC/Screenshot-2021-07-21-at-11-14-43.png">

# As an unregistered user, I want to be able to view content on the site without having to register, so I can decide whether to make an account."

### Benchmark - An unregistered user must be able to see all content posted by other logged-in users without making an account.

* Unregistered users have viewing access to all features across the website.
* Unregistered users can view film cards that contain all the information of the specific film
* An unregistered user is capable of viewing all user-contributed content on the site, without having to register or log in.

#### Outcome - Successful 

<img src="https://i.ibb.co/fX7ppYh/Screenshot-2021-07-21-at-11-23-46.png">

# As an unregistered user, I want to be able to make an account and log in, so that I can benefit from the features of a registered user.

### Benchmark Criteria: An unregistered user must be able to make an account, log in to their account, sign out of their account.

* The Register, Login, and Logout functionalities are visible, where applicable, from all pages, within the NavBar/SideNav.

* Interacting with the Register or Login feature presents the user with a form that has step by step instructions for successfully adding data

* The Register Modal requests a username, a password, and a confirmation password for registration.
  * Feedback is presented to the user when changing fields within the form, in the form of both colour and text. Validation of any given input field is unsuccessful, the appropriate field is highlighted red, and instructional text is presented at the top of the form. communicating which field needs attention.
  * Users cannot submit the form without all forms being validated.
  * If the username requested already exists, the user is informed via a Toast at the top of the page.
  * If registration is successful, the user is automatically logged into their account and is redirected to the homepage.
  * Each registration and login page has small paragraph text that links the user to the correct page if a user already has an account or need to still make one.
* The login page is similar to the Register modal, but without the password confirmation field
 * If login is unsuccessful, a user is returned to the page they were previously on and is presented with information at the top of the page that the username or password was incorrect.
 * If login is successful, a welcome message appears at the top, and the user is redirected to the home page.
 * When logged in, a user can click the Log Out button, and the user is logged out and redirected to the login page.

#### Outcome - Successful 

# As a logged-in user, I want to be able to add content to the database in a simple manner

### Benchmark Criteria: As a logged in user I want to be able to add films of my choice and fill out the relevant information of that film. 

* When a user is logged in they are they have access to extra features on the navbar
* A logged in user can select `Add Film` which is where they are then presented with a form
 * Simple step by step guides are presented with filling the form out correctly with tooltips on each input 
 * validation is in place and each field will highlight green for a successful input or red for a successful input
 * Not all fields are required and have backup content in place if a field is not added
 * once a user has added all relevant data they select `Add Film` which they are presented with a flash message then redirected to the films page.

#### Outcome - Successful

<img src="https://i.ibb.co/qmFfzVT/Screenshot-2021-07-21-at-11-49-55.png">

# As a logged-in user, I want to be able to edit or delete content, so that I have control over the content I have stored on the platform.

### Benchmark Criteria: Logged in Users must be shown the required buttons to be able to update and delete their film additions.

* If I am the created use of a selected film, I can see the buttons "Edit" and "Delete" on the film_card page.
* If I am not the created use of a selected film, the "Edit" and "Delete" buttons are not shown
* When I select edit, the previous information is still shown 
   * After changing the required fields I can select `Edit` which will then show a successful flash image at the top of the page 
   * If a user does not want to change any fields they can press `Cancel` which transports them back to the `Films` page and no changes will be made 
* A created user has the option to delete their data
  * when selected delete a modal is activated asking them if "they are you sure to remove"
  * If a user selects `Delete` the data will be removed from the films page and database

#### Outcome - Successful

<img src="https://i.ibb.co/JcVKcnV/Screenshot-2021-07-21-at-12-12-39.png">
<img src="https://i.ibb.co/Y01zSjX/Screenshot-2021-07-20-at-19-44-49.png">

# As a user I want to search movies by typing in the keyword of the movie or specific genre

### Benchmark Criteria: A user can successfully get filtered results by tying the film name or genre

* At the head of the films page there is a search bar that has an input field with a placeholder hinting to the user what to input
* When user inputs desired film name or genre, there are shown the filtered results
* If the search is unsuccessful the user is shown a message and a `Back to Films` button which redirects them to the film page. 

#### Outcome - Successful

<img src="https://i.ibb.co/Hnndvfy/Screenshot-2021-07-21-at-12-21-01.png">
<img src="https://i.ibb.co/KF9bsXg/Screenshot-2021-07-21-at-12-20-07.png">

# As a mobile user I want to be able to have the same features as the desktop site so I can connect with films on the go

### Benchmark - A user should be able to use all the features in any chosen viewport

* This website uses materialize functionality to be able to allow native compatibility in any viewport
* The NavBar collapses into a SideNav on medium viewports and down, preventing the NavBar from being overcrowded, with the burger icon being distinguishable and easy to interact with.
* All interactive icons work with touch screen devices and are large enough to target using touch.
* All text is legible on all screen sizes.

#### Outcome - Successful

# Manual Testing <a name="manual-testing"></a>

Features below are manual testing and described below

## Registration
* Ensure that when a user is not logged in, they can access the Register link within the NavBar/SideNav from any location on the site.
* Ensure that when a user interacts with the Register link in the NavBar/SideNav, the registration page appears
* Ensure that the form presented shows the fields username, password, confirm password
* Ensure that the following validation occurs
  * Username
     * Alert box pops up when fields are not entered correctly and hints to correct validation
     * Ensure form can not be submitted if the username does not contain letters numbers and one case sensitive.
  * Password
      * Requirements: Required/Between 8 characters, with upper and lowercase letters
      * If a user does not provide a password, a required message will prompt the user
      * If the field is in an invalid state, and the user provides a valid password, they attempt to submit the form, the field reverts to its valid state.
  * Password Confirmation
    * Required/Must match Password
    * if a user provides a valid confirmation password that matches, flash message registration is successful
    * If a user does not provide a confirmation password, a required message prompts the user to provide a confirmation password
    * If the users' password does no match, a user is prompted with a "passwords do not match" flash message
* Ensure that when a user successfully registers, they are presented with a welcome message, and are automatically logged into their account and sent to the home page.
* If a user has attempted to register an account with a username that already exists in the database, registration is unsuccessful, and the user is informed via a flash message that the username already exists.
* If a user already has an account and needs to go to the login screen the link takes them there successfully
## Login
* Ensure that when a user is not logged in, they can access the login link within the NavBar/SideNav from any location on the site.
*  Ensure that when a user interacts with the login link in the NavBar/SideNav, the login page appears
* Ensure that the following validation occurs appropriately
   * Username
      * Alert box pops up when fields are empty
      * If users enter incorrect details they are shown an Unsuccessful flash message
      * If a user still has not created an account, the button is active and sends a user to a registration page 
      * If a user matches the database with the correct username and password, a flash message is shown welcoming them with their name and is sent to the home page.
* ## User Logout
* Ensure that when a user is logged in, they can access the LogOut link within the NavBar/SideNav from any location on the site.
* Ensure that when a user selects the Log Out link, they are logged out of the website.
* Ensure when a user logs out they are prompted with a message and returned to the login screen


## Nav Bar
* On initial load ensure the navigation bar loads the full width of the screen with correct links and logo.
* Ensure all links are active and not broken and send a user to the correct location
* Ensure the navbar is sticky and is constantly at the head of a page
* Ensure the logo is active and redirects the user to the home page

## Home Page
* Ensure background image renders correctly
* Ensure the C2A button is working correctly and directs the user to the films section
* Ensure Four random film cards are generated when the page is loaded
    * Ensure each film card is interactive and when initiated sends the user to the films information
* Ensure footer is at the base of the page at all times
* Ensure all social links are active, open in a new tab when initiated and send a user to the correct location 

## Films
* On initial load ensure search bar, 8 film cards render with pagination active at the base
* Ensure the search bar is active and filters correct results
    * Ensure if no results are found the user is presented with a Call to Action and sends user back to the films page
* Films cards
  * Ensure each film card is active.
  *  Ensure all film cards show the title of the film and genre.
  * Ensure when initiated it sends the user to the correct film card.
  * Ensure the user is greeted with the title of the film, film image, film synopsis, film genre, film rating, film year, film actors and user-created by.
  Ensure if created by the user that edit & delete buttons are shown.
  Ensure if not created by the user that edit & delete buttons are not shown.
  Ensure the back button is active and returns the user to the films page. 
* Pagination
  * Ensure pagination is active with the correct amount of pages.
  * Ensure When the next page is selected 8 more results are shown or the remaining data.

## Add Film
* Ensure only logged in users can access the `Add Film` Page.
* On initial load make sure Input form has rendered.
* Form 
    * Movie Title
        * Ensure placeholder text is showing.
        * Ensure tooltip show relevant hints.
        * Ensure the red asterisk icon is showing.
        * Ensure Validation Box turns red if no input has been made.
        * Ensure only 1-20 characters can be inserted.
        * Ensure validation box turns green if correct input has been made.
        * Ensure form can not be submitted without correct validation. 
    * Film Synopsis
        * Ensure placeholder text is showing.
        * Ensure Tooltip show relevant hints.
        * Ensure the red asterisk icon is showing.
        * Ensure validation box turns red if no input has been made.
        * Ensure only 5-200 characters can be inserted.
        * Ensure validation box turns green if correct input has been made. 
        * Ensure form can not be submitted without correct validation.
    * Film Genre
        * Ensure placeholder text is showing.
        * Ensure Tooltip show relevant hints.
        * Ensure the red asterisk icon is showing.
        * Ensure dropbox shows with correct fields.
        * Ensure validation box turns green if correct input has been made.
        * Ensure form can not be submitted without correct validation. 
    * Film Year
        * Ensure placeholder text is showing.
        * Ensure Tooltip show relevant hints.
        * Ensure the red asterisk icon is showing.
        * Ensure Validation Box turns red if no input has been made.
        * Ensure only 4 numbers can be inserted.
        * Ensure validation box turns green if correct input has been made.
        * Ensure form can not be submitted without correct validation.
    * Film Rating
        * Ensure placeholder text is showing.
        * Ensure Tooltip show relevant hints.
        * Ensure the red asterisk icon is showing.
        * Ensure Validation Box turns red if no input has been made.
        * Ensure only 1-2 numbers can be inserted.
        * Ensure validation box turns green if correct input has been made.
        * Ensure form can not be submitted without correct validation.
    * Lead Characters
        * Ensure placeholder text is showing.
        * Ensure Tooltip show relevant hints.
        * Ensure the red asterisk icon is showing.
        * Ensure Validation Box turns red if no input has been made.
        * Ensure validation box turns green if correct input has been made.
        * Ensure form can not be submitted without correct validation.
    * Film Image
        * Ensure placeholder text is showing.
        * Ensure Tooltip show relevant hints.
        * Ensure the red asterisk icon is not showing.
        * Ensure there is no Validation Box if no input has been made.
        * Ensure form can be submitted without correct validation.
    * Ensure When all fields have been successfully entered that the user is prompted. with a successful flash message and is returned to the films page.
    * Ensure The cloud database (Mongo DB) has been updated.
## Edit Film
* Ensure only the created users have access to the edit film function. 
* Ensure the button is only visible on the film card
* Ensure Page renders with form and inputs are still loaded with correct data.
* Ensure the validation process is still the same as when adding a film.
* Ensure no film can be updated without all fields been filled out.
* Ensure when changes have been made successful the user can select the `Edit Film` button.
* Ensure on successful completion the user is presented with a flash message and returned to the films page 
* Ensure if the user selects Cancel, no changes are made and the user is returned to the films page.
*  Ensure The cloud database (Mongo DB) has been updated.

## Delete Film
* Ensure only the created users have access to the edit film function.
* Ensure the button is only visible on the film card.
* Ensure when selected a modal is activated.
* Ensure the modal gives the user option to delete or go back.
* Ensure back closes the modal and no changes have been made.
* Ensure when the user selects delete that the film is removed. 
* Ensure the film is removed from the cloud database.

## Manage Films
* Ensure only logged in users can view this page
* Ensure when page selected, manage films renders 
* Ensure if you have not yet created any films that a message states you have not and shows a C2A to add a film
    * Ensure the C2A sends the user to the `Add Film` Page
* Ensure if the user has already created films, only films that he has created are showing
* Ensure all films created are active and send the user to the correct film card
* Ensure the user is present with a C2A that sends them to the `Add Film` page 


# Further Testing <a name="further-testing"></a>
## Responsive Design

All testing above was again tested on multiple devices through chrome developer tools with their `toggle device tool bar`

Devices used for testing:
* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2XL
* iPhone 5/SE
* iPhone 6/7/8 (plus)
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold

All features are tested from viewports of 280px and above.


# Browser Testing <a name="browser-testing"></a>

 All browser testing was done with the same method above

 Problems usually occurred when my CSS was not compatible with most browsers. Running my CSS code through an Auto-Prefixer solved these compatibility issues.

## Chrome/Mircrosoft Edge

* All testing successful

## Mozilla Firefox

* All testing successful

## Safari

* All testing successful

## Internet Explorer

* My project uses ES6 which has compatibility issues with Internet Explorer. No further testing was made.

# Validation Testing <a name="validation-testing"></a>

 Validation testing was done with third party applications below:

## [W3 Vailidator](https://validator.w3.org/)

* HTML successfully passes W3 Validator

## [Jigsaw Validator ](https://jigsaw.w3.org/css-validator/)
* CSS successfully passes the W3 Jigsaw Validator
<img src="https://i.ibb.co/cCw8VpC/Screenshot-2021-07-21-at-14-49-59.png">
## [JSHint](https://jshint.com/)

* JS Hint was used to flag any errors or mistakes in the javascript code and was used consistently throughout the development process.
* No errors are present 
* Two warnings present are due to " 'let' is available in ES6 (use 'version: 6') or Mozilla JS extensions (use Moz)"
## [Python](http://pep8online.com/)
* The project's Python was validated for PEP8 compliance using Pep8,
* These warnings have been considered, however, they appear to be incorrectly reporting `env.py` as being unused, due to how `env.py` works. Once deployed, this will not be imported anyway, and therefore this has been added to the ignore file.

## [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)

#### The project's Accessibility, Performance, and Best Practices audit were undertaken with Google Lighthouse. Webpages graded are below:

## Home Page
<img src="https://i.ibb.co/8NbzD72/Screenshot-2021-07-21-at-16-47-03.png">

## Films
<img src="https://i.ibb.co/G2LZC4D/Screenshot-2021-07-21-at-16-53-11.png">

## Add Film
<img src="https://i.ibb.co/FmtLhhv/Screenshot-2021-07-21-at-16-53-56.png">

## Film Card
<img src="https://i.ibb.co/nwRQzfN/Screenshot-2021-07-21-at-16-54-49.png">

It appears that I have been down scored due to the sheer size of the external images been used. All Images come from users and maybe various sizes. Images can be reduced in size but this will affect visual quality. 

# Bugs <a name="bugs"></a>

### Input areas highlight whiter when predicted text is used
* Unable to locate a specific class to target background to remove the highlight.

Solution: unresolved

### Pagination on Manage Films page
* After printing each section to the terminal of my manage film function, I can't get the pagination to show on the manage films page. Reaching out to the tutor support team they were also unable to help. due to submission time, I could not follow up with them.  

Solution unresolved

### Targeting the object ID

* I had a BSON error issue trying to target the ObjectId. I resolved this issue by removing the `insert_one` for the `find_one` method.

Solution: resolved

For full readme [click here](README.md)


