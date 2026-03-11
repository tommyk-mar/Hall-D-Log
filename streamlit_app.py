import streamlit as st
import pandas as pd
import time

# link do CSV
url = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

st.title("Dashboard produkcji")

# miejsce na dane
placeholder = st.empty()

while True:
    try:
        df = pd.read_csv(url)
        
        with placeholder.container():
            st.subheader("Ostatnie próbki")
            st.dataframe(df.tail(10))  # ostatnie 10 wierszy
            
            st.line_chart(df['produkcja'])  # wykres produkcji
            st.line_chart(df['odrzut'])    # wykres odrzutów

    except Exception as e:
        st.error(f"Błąd odczytu pliku: {e}")

    time.sleep(5)  # odświeżanie co 5 sekund
