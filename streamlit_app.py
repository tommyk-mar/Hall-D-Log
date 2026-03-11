import streamlit as st
import pandas as pd
import time

st.title("Dashboard produkcji")

# miejsce na tabelę
placeholder = st.empty()

csv_file = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

REFRESH_INTERVAL = 5  # odświeżanie co 5 sekund

while True:
    try:
        # wczytanie CSV
        df = pd.read_csv(csv_file, delimiter=';')  # delimiter ';' bo Twój CSV ma średniki

        # wyświetlenie tabeli w Streamlit
        with placeholder.container():
            st.subheader("Aktualne dane z produkcji")
            st.dataframe(df)  # tabela interaktywna

    except Exception as e:
        st.error(f"Błąd odczytu pliku: {e}")

    time.sleep(REFRESH_INTERVAL)
