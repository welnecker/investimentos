from utils.scraper import obter_html
from utils.parser import extrair_indicadores

# =========================================================
# URL
# =========================================================

url = "https://investidor10.com.br/fiis/hglg11/"

# =========================================================
# CAPTURAR HTML
# =========================================================

html = obter_html(url)

# =========================================================
# EXTRAIR DADOS
# =========================================================

dados = extrair_indicadores(html)

# =========================================================
# RESULTADO
# =========================================================

print()

print("DADOS EXTRAÍDOS")

print(dados)

print()
