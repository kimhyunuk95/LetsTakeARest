import os
import requests
import googlemaps
import time
import json
import ssl
import urllib.request

def get():
    LOCATION_API_KEY = 'AIzaSyDKwnXEssm-ObZx0UO4XpGfZxgytTu6VMw'

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'
    data = {
        'considerIp': True,
    }

    result = requests.post(url, data)
    result = result.json()

    return result['location']['lat'], result['location']['lng']