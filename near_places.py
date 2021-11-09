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

# Get the lat and lng of input places
# If places is limited, the geometry can be hard coded
# Input of function is the name of places
def getGeometry(atl_location):
    atl_location = atl_location.replace(" ", "%20")
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={atl_location}&inputtype=textquery&fields=geometry&key={API_KEY}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    # print(response)
    try:
        geometry = response["candidates"][0]["geometry"]["location"]
    except:
        pass
    lat = geometry["lat"]
    lng = geometry["lng"]
    return lat, lng


# Use the Nearby Search Request to find near places
# Input is the type of nearby locations
def getNearPlace(lat, lng, location_type):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius=1000&type={location_type}&key={API_KEY}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    # Get the frist five elements of return locations
    try:
        if len(response["results"]) > 5:
            places = response["results"][0:5]
        else:
            places = response["results"]
    except:
        pass
    print(places[0])


lat, lng = getGeometry(atl_locations[2])
getNearPlace(lat, lng, location_types[3])

