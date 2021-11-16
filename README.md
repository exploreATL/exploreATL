# Explore ATL

This is the project repository for CSC 4350 SWE CTW.

A Python Flask web server app with React front end, that utilizes the Google Places API to find popular attractions in different places around the Atlanta area.
The app takes user input as to which location in Atlanta they would like to explore and delivers 5 places that can be checked off as they are visited around the location. It takes advantage of a postgreSQL database making reliable and secure login as well as keeping track of user activity. It then uses React to displace user interactable checklist of their nearby places.

Deployment: https://explore-atl.herokuapp.com/

## Team Members:

Michael Roussell

Yijing Zhou

Eshan Bhojane

...

# Sep Up:

For setting up this app locally please follow these steps:

Install Python requirements using `pip install -r requirements.txt`, if this fails try using `pip3` instead.

Install npm and react use `npm install -g npm` and then `npm install react`.

Install Ant Design using `npm install antd --save` and `npm install --save @ant-design/icons`.

Then to create the build for the app run `npm run build`
