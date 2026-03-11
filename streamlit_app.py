import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.title("Dashboard produkcji")

# odświeżanie co 5 sekund (5000 ms)
st_autorefresh(interval=5000, key="refresh")

# Link do CSV na Google Drive
csv_file = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

# Wczytanie CSV
try:
    df = pd.read_csv(csv_file, delimiter=';')
except Exception as e:
    st.error(f"Błąd odczytu CSV: {e}")
    df = pd.DataFrame()

# Wyświetlenie tabeli
st.subheader("Aktualne dane z produkcji")
st.dataframe(df, use_container_width=True)

# Wykresy
if not df.empty:
    st.subheader("Wykresy produkcji i odrzutów")
    st.line_chart(df[['Denka', 'Wieczka', 'Wkladki']])
    st.line_chart(df[['Blad A', 'Blad B']])
