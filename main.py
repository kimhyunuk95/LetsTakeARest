import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
import json
import requests
import cafe_distance


def main():
  result = cafe_distance.get()
  st.write(result)
    
    
main()
