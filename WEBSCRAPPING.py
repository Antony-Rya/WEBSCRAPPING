from bs4 import BeautifulSoup
from lxml import etree 

import requests

html  = requests.get("https://portal.inmet.gov.br/").content

soup = BeautifulSoup(html, 'html.parser')

dom = etree.HTML(str(soup)) 
print(dom.xpath('/html/body/div[3]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/b')[0].text) 