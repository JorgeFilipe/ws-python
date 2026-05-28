import requests
from bs4 import BeautifulSoup
import httpstatuscodelib

## job = {
##     "title": "Titulo da Vaga",
##     "company": "Empresa que oferece a vaga",
##     "location": "Localização da vaga",
##     "how_old": "Idade da vaga"
## }

## VERIFICAR SE A URL RETORNA [200] PARA CONSEGUIR MANIPULAR OS DADOS.
url_infojobs = "https://www.infojobs.com.br/empregos.aspx?palabra=Python"
url_gupy = "https://portal.gupy.io/job-search/term=python"
url_progamathor="https://programathor.com.br/jobs-python"
url_pythonjobs = "https://www.python.org/jobs/"
lsturl=[url_gupy,url_infojobs,url_pythonjobs,url_progamathor]
print()##</br>
for u in lsturl:
    r = requests.get(u)
    print(u," 🌏 ","Status:",requests.get(u), "-",httpstatuscodelib.status_code_meaning(r.status_code))

## ***
print()##</br>

url_alvo="https://www.infojobs.com.br/empregos.aspx?palabra=Python"

html_alvo=requests.get(url_alvo).text

soup=BeautifulSoup(html_alvo,'html.parser')

cards = soup.find('div', class_="js_vacancyLoad") # procurar DIV com CLASS contais = vacancyLoad

print(cards)


# Pagina InfoJobs (https://www.infojobs.com.br/empregos.aspx?palabra=Python)
# tag 'h2' com class="js_vacancyTitle" ou h2.string # pega nome da vaga
# tag 'div' com class="d-flex align-items-baseline" mais tem que usar a função get_text() do BS # Pega a Company
# tag 'div' com class="mb-8" tentar pegar apenas a primeira de cada CARD pois a segunda tag com essa classe trás infos desnecessárias # Pega o Location
# div com class="text-medium small text-nowrap" # Pega o how_old


##############################
# Página Gupy (https://portal.gupy.io/job-search/term=python)
# tag 'h3' com class="sc-iHGNWf jvRwVv sc-3b0b8240-4 ihxGJr" ou h3.string pega o title
# tag 'p' com class="sc-fjvvzt tyvCs sc-3b0b8240-5 FPfdd" # Pega Company
# tag 'span' com data-testid="job-location" # Pega Location (mas tem que ver como pegar o atributo 'data-testid' no BS)
# tag 'p' com class="sc-fjvvzt tyvCs sc-e6fca2ac-0 bteFxv" pega o how_old#
