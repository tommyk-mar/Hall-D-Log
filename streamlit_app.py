import streamlit as st
import pandas as pd
import time

st.title("Dashboard produkcji")

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

# Wykresy (opcjonalnie)
if not df.empty:
    st.subheader("Wykresy produkcji i odrzutów")
    st.line_chart(df[['Denka', 'Wieczka', 'Wkladki']])
    st.line_chart(df[['Blad A', 'Blad B']])

# --- automatyczne odświeżanie co 5 sekund ---
st_autorefresh = st.experimental_get_query_params()
refresh_interval = 5  # sekundy

# dodajemy parametr odświeżania
if "refresh" not in st_autorefresh:
    st.experimental_set_query_params(refresh=0)

# Streamlit samo odświeża stronę po podanym czasie
st.experimental_rerun()  # wymusza ponowne uruchomienie skryptu
