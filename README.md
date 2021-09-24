# Survey App

## Link to the app on Heroku
![Here is the live version on my Survey-App](https://kristina-survey-application.herokuapp.com/)

## Features
The app is based on a corona virus survey questions that I have found online.
It is connected to the google sheets API and let's the user input desired
answer, which updates the google sheet provided [Here](https://docs.google.com/spreadsheets/d/1H56-CzhiVaVck5yGSWQvKi16_GZPmLz0ulLKzqpEEqQ/edit#gid=0).

## Purpose and Functionality
The survey application provides functionality to perform and maintain survey data.
In the background the application is using a spread sheet in Google Drive to read and update the survey data.
When the user launches the application, they are presented with the following options:

![Screen shot of the app](https://github.com/Kristina30/survey-app/blob/main/images/main-image.png)

Option 1 - Complete survey – when this option is selected it gives the opportunity to complete a survey.  The user needs to answer one question at the time. In the background there is validation in place based on the data type of the question. There are few data types used in the application: 

* Text – this is a free text used for questions like Name
* Number – numeric value is expected for questions like Age
* F/M and Y/N data type – this gives the option to the user to enter one of displayed values.

In all scenarios users are not allowed to move to the next question unless they enter an answer with the valid data type. Once they’ve reached the end of the survey, their answers are written to the spreadsheet. 

Option 2 - View all survey result – when this option is selected users are presented with an extract with the data from the entire spreadsheet. The second row is not included as it contains the data types. The data is presented in a table view which makes it easier for the customer to read the data.

Option 3 - View survey result per gender – this selection gives an option to the user to select which gender he would like to see the data for.

![Screen shot of the app](https://github.com/Kristina30/survey-app/blob/main/images/gender-results.png)

When the users select the gender the are presented with a list of data for the specific gender. Again, the data is presented in a table view to make it more user friendly.

Option 4 - View survey results per age group – When this option is selected the user is presented with a sub menu to select which age group, they would like to see the data for.

![Screen shot of the app](https://github.com/Kristina30/survey-app/blob/main/images/age-results.png)

Once the age group is selected then the customer is presented with the data for the specific age group in a nice table view. They also have an option to move back to the main menu.

## Development
For development of this app, I used code institutes mock terminal.
The reason for this is simplicity: the user won't therefore have to download any files, but can instead use
the python program directly though the browser.

The main thing to do was to figure out the way of getting the sheets from google.
This was done installing and importing the gspread module.

## Creating the Heroku app

When I created the app, I needed to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

I then created a _Config Var_ called `PORT`. Set this to `8000`

I have also created another _Config Var_ called `CREDS` and paste the JSON into the value field.

Last step taken was to connect my GitHub repository and deploy as normal.

## Technologies Used
* Github - storing code for the project after being pushed.
* Gitpod - development enviroment for the project.
* PEP8 - Python code passes through a linter with no significant issues.
* Google sheets
* Heroku app

## Testing
* The PEP8 Validator is used to validate the code of my project to ensure there were no syntax errors (PASSED).
* Giving invalid inputs (strings when numbers are expected, same input twice).
* Tested in the code institute Heroku Terminal and my local terminal.

The project was manually tested. There weren't any issues apart from one in Option 2 . If more than 5/6 users save survey results, the lay out of the program changes and becomes unstructured and difficult to read the results. As I am not very advanced in Python and the due date of my submission is near I have decided  to fix this bug in the future.

## Deployment 
This project was deployed using code institute's mock Terminal for Heroku.

Deployment Steps:
* Fork or clone this repository.
* Create new Heroku app.
* Set a built back to `Python` and `nodeJs` (in this exact order).
* Link the Heroku app to the repository.
* Finally click on Deploy.





