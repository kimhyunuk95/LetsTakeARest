import streamlit as st
import pandas as pd
import numpy as np
import cafe_distance

result = cafe_distance.get()
st.write(result)
