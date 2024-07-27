import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = "https://www.kabum.com.br/espaco-gamer/cadeiras-gamer"

headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")

qtd_itens = soup.find("span", class_="bstn-hl-title gui-color-primary gui-color-hover gui-color-primary-bg-after").get_text()
print(qtd_itens)