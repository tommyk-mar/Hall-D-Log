import streamlit as st
import pandas as pd

st.title("Dodawanie wartości do osobnej tabelki")

# Link do CSV
csv_url = "https://drive.google.com/uc?id=NOWE_ID_TUTAJ&export=download"

# Wczytanie oryginalnego CSV
try:
    original_df = pd.read_csv(csv_url, sep=";")
except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")
    st.stop()

st.subheader("Oryginalna tabela CSV")
st.dataframe(original_df)

# ---- Oddzielna tabelka dla nowych wartości ----
st.subheader("Nowe wartości")

# Używamy session_state, żeby przechować dodane wartości
if "new_values" not in st.session_state:
    st.session_state.new_values = pd.DataFrame(columns=[original_df.columns[0]])

# Formularz dodawania wartości
with st.form(key="add_form"):
    new_value = st.text_input(f"Wpisz wartość do kolumny '{original_df.columns[0]}'")
    submit_button = st.form_submit_button(label="Wyślij")

    if submit_button and new_value:
        # Dodajemy wartość jako nowy wiersz do osobnej tabelki
        new_row = {original_df.columns[0]: new_value}
        st.session_state.new_values = pd.concat([st.session_state.new_values, pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"Dodano wartość: {new_value}")

# Wyświetlenie tabelki z nowymi wartościami
st.dataframe(st.session_state.new_values)
