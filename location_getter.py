import os
import requests
import googlemaps
import time
import json
import ssl
import urllib.request
import streamlit as st

def get():
    LOCATION_API_KEY = 'AIzaSyAF4T_1XzBl48PyXYjsCwGYvTtdvp59aUc'

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'
    data = {
        'considerIp': True,
    }

    result = requests.post(url, data)
    result = result.json()
    
    st.write(result)

    return result['location']['lat'], result['location']['lng']
