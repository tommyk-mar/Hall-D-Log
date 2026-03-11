import streamlit as st
import pandas as pd

# URL pliku CSV z Google Drive w formacie "uc"
csv_url = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

st.title("Dynamiczny podgląd CSV")

# Funkcja do pobrania danych
@st.cache_data(ttl=5)  # cache wygasa po 5 sekundach
def load_data(url):
    df = pd.read_csv(url)
    return df

# Wyświetlenie danych
data = load_data(csv_url)
st.dataframe(data)
