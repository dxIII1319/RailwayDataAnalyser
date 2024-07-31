import pandas as pd

import streamlit as st


@st.cache_data
def load_data():
    data = pd.read_excel('data/data.xls')
    return data
