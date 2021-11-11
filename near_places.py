"""
Project 2
Explore ATL
GSU CSC 4350 Software Engineering
Fall 2021

This is the 'near_places.py' python file for the Project 2.
This file handler the Google Places API calls needed for the app.

Python3.9 was used for this assignment.
Please run with the Linux or macOS 3.9 version of the python interpreter.

If there are any questions, please contact us at 'exploreatl.devs@gmail.com'.
MIT Eduation License Preferred
"""
import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Get the Google Map API key
API_KEY = os.getenv("API_KEY")

atl_locations = [
    "downtown atlanta",
    "buckhead atlanta",
    "sandy springs",
    "johns creek",
    "norcross atlanta",
]
location_types = [
    "restaurant",
    "museum",
    "park",
    "university",
    "store",
    "city_hall",
    "amusement_park",
    "library",
]

class NearPlaces:
    def getGeometry(atl_location):
        '''
        Get the lat and lng of input places

        Parameters:
        atl_location(string): the name of a place

        Returns:
        lat, lng
        '''
        # Get the Google Map API key
        API_KEY = os.getenv("API_KEY")
        
        atl_location = atl_location.replace(" ", "%20")
        url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={atl_location}&inputtype=textquery&fields=geometry&key={API_KEY}"

        response = requests.get(url).json()
        try:
            geometry = response["candidates"][0]["geometry"]["location"]
        except:
            pass
        lat = geometry["lat"]
        lng = geometry["lng"]
        return lat, lng


    def getNearPlace(location, location_type):
        '''
        Use the Nearby Search Request to find near places

        Parameters:
        location(string): the name of a place
        location_type(string): the type of nearby locations

        Returns:
        List nearby_places with 5 elements, each element is a nearby place with fields
        of geometry location(lat, lng), name, and photo reference
        '''
        # Get the Google Map API key
        API_KEY = os.getenv("API_KEY")

        lat, lng = NearPlaces.getGeometry(location)

        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius=1000&type={location_type}&key={API_KEY}"

        response = requests.get(url).json()
        # Get the frist five elements of return locations
        try:
            if len(response["results"]) > 5:
                places = response["results"][0:5]
            else:
                places = response["results"]
        except:
            pass
        nearby_places = []
        for place in places:
            nearby_place = {}
            nearby_place["location"] = place["geometry"]["location"]
            nearby_place["name"] = place["name"]
            nearby_place["photo_reference"] = place["photos"][0]["photo_reference"]
            nearby_places.append(nearby_place)
        return nearby_places


nearby_places = NearPlaces.getNearPlace(atl_locations[0], location_types[0])
for place in nearby_places:
    print(place)
