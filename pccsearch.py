import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import argparse
import re

# Parsear argumentos
parser = argparse.ArgumentParser(description="Scrapper de PCComponentes")
parser.add_argument("input", type=str, help="Texto a buscar o URL de producto")
args = parser.parse_args()
entrada = args.input

# Configura opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")

# Inicializa el navegador con undetected-chromedriver
driver = uc.Chrome(options=chrome_options)
driver.minimize_window()  # abre minimizado

# Detecta si es URL
if re.match(r"^https?://", entrada):
    driver.get(entrada)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    # Precio: primer span que contenga €
    precio = None
    for span in soup.find_all("span"):
        if span.text.strip().endswith("€"):
            precio = span
            break
    
    if precio:
        print(precio.text.strip())
    else:
        print("No se pudo encontrar el precio del producto.")

else:
    # Es texto de búsqueda
    query = entrada.replace(" ", "+")
    driver.get(f"https://www.pccomponentes.com/search/?query={query}")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    productos = soup.find_all("div", class_="product-card__content")
    if not productos:
        print("No se encontraron productos.")
    
    # Encabezado CSV
    print("Nombre;Precio")

    for producto in productos:
        nombre = producto.find("h3")
        precio = producto.find("span") 
        
        if nombre and precio:
            # Limpia ";" para no romper el CSV
            nombre_text = nombre.text.strip().replace(";", ",")
            precio_text = precio.text.strip().replace(";", ",")
            print(f"{nombre_text};{precio_text}")

driver.quit()

