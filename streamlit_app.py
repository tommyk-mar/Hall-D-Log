import streamlit as st
import pandas as pd

st.title("Dodawanie wartości do osobnej tabelki")

# Link do CSV
csv_url = "https://drive.google.com/uc?id=1_vjkv3wfZ_Uc8eer8evRVW_j3G5EevQq&export=download"

# Wczytanie oryginalnego CSV
try:
    original_df = pd.read_csv(csv_url, sep=";")
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
    st.stop()

st.subheader("Log: Hala D")
st.dataframe(original_df)

fig, ax = plt.subplots()
ax.bar(df["Produkt"], df["Uzytki"], label="Użytek 1")
ax.bar(df["Produkt"], df["Uzytki2"], bottom=df["Uzytki"], label="Użytek 2")  # wykres skumulowany
ax.set_xlabel("Produkt")
ax.set_ylabel("Liczba użytków")
ax.set_title("Wykres użytków")
ax.legend()
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

st.pyplot(fig)
