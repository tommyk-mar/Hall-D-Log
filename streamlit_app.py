import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.title("Dashboard produkcji")

# automatyczne odświeżanie co 5 sekund
st_autorefresh(interval=5*1000, key="datarefresh")

csv_file = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

try:
    # wczytanie CSV
    df = pd.read_csv(csv_file, delimiter=';')  # delimiter ';' bo Twój CSV ma średniki

    st.subheader("Aktualne dane z produkcji")
    st.dataframe(df)  # wyświetla wszystkie wiersze

except Exception as e:
    st.error(f"Błąd odczytu pliku: {e}")
