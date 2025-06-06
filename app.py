import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import random
from pathlib import Path
from utils.helpers import get_employee_names
from utils.helpers import get_unique_departments
from utils.helpers import get_unique_date
from calculator_engine.calculator import calcular_total_sub_almocos
from calculator_engine.calculator import calcular_total_horas_noturnas
from calculator_engine.calculator import calcular_total_gozo_ferias

st.set_page_config(
    page_title="Calculador Automático de Horas 🧮",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Calculador Automático de Horas 🧮")

st.write(
    "Esta app permite a execução automática de Horas através do report de [detalhes salariais do Tamigo](https://app.tamigo.com/Wage/Pages/WageDetails.aspx)."
)

with st.sidebar:
    st.logo(
        Path("Logos/quake_horizontal.png"),
        size="medium",
        icon_image=Path("Logos/quake_vertical.png")
    )

    uploaded_file = st.file_uploader(
        "Importe o seu ficheiro excel aqui:", type=["xlsx", "xls"]
    )

    if uploaded_file is None:
        st.sidebar.warning("Importar um ficheiro do Tamigo", icon="⚠️")
    else:
        with st.spinner("A carregar dados...", show_time=True):
            time.sleep(random.randint(1, 2))
        try:
            st.sidebar.success("Dados importados corretamente! Em baixo pode encontrar os campos que selecionou no Tamigo.", icon="✅")
            
            unique_dates = get_unique_date(uploaded_file)
            departamentos_unique = get_unique_departments(uploaded_file)
            colaboradores_unique = get_employee_names(uploaded_file)
            
            sample_data = pd.DataFrame(
            {
                "Data": unique_dates,
                "Departamentos": departamentos_unique,
                "Colaboradores": len(colaboradores_unique),
            }
            )

            st.dataframe(sample_data, hide_index=True)

        except Exception as e:
            st.sidebar.error(
                "Ocorreu um erro ao importar o ficheiro. Verifique o formato e tente novamente.",
                icon="🚨"
            )
            st.sidebar.caption(f"Erro técnico: {str(e)}")

if uploaded_file is not None:

    names = get_employee_names(uploaded_file)

    Colaboradores = st.multiselect(
        "Colaboradores",
        (names),
        placeholder="Escolha o(s) colaborador(es)",
        default=names
    )

    coluna_sub_almoco, coluna_horas_noturnas, coluna_gozo_ferias = st.columns(3)

    with coluna_sub_almoco:
        if Colaboradores:
            total_sub_almoco = calcular_total_sub_almocos(uploaded_file, Colaboradores)
        else:
            total_sub_almoco = 0
        
        st.metric("Total de subsídios de almoço 🍽️", f"{total_sub_almoco:.2f} uni")

    with coluna_horas_noturnas:
        if Colaboradores:
            total_horas_noturnas = calcular_total_horas_noturnas(
                uploaded_file, Colaboradores
            )
        else:
            total_horas_noturnas = 0

        st.metric("Total de horas noturnas 🌙", f"{total_horas_noturnas:.2f} horas")

    with coluna_gozo_ferias:
        if Colaboradores:
            total_gozo_ferias = calcular_total_gozo_ferias(uploaded_file, Colaboradores)
        else:
            total_gozo_ferias = 0

        st.metric("Total de gozo de férias 🌴", f"{total_gozo_ferias:.2f} dias")

    almocos = []
    horas = []
    ferias = []

    for colaborador in Colaboradores:
        almoco = calcular_total_sub_almocos(uploaded_file, [colaborador])
        hora = calcular_total_horas_noturnas(uploaded_file, [colaborador])
        ferias_gozadas = calcular_total_gozo_ferias(uploaded_file, [colaborador])

        almocos.append(almoco)
        horas.append(hora)
        ferias.append(ferias_gozadas)

    chart_data = pd.DataFrame(
        {
            "Colaboradores": Colaboradores,
            "Subsídios de Almoço": almocos,
            "Horas Noturnas": horas,
            "Dias de Férias": ferias,
        }
    )

    data_melted = chart_data.melt("Colaboradores", var_name="Tipo", value_name="Valor")

    chart = (
        alt.Chart(data_melted)
        .mark_bar()
        .encode(
            x="Valor:Q",
            y="Colaboradores:N",
            color=alt.Color(
                "Tipo:N",
                scale=alt.Scale(
                    domain=["Subsídios de Almoço", "Horas Noturnas", "Dias de Férias"],
                    range=["#BAA5FF", "#FFD3A5", "#FF8A8A"],
                ),
            ),
            tooltip=["Colaboradores", "Tipo", "Valor"],
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.dataframe(chart_data,hide_index=True)
