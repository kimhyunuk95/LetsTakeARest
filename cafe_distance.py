import pandas as pd
import howlong
import location_getter
import streamlit as st

df = pd.read_csv('./seoul_info.csv')
if df.empty:
    st.write('없음')
else :
    st.write('있음')
    
a = df.columns[0]
st.write(a)

df = df[df['상권업종중분류명']=="커피점/카페"]
df = df[["상호명","지점명","상권업종소분류명","시군구코드",\
    "시군구명","행정동명","법정동명","지번주소","도로명주소",\
    "경도","위도"]]
df["상호지점명"] = (df["상호명"] + " " + df["지점명"].fillna("")).str.strip()    
df = df.reset_index(drop=True)

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
