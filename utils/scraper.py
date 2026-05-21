import requests
from bs4 import BeautifulSoup

# =========================================================
# COLETAR FII
# =========================================================

def coletar_fii(ticker):

    url = f"https://investidor10.com.br/fiis/{ticker.lower()}/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    dados = {}

    try:

        indicadores = soup.find_all(
            "div",
            class_="_card-body"
        )

        texto = soup.get_text()

        dados["Fundo"] = ticker

        return dados

    except Exception as erro:

        print(f"Erro em {ticker}: {erro}")

        return None
