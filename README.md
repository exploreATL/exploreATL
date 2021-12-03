# Explore ATL

This is the project repository for GSU CSC 4350 SWE CTW, Section 002.

A Python Flask web server app with React front end, that utilizes the Google Places API to find popular attractions in different places around the Atlanta area.
The app takes user input as to which location in Atlanta they would like to explore and delivers 5 places that can be checked off as they are visited around the location. It takes advantage of a postgreSQL database making reliable and secure login as well as keeping track of user activity. It then uses React to display user interactable checklist of their nearby places.

___
Deployment: https://explore-atl.herokuapp.com/

Deployment Sprint 2: http://explore-atl-live.herokuapp.com/landpage
___
## Team Members:

Michael Roussell

Yijing Zhou

Eshan Bhojane

___
## Set Up:

For setting up this app locally please follow these steps:

First, install both python and node.js with your package manger.
Second, you will have to install these dependencies in this order:

1. Install Python requirements using `pip install -r requirements.txt`, if this fails try using `pip3` instead.

2. Install npm and react use `npm install -g npm` and then `npm install react`.

3. Install Ant Design using `npm install antd --save` and `npm install --save @ant-design/icons`.

Then to create the build for the app run `npm run build`
Finally, you will be able to use `python app.py` to launch the app onto a local host.

## Extra Notes:

NOTE: Linting and formatting was done with black.

NOTE: The Kanban Board is in the Organization not the just Repo.

NOTE: Continous interegation is in the Heroku deployment.


