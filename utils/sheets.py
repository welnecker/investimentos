import streamlit as st
import gspread

from google.oauth2.service_account import Credentials

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
