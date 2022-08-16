import pandas as pd
import howlong
import location_getter
import streamlit as st

df = pd.read_csv('./seoul_info2.csv')
if df.empty:
    st.write('없음')
else :
    st.write('있음')
    st.write(df.shape)
    
def get():
    destination_lat = df['위도']
    destination_lng = df['경도']
    origin_lat, origin_lng = location_getter.get()
    lat_list = destination_lat.tolist()
    lng_list = destination_lng.tolist()
    
    ds_list = []
    for i in range(len(lat_list)):
        ds_list.append(howlong.distance(origin_lat, origin_lng, lat_list[i], lng_list[i]))
    df['거리'] = pd.DataFrame(ds_list)
    return df[['상호지점명','거리']].sort_values(by='거리').head(5).to_string(index=False)
