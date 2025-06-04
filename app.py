import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calculador Automático de Horas",
    page_icon="🧮",
    layout="wide",
)

st.title("Calculador Automático de Horas")

st.write(
    "Esta app permite a execução automática de Horas atrasvés do report de detalhes salariais do Tamigo"
)

with st.sidebar:
    uploaded_file = st.file_uploader(
        "Importa o teu ficheiro excel aqui", type=["xlsx", "xls"]
    )

    if uploaded_file is None:
        st.sidebar.warning("Importar um ficheiro do Tamigo", icon="⚠️")
    else:
        st.sidebar.success("Dados importados corretamente, Sra. Ângela! ✅")
        df = pd.read_excel(uploaded_file)
        st.dataframe(df.head())

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df.head())
