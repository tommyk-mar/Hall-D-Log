import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard produkcji")

csv_file = "dane_log.csv"

# Wczytanie CSV
df = pd.read_csv(csv_file, delimiter=';')

# Zamiana kolumny 'Czas' na datetime
df['Czas'] = pd.to_datetime(df['Czas'])

# --- Wykres produkcji w czasie ---
if not df.empty:
    st.subheader("Produkcja w czasie")
    
    fig_prod = px.line(df, x='Czas', y=['Denka', 'Wieczka', 'Wkladki'], 
                       labels={'value':'Ilość', 'Czas':'Czas'})
    st.plotly_chart(fig_prod, use_container_width=True)
    
    # Wykres odrzutów w czasie
    fig_odrzuty = px.line(df, x='Czas', y=['Blad A', 'Blad B'],
                          labels={'value':'Ilość odrzuconych', 'Czas':'Czas'})
    st.plotly_chart(fig_odrzuty, use_container_width=True)

# --- Wykres kolumnowy: ostatnia próbka z każdego dnia ---
df_last_per_day = df.groupby(df['Czas'].dt.date).last().reset_index()

st.subheader("Ostatnia próbka każdego dnia (produkcja)")

fig_daily = px.bar(df_last_per_day, x='Czas', y=['Denka', 'Wieczka', 'Wkladki'],
                   labels={'Czas':'Data', 'value':'Ilość'}, barmode='group')
st.plotly_chart(fig_daily, use_container_width=True)
