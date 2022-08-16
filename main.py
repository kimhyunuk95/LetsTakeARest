import streamlit as st
import pandas as pd
import numpy as np
import howlong
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

df = pd.read_csv('./seoul_info2.csv')

origint_lat,origin_lng = 37.5666805, 126.9784147

loc_button = Button(label="Get Location")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

destination_lat = df['위도']
destination_lng = df['경도']
origin_lat, origin_lng = result.get("GET_LOCATION")['lat'], result.get("GET_LOCATION")['lon']
lat_list = destination_lat.tolist()
lng_list = destination_lng.tolist()
    
ds_list = []
for i in range(len(lat_list)):
    ds_list.append(howlong.distance(origin_lat, origin_lng, lat_list[i], lng_list[i]))
df['거리'] = pd.DataFrame(ds_list)
a = df[['상호지점명','거리']].sort_values(by='거리').head(5).to_string(index=False)
    

st.write(a)
