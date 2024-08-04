from io import BytesIO
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd
st.header("Upload Railway Act Data")

upload_form = st.form("upload_form", clear_on_submit=True, border=True)
uploaded_file = upload_form.file_uploader("Please submit a excel file (.xls) containing the data to be analyzed here:", type=['xls'])
submit = upload_form.form_submit_button("Submit")

if submit:
    if uploaded_file:
        data= pd.read_excel(uploaded_file)
        st.write(data)
        st.session_state.data = data
        st.success("The data has been uploaded successfully!!")
    else:
        st.warning("Please upload the relevant data!")