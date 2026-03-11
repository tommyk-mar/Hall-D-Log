import streamlit as st
import pandas as pd

st.title("Dynamiczny podgląd CSV bez cache")

csv_url = "https://drive.google.com/uc?id=1_vjkv3wfZ_Uc8eer8evRVW_j3G5EevQq"

try:
    df = pd.read_csv(csv_url, sep = ";")
    st.subheader("Tabela CSV")
    st.dataframe(df, width=2000, height=600)

except Exception as e:
    st.error(f"Nie udało się wczytać pliku CSV: {e}")

st.subheader("Dodaj nową wartość")
with st.form(key="add_form"):
    # Zakładamy, że CSV ma kolumnę 'Wartość', jeśli jest inna, zmień nazwę
    new_value = st.text_input("Wpisz wartość")
    submit_button = st.form_submit_button(label="Wyślij")

    if submit_button:
        # Dodanie nowego wiersza
        new_row = {df.columns[0]: new_value}  # tylko pierwsza kolumna w tym przykładzie
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"Dodano wartość: {new_value}")
