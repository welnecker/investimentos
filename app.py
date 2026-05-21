# app.py

import streamlit as st
import pandas as pd

from utils.sheets import carregar_fiis
from utils.score import calcular_score

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Radar FIIs",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# TÍTULO
# =========================================================

st.title("📊 Radar de FIIs")
st.caption("Monitoramento de FIIs de Papel e Tijolo")

# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_fiis()

# =========================================================
# SCORE
# =========================================================

df["Score"] = df.apply(
    calcular_score,
    axis=1
)

# =========================================================
# ORDENAÇÃO
# =========================================================

df = df.sort_values(
    by="Score",
    ascending=False
)

# =========================================================
# MÉTRICAS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "FIIs Monitorados",
    len(df)
)

col2.metric(
    "DY Médio",
    f"{df['DY'].mean():.2f}%"
)

col3.metric(
    "P/VP Médio",
    f"{df['PVP'].mean():.2f}"
)

col4.metric(
    "Maior DY",
    f"{df['DY'].max():.2f}%"
)

# =========================================================
# FILTROS
# =========================================================

st.sidebar.header("Filtros")

tipo_filtro = st.sidebar.multiselect(
    "Tipo",
    options=df["Tipo"].unique(),
    default=df["Tipo"].unique()
)

df_filtrado = df[
    df["Tipo"].isin(tipo_filtro)
]

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "📋 Geral",
    "🧱 Tijolo",
    "📄 Papel"
])

# =========================================================
# ABA GERAL
# =========================================================

with tab1:

    st.subheader("Todos os FIIs")

    st.dataframe(
        df_filtrado,
        use_container_width=True
    )

# =========================================================
# ABA TIJOLO
# =========================================================

with tab2:

    tijolo = df_filtrado[
        df_filtrado["Tipo"] == "Tijolo"
    ]

    st.subheader("FIIs de Tijolo")

    st.dataframe(
        tijolo,
        use_container_width=True
    )

# =========================================================
# ABA PAPEL
# =========================================================

with tab3:

    papel = df_filtrado[
        df_filtrado["Tipo"] == "Papel"
    ]

    st.subheader("FIIs de Papel")

    st.dataframe(
        papel,
        use_container_width=True
    )
