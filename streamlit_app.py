import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Hala D", layout="wide")
st.title("Dashboard produkcji - Hala D")

# Link do CSV (Google Drive)
csv_url = "https://drive.google.com/uc?id=1_vjkv3wfZ_Uc8eer8evRVW_j3G5EevQq&export=download"

# Auto-odświeżanie co 5 sekund
st.markdown('<meta http-equiv="refresh" content="5">', unsafe_allow_html=True)

# Wczytanie CSV
try:
    df = pd.read_csv(csv_url, sep=";")
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
    st.stop()

# --- Konwersja kolumny Czas na datetime (bezpieczna) ---
if not pd.api.types.is_datetime64_any_dtype(df['Czas']):
    df['Czas'] = pd.to_datetime(df['Czas'], errors='coerce')

# --- Wyświetlenie tabeli ---
st.subheader("Log: Hala D")
st.dataframe(df, use_container_width=True)

if not df.empty:
    # --- Wykres liniowy produkcji w czasie ---
    st.subheader("Produkcja w czasie")
    fig_prod = px.line(
        df,
        x='Czas',
        y=['Denka', 'Wieczka', 'Wkladki'],
        labels={'value':'Ilość', 'Czas':'Czas'}
    )
    st.plotly_chart(fig_prod, use_container_width=True)
    
    # --- Wykres liniowy odrzutów w czasie ---
    st.subheader("Odrzuty w czasie")
    fig_odrzuty = px.line(
        df,
        x='Czas',
        y=['Blad A', 'Blad B'],
        labels={'value':'Ilość odrzuconych', 'Czas':'Czas'}
    )
    st.plotly_chart(fig_odrzuty, use_container_width=True)
    
    # --- Wykres kolumnowy: ostatnia próbka z każdego dnia ---
    df_last_per_day = df.groupby(df['Czas'].dt.date).last().reset_index()
    
    st.subheader("Ostatnia próbka produkcji każdego dnia")
    fig_daily = px.bar(
        df_last_per_day,
        x='Czas',
        y=['Denka', 'Wieczka', 'Wkladki'],
        barmode='group',
        labels={'Czas':'Data', 'value':'Ilość'}
    )
    st.plotly_chart(fig_daily, use_container_width=True)
