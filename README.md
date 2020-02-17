<h1 align='center'>
Data Centric Development - Milestone Project 3 -World of Recipes -Marzena Chodnicka
</h1>

<div align='center'>

[World of Recipes](https://worldofrecipes.herokuapp.com/) is a website where you can get recipes from over the world, 
people who loves cooking can use the website for any ideas, to add their very own collection of recipes or to inspire other users! There is always something good for everyone tast!
<br><br>
[**View World of recipes website here**](https://worldofrecipes.herokuapp.com/),
[**View Website Development in Github here**](https://github.com/MarzDell/worldofrecipes)
</div>

## Contents Table

1. [**UX**](#ux)
    -[**Project Purpose**](#project-purpose)
    -[**Design**](#design)
    -[**Wireframes**](#wireframes)

2. [**Features**](#features)
    -[**Existing Features**](#existing-features)
    -[**Features to implement**](#features-to-implement)

3. [**Technologies Used**](technologies-used)

4. [**Testing**](#testing)

5. [**Deployments**](#deployments)

6.  [**Credits**](#credits)
    -[**Contents**](#contents)
    -[**Images**](#images)
    -[**Help with code**](#help-with-code)
    -[**Acknowledgements**](#acknowledgements)

## UX

### Project Purpose

The main goal of World Of Recipes is to make perfect place for users to get their own recpies in one place and share the love of cooking.

### Design

The design of the page is simple and easy to move around, it is intuitive as well as colours are light which improves user experience.

- #### Fonts
    
    - The font **'Playfair Display'** was used as it is simple and easy to read also it is commonly used on popular websites.

- #### Colours
    
    - **All Pages -** A white background was chosen to keep good looking design.
    - **Buttons -** Colours of the button has been chosen to merge into background picter on landing page and give amazing appearance. 
                    Style of the buttons on other pages were followed the same as on landing page.
    - **Links -** An orange colour was chosen once hovering to match the colour of the button and make conection of styles on the website.
    - **Social Links -** A black colour was chosen as a good contrast between the background, an orange was chosen once hovering to match links and button colours.
    - **Pictures -** All theme of pictures were chosen in the same style to make nice and good connection between pages.
    
- #### Styling

    Style on each page were chosen to match all website, the user changing from one page to another will see more as a flow then just a page.
    I created short and simple way of display that the user will be not overload of content. Style on the website fits to every generation of the user due to having 
    modern layout but well-known to the rest.
    
- #### Website Pictures

    All images have been chosen to match and have been downloaded from Pinteres.
    
### Wireframes

Wireframes were made using [Moqups](https://moqups.com).

- #### Desktop Wireframes
    
    -[Landing Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/desktop/landing-page.png)
    -[Home Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/desktop/home-page.png)
    -[Add Recipe Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/desktop/add-recipe-page.png)
    -[Shop Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/desktop/shop-page.png)
    -[Statistic Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/desktop/statistic-page.png)

- #### Tablet Wireframes
    
    -[Landing Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/tablet/landing-page-tablet.png)
    -[Home Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/tablet/home-page-tablet.png)
    -[Add Recipe Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/tablet/add-recipe-page-tablet.png)
    -[Shop Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/tablet/shop-page-tablet.png)
    -[Statistic Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/tablet/statistic-page-tablet.png)

- #### Mobile Wireframes
    
    -[Landing Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/mobile/landing-page-mobile.png)
    -[Home Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/mobile/home-page-mobile.png)
    -[Add Recipe Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/mobile/add-recipe-page-mobile.png)
    -[Shop Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/mobile/shop-page-mobile.png)
    -[Statistic Page](https://github.com/MarzDell/worldofrecipes/blob/master/UX/skeleton-plane/wireframes/mobile/statistic-page-mobile.png)

## Features

### Existing Features

1. #### Navigation

    We have little amount of navigation on website. On Home Page you can find four links to Home, Add Recipe, Shop and Statistic as well you can find link back to landing page.
    
2. #### Search function

    On Home page you can find search function where the user can type in a keyword  to find category of recipes. It is created to save them some time and make it simple.
    
3. #### Individual Recipe

    It is displayed under search function in card styled container, user can click picture or hyperlink to chose the specific recipe and will be moved automatically to another page where 
    the recipe will be displayd in full details. As well I added view counter which show how many times was seen by users as a individual recipe.
    
4. #### Edit Recipe

    In edit recipe user can update or edit an existing recipe.
    
5. #### Delete Recipe

    Users have option to delete recipe. When they choose this option, before deleting is done a message will pop up asking them 'Are you sure you want to delete this recipe?',
    this can prevent deleting recipe if it was done in error, it gives the user the opportunity to cancel the action.
    
6. #### Add Recipe

    This function allows the user to insert their own recipe which adds the user data to the database when it is submitted, once pressed it is then transferred to the Home Page for all user to see.
    
7. #### Shop Page

    It is created to make users aware that feature option will be available soon.
    
8. #### Statistic

    I have added statistic page for data collection but it is not wired up yet and it is not showing any relevant data from the information that is provided to the database in MongoDB.
    
### Features to Implement

1. #### Sign up/Login account

    In close future I will create a secure username, password login, sign up: registration page so that the user will be protected and data can be collected.
    At the moment everyone can edit or update individual recipe but once secure login will be in use only author of recipe would be able to do so.
    
2. #### Shop Page

    Shop page is already on website but still not in use. At the moment all agreement with the suppliers are on going process.
    The shop will be ready to take very first order once is all singed by suppliers.

3. #### Statistic Page 

    Statistic Page will be in use of real data once Sign up account will be created. The page will collect all the datas from the website and will display variation of diagrams 
    with different option to choose by users. 
    
## Technologies Used

- This project uses HTML, CSS, JavaScript and various different technologies to work as helpers to the languages.
- #### [New Cloud9](https://www.vocareum.com)
    - **Cloud9** is an IDE used to develop the website.
- #### [Bootstrap](https://www.bootstrapcdn.com/)
    - **Bootstrap** is used to create easier & cleaner responsiveness in addition with helping maintain padding and margins.
    - It's also used to include modal features to the website to give it a professional look.
- #### [Google Fonts](https://fonts.google.com/)
    - **Google Fonts** has been used to provide clean and eye-catching fonts to the website.
- #### [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- #### [Font Awesome](https://www.bootstrapcdn.com/fontawesome/)
    - **Font Awesome** has been used to add icons to the website.
- #### [GitHub](https://github.com/)
    - **Github** is used: 
    1. As a remote backup of code used in the project.
    2. As a remote server for another user to see the code used in the project.
    3. For users to view the deployed version of the website. The deployed version can be viewed [here!](https://github.com/MarzDell/worldofrecipes)
- #### [MongoDB](https://www.mongodb.com/)
    - **MongoDB** was used as the NoSqldatabase for the storage of user data(recipe).
- #### [Python3](https://www.python.org/downloads/)
    - **Python3** was used to compile and utilise the logic for the project.
- #### [Flask](https://flask.palletsprojects.com/en/1.0.x/)
    - **Flask** is a Python web framework usedfor developing web apps.
- #### [Heroku](https://www.heroku.com/)
    - **Heroku** This is a cloud platform where the project is deployed to. The website can be viewed [here!](https://worldofrecipes.herokuapp.com/)


## Testing

<h1 align="center">
World of Recipes- Testing
</h1>

## Automated Testing

### Validating Code

Validation services were used to ensure that code was valid code used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code.
- [Code Beautify JavaScript Validator](https://codebeautify.org/jsvalidate) was used to test JavaScript code to ensure it was valid code.

## Manual Testing

A number of manual tests were done to ensure the website is working as it should be and that the user can use without any problems.

### Testing on Desktop

The website was tested in Browsers: Chrome, Safari, FireFox and Internet Explorer. 
The website was tested and used on a Laptop, Macbook & Desktop PC and Iphone and Samsung Galaxy.

### Testing on tablet and mobile devices

The website was tested on iPhone 6, Samsung Galaxy. It's also been run through Chrome Developer tools
in the 'Responsive' setting.

## Testing

I checked that:

 All the links are working correctly and the page does not show any error. I added, edit, update and delete many recipes to check the performance of all of the function and if it is transport to MongoDB.
    
## Deployments

The project is deployed on the Heroku Cloud Platform by using a local Git repository linked to Heroku. A MongoDB database was utilised and set up inside the Heroku platform. 
Credentials of the database connection are inside the requirements.txt file, it uses the os environ method to tell Heroku to look inside its own config variable (MONGODB_URI) 
in order to make sure the production database is kept secret.
A Procfile is required, it is a text file named 'Procfile' placed in the root of the application that lists the process types that are needed in an application.

## Credits

### Contents

- All Content has been thought of and written by the Developer. 


### Images

-Images were downloaded from the webpage [Pinterest](https://www.pinterest.co.uk/).
  

### Help with code

- Ideas on how to start with my project a took from youtuber that I follow: [Traversy Media](https://www.youtube.com/user/TechGuyWeb)
- I use help as well from:
    -Website about tutorial[Python3](https://www.tutorialspoint.com/python3/index.htm)
    -Tutorials about [MongoDB](https://www.guru99.com/mongodb-tutorials.html)

### Acknowledgements

- Spencer Barriball (spence_mentor) - For discussing ideas, providing help with project and any ideas related to the project. 
    As well offering me help outside of mentor sessions if I will need anything or if i have an issue that I cannot solve by myself.
- Slack app that whenever I needed help or tips I could check on app.