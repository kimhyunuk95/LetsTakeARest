import streamlit as st
import pandas as pd
import numpy as np
import howlong
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import folium
from streamlit_folium import st_folium


df = pd.read_csv('./deleted_df.csv')


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
try:
    origin_lat, origin_lng = result.get("GET_LOCATION")['lat'], result.get("GET_LOCATION")['lon']
    lat_list = destination_lat.tolist()
    lng_list = destination_lng.tolist()

    ds_list = []
    for i in range(len(lat_list)):
        ds_list.append(howlong.distance(origin_lat, origin_lng, lat_list[i], lng_list[i]))
    df['거리'] = pd.DataFrame(ds_list)

    a = df[['상호지점명','거리','위도','경도']].sort_values(by='거리').head(10).reset_index(drop=True)
    st.write(a)



    b = pd.DataFrame()
    b['lat'] = a['위도']
    b['lon'] = a['경도']

    #folium
    m = folium.Map(location=[origin_lat,origin_lng], zoom_start=16)

    for i in range(0,10):
        folium.Marker(
            [a['위도'][i], a['경도'][i]],
            popup =a['거리'][i],
            tooltip = a['상호지점명'][i]
        ).add_to(m)
    folium.Marker(
        [origin_lat, origin_lng],
        tooltip = '현재위치',
        icon = folium.Icon(
            color = 'red'
        )
    ).add_to(m)
    
    st_data = st_folium(m, width=725)
except AttributeError:
    st.error('Click GetLocation Button')

