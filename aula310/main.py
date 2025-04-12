import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333'
response = requests.get(url)
raw_html = response.text


if response.status_code == 200:
    print('Conectado')
else:
    print('Não acessível:', response.status_code)

parsed_html = BeautifulSoup(raw_html, 'html.parser') # converte tudo para python

print(parsed_html.tittle)