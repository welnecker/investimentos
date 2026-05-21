from bs4 import BeautifulSoup
import re

# =========================================================
# EXTRAIR INDICADORES
# =========================================================

def extrair_indicadores(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    texto = soup.get_text(
        separator=" ",
        strip=True
    )

    dados = {}

    # =====================================================
    # DY
    # =====================================================

    dy = re.search(
        r"DY \(12M\)\s*([\d,]+)",
        texto
    )

    if dy:

        dados["DY"] = float(
            dy.group(1).replace(",", ".")
        )

    # =====================================================
    # P/VP
    # =====================================================

    pvp = re.search(
        r"P/VP\s*([\d,]+)",
        texto
    )

    if pvp:

        dados["PVP"] = float(
            pvp.group(1).replace(",", ".")
        )

    # =====================================================
    # LIQUIDEZ
    # =====================================================

    liquidez = re.search(
        r"Liquidez Diária\s*R\$\s*([\d,]+)\s*M",
        texto
    )

    if liquidez:

        valor = float(
            liquidez.group(1).replace(",", ".")
        )

        dados["Liquidez"] = valor * 1000000

    return dados
