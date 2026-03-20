import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Log Hala D")

# Link do CSV
#csv_url = "https://drive.google.com/uc?id=1_vjkv3wfZ_Uc8eer8evRVW_j3G5EevQq&export=download"
csv_url = "https://drive.google.com/uc?id=1HREuU-v3s_YT3f-mdIEJNwxObJoJgj-I&export=download"  

# Wczytanie oryginalnego CSV
try:
    df = pd.read_csv(csv_url, sep=";")
    df = df.replace(0,None)
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
    st.stop()

st.subheader("Log: Hala D")
st.dataframe(df)

if not df.empty:
    st.subheader("Produkcja w czasie")
    
    fig_prod = px.line(df, x='Czas', y=['Denka', 'Wieczka', 'Wkladki'], 
                       labels={'value':'Ilość', 'Czas':'Czas'})
    st.plotly_chart(fig_prod, use_container_width=True)
    st.subheader("Błędy:")  
    # Wykres odrzutów w czasie
    fig_odrzuty = px.line(df, x='Czas', y=['Blad Pobrania RS', 'Blad Pobrania RD','Blad Pobrania RM'],
                          labels={'value':'Ilość odrzuconych', 'Czas':'Czas'})
    st.plotly_chart(fig_odrzuty, use_container_width=True)


df['Czas'] = pd.to_datetime(df['Czas'], format='ISO8601')

# ostatni stan licznika w każdym dniu
dzien = df.groupby(df['Czas'].dt.date)[['Denka','Wieczka','Wkladki']].last().reset_index()
dzien = dzien.rename(columns={'Czas':'dzień'})

# produkcja dzienna
dzien['Denka_dzien'] = dzien['Denka'].diff().clip(lower=0)
dzien['Wieczka_dzien'] = dzien['Wieczka'].diff().clip(lower=0)
dzien['Wkladki_dzien'] = dzien['Wkladki'].diff().clip(lower=0)

dzien = dzien.fillna(0)

# ustawienie indeksu
dzien = dzien.set_index('dzień')

st.subheader("Denka: suma,dziennie ")
st.bar_chart(dzien[['Denka']])
st.bar_chart(dzien[['Denka_dzien']])

st.subheader("Wieczka: suma,dziennie")
st.bar_chart(dzien[['Wieczka']])
st.bar_chart(dzien[['Wieczka_dzien']])

st.subheader("Wkładki: suma,dziennie")
st.bar_chart(dzien[['Wkladki']])
st.bar_chart(dzien[['Wkladki_dzien']])
