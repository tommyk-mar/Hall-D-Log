import streamlit as st
import pandas as pd
import time

st.title("Dashboard produkcji")

# miejsce na tabelę
placeholder = st.empty()

csv_file = "dane_log.csv"  # jeśli w Drive -> podmień link na 'https://drive.google.com/uc?id=ID_PLIKU'

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
