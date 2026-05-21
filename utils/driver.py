from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# =========================================================
# CONECTAR CHROME DEBUG
# =========================================================

def conectar_driver():

    options = Options()

    options.debugger_address = "127.0.0.1:9222"

    driver = webdriver.Chrome(
        options=options
    )

    return driver
