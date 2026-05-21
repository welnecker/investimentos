from utils.driver import conectar_driver

# =========================================================
# OBTER HTML
# =========================================================

def obter_html(url):

    driver = conectar_driver()

    driver.get(url)

    html = driver.page_source

    return html
