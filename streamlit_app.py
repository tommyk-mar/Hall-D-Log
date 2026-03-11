import streamlit as st
import pandas as pd

st.title("Dynamiczny podgląd CSV bez cache")

csv_url = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

try:
    df = pd.read_csv(csv_url)
    st.dataframe(df)
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
