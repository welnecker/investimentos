# utils/sheets.py

import streamlit as st
import gspread
import pandas as pd

from google.oauth2.service_account import Credentials

# =========================================================
# CONECTAR GOOGLE SHEETS
# =========================================================

def conectar_planilha():

    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scope
    )

    client = gspread.authorize(creds)

    return client.open_by_key(
        "19sE4GRsHDovx_daoD1LC2uzQ5VKoRsoaSL3sncQDH6I"
    )

# =========================================================
# CARREGAR FIIS
# =========================================================

def carregar_fiis():

    planilha = conectar_planilha()

    aba = planilha.worksheet("FIIS")

    dados = aba.get_all_records()

    df = pd.DataFrame(dados)

    return df
