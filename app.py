import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('scum_model.pkl', 'rb'))

st.title("Scum Prediction System")

fe = st.number_input("Fe%", min_value=0.0)
oil = st.number_input("Oil%", min_value=0.0)
ph = st.number_input("pH", min_value=0.0)
esi = st.number_input("ESI", min_value=0.0)
filter_paper = st.selectbox("Filter Paper", [0, 1])

if st.button("Predict"):
    result = model.predict([[fe, oil, ph, esi, filter_paper]])
    if result[0] == 1:
        st.error("WARNING! Scum will form!")
    else:
        st.success("No Scum! All good!")
