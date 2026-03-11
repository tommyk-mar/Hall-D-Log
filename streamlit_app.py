import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Produkcji", layout="wide")
st.title("Dashboard produkcji")

csv_file = "https://drive.google.com/uc?id=1U6EadEGw-gFn63lnQTrtv43qtV_H9nnt"

# --- Sekcja JavaScript odświeżająca stronę co 5 sekund ---
st.markdown(
    """
    <script>
    function refresh(){
        setTimeout(function(){window.location.reload();}, 5000);
    }
    refresh();
    </script>
    """,
    unsafe_allow_html=True
)

# --- Wczytanie CSV ---
try:
    df = pd.read_csv(csv_file, delimiter=';')
except Exception as e:
    st.error(f"Błąd odczytu CSV: {e}")
    df = pd.DataFrame()

# --- Wyświetlenie tabeli ---
st.subheader("Aktualne dane z produkcji")
st.dataframe(df, use_container_width=True)

# --- Wykresy ---
if not df.empty:
    st.subheader("Wykresy produkcji i odrzutów")
    st.line_chart(df[['Denka', 'Wieczka', 'Wkladki']])
    st.line_chart(df[['Blad A', 'Blad B']])
