import streamlit as st
import pandas as pd
import plotly.express as px

from utils.sheets import carregar_fiis
from utils.score import calcular_score
from utils.indicadores import (
    formatar_milhoes,
    definir_status,
    colorir_score
)

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Radar FIIs",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================

st.title("📊 Radar de FIIs")
st.caption("Monitoramento de FIIs de Papel e Tijolo")

# =========================================================
# DADOS
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
# STATUS
# =========================================================

df["Status"] = df.apply(
    definir_status,
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
# SIDEBAR
# =========================================================

st.sidebar.header("Filtros")

tipo_filtro = st.sidebar.multiselect(
    "Tipo",
    options=df["Tipo"].unique(),
    default=df["Tipo"].unique()
)

# =========================================================
# FILTRAR
# =========================================================

df_filtrado = df[
    df["Tipo"].isin(tipo_filtro)
].copy()

# =========================================================
# FORMATAR
# =========================================================

df_exibicao = df_filtrado.copy()

df_exibicao["Liquidez"] = df_exibicao[
    "Liquidez"
].apply(formatar_milhoes)

# =========================================================
# OPORTUNIDADES
# =========================================================

oportunidades = df_filtrado[
    (df_filtrado["PVP"] < 0.95)
    &
    (df_filtrado["DY"] > 9)
]

if len(oportunidades) > 0:

    st.success(
        f"🟢 {len(oportunidades)} oportunidades encontradas"
    )

# =========================================================
# GRÁFICO
# =========================================================

st.subheader("📈 Radar de Oportunidades")

fig = px.scatter(
    df_filtrado,
    x="PVP",
    y="DY",
    color="Tipo",
    size="Score",
    text="Fundo",
    hover_data=["Liquidez"],
    height=500
)

fig.update_traces(
    textposition="top center"
)

fig.update_layout(
    xaxis_title="P/VP",
    yaxis_title="Dividend Yield (%)",
    legend_title="Tipo",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "📋 Geral",
    "🧱 Tijolo",
    "📄 Papel"
])

# =========================================================
# GERAL
# =========================================================

with tab1:

    st.subheader("Todos os FIIs")

    st.data_editor(
        df_exibicao,
        use_container_width=True,
        disabled=True
    )

# =========================================================
# TIJOLO
# =========================================================

with tab2:

    tijolo = df_exibicao[
        df_exibicao["Tipo"] == "Tijolo"
    ]

    st.subheader("FIIs de Tijolo")

    st.data_editor(
        tijolo,
        use_container_width=True,
        disabled=True
    )

# =========================================================
# PAPEL
# =========================================================

with tab3:

    papel = df_exibicao[
        df_exibicao["Tipo"] == "Papel"
    ]

    st.subheader("FIIs de Papel")

    st.data_editor(
        papel,
        use_container_width=True,
        disabled=True
    )
