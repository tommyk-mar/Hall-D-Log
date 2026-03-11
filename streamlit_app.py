import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Log Hala D")

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
    st.subheader("Produkcja w czasie")
    
    fig_prod = px.line(df, x='Czas', y=['Denka', 'Wieczka', 'Wkladki'], 
                       labels={'value':'Ilość', 'Czas':'Czas'})
    st.plotly_chart(fig_prod, use_container_width=True)
    
    # Wykres odrzutów w czasie
    fig_odrzuty = px.line(df, x='Czas', y=['Blad A', 'Blad B'],
                          labels={'value':'Ilość odrzuconych', 'Czas':'Czas'})
    st.plotly_chart(fig_odrzuty, use_container_width=True)


# Upewnij się, że kolumna 'czas' jest w formacie datetime
df['Czas'] = pd.to_datetime(df['Czas'], format="%d.%m.%Y %H:%M")

# Grupowanie po dniu i wybór ostatniej wartości w każdym dniu
ostatnie_denka = df.groupby(df['Czas'].dt.date)['Denka'].last().reset_index()
ostatnie_wieka = df.groupby(df['Czas'].dt.date)['Wieka'].last().reset_index()
ostatnie_wkladki = df.groupby(df['Czas'].dt.date)['Wkladki'].last().reset_index()
# Zmiana nazwy kolumn dla czytelności
ostatnie_denka.columns = ['dzień', 'ostatnie_denko']
ostatnie_wieka.columns = ['dzień', 'ostatnie_wieko']
ostatnie_wkladki.columns = ['dzień', 'ostatnia_wkladka']

st.bar_chart(data=ostatnie_denka.set_index('dzień')['ostatnie_denko','ostatnie_wieko','ostatnia_wkladka'])
