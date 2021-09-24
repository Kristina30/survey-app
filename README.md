# Survey App

## Link to the app on Heroku
![Survey-App](https://kristina-survey-application.herokuapp.com/)

## Features
The app is based on a corona virus survey questions that I have found online.
It is connected to the google sheets API and let's the user input desired
answer, which updates the google sheet provided [Here](https://docs.google.com/spreadsheets/d/1H56-CzhiVaVck5yGSWQvKi16_GZPmLz0ulLKzqpEEqQ/edit#gid=0).

## Purpose

The survey application provides functionality to perform and maintain survey data.
In the background the application is using a spread sheet in Google Drive to read and update the survey data.
When the customer launches the application, they are presented with the following options:






## Creating the Heroku app

When I created the app, I needed to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

I then created a _Config Var_ called `PORT`. Set this to `8000`

I have also created another _Config Var_ called `CREDS` and paste the JSON into the value field.

Last step taken was to connect my GitHub repository and deploy as normal.
