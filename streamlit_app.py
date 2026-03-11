import streamlit as st
import pandas as pd

st.title("Dodawanie wartości do osobnej tabelki")

# Link do CSV
csv_url = "https://drive.google.com/uc?id=1_vjkv3wfZ_Uc8eer8evRVW_j3G5EevQq&export=download"

# Wczytanie oryginalnego CSV
try:
    df = pd.read_csv(csv_url, sep=";")
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
    st.stop()

st.subheader("Log: Hala D")
st.dataframe(df)

if not df.empty:
    st.subheader("Wykresy produkcji i odrzutów")
    st.line_chart(df[['Denka', 'Wieczka', 'Wkladki']])
    st.line_chart(df[['Blad A', 'Blad B']])
