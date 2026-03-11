import streamlit as st
import pandas as pd
import time

st.title("Dashboard produkcji")

csv_file = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

# Streamlit placeholder na tabelę
placeholder = st.empty()

# główna pętla

try:
        # wczytanie całego CSV
    df = pd.read_csv(csv_file, delimiter=';')

        # wyświetlenie tabeli w Streamlit
    with placeholder.container():
        st.subheader("Aktualne dane z produkcji")
        st.dataframe(df)

except Exception as e:
    st.error(f"Błąd odczytu pliku: {e}")

    # odświeżenie co 5 sekund
time.sleep(5)
st.experimental_rerun()
st_autorefresh
