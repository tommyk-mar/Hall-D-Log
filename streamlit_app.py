import streamlit as st
import pandas as pd

st.title("Dynamiczny podgląd CSV bez cache")

csv_url = "https://drive.google.com/uc?id=1_vjkv3wfZ_Uc8eer8evRVW_j3G5EevQq"

try:
    df = pd.read_csv(csv_url, sep = ";")
    st.subheader("Tabela CSV")
    st.dataframe(df, width=1600, height=800)
    st.table(df)
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
