import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Get the Google Map API key
API_KEY = os.getenv("API_KEY")

# Get the lat and lng of input places
# If places is limited, the geometry can be hard coded
def getGeometry():
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=downtown%20atlanta&inputtype=textquery&fields=geometry&key={API_KEY}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    print(response)
    try:
        geometry = response['candidates'][0]['geometry']['location']
    except:
        pass
    lat = geometry['lat']
    lng = geometry['lng']
    return lat, lng

# Use the Nearby Search Request to find near places
def getNearPlace():
    lat, lng = getGeometry()
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius=1000&type=restaurant&key={API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    places = response['results'][0:5]
    print(places)

getNearPlace()


