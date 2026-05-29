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
##  url_infojobs = "https://www.infojobs.com.br/empregos.aspx?palabra=Python"
##  url_gupy = "https://portal.gupy.io/job-search/term=python"
##  url_progamathor="https://programathor.com.br/jobs-python"
##  url_pythonjobs = "https://www.python.org/jobs/"
##  lsturl=[url_gupy,url_infojobs,url_pythonjobs,url_progamathor]
##  print()##</br>
##  for u in lsturl:
##      r = requests.get(u)
##      print(u," 🌏 ","Status:",requests.get(u), "-",httpstatuscodelib.status_code_meaning(r.status_code))

print()#BREAKLINE

## URL + Request
url_alvo="https://www.infojobs.com.br/empregos.aspx?palabra=Python"
r_alvo = requests.get(url_alvo)

## Salva o HTML da página em uma variável
html_alvo=r_alvo.text

## Cria uma "sopa", ou seja um objeto BeautifulSoup para manipular o HTML
soup=BeautifulSoup(html_alvo,'html.parser')

## Procura a DIV com a classe "js_vacancyLoad" que contém os cards de vagas
cards = soup.find_all('div', class_="js_vacancyLoad") # procurar DIV com CLASS contais = vacancyLoad

jobs=[]

for card in cards:
    ## print(card.find('h2', class_="js_vacancyTitle").string.lstrip().rstrip()) ## CAPTURA O TITLE
    ## print(card.find('div', class_="text-medium small text-nowrap").get_text().lstrip().rstrip()) ## CAPTURA A IDADE DA VAGA

    ##-------CAPTURANDO A EMPRESA---------------
    company_class = card.find('a', class_="text-body text-decoration-none") ## SALVA A TAG INTEIRA Q CONTÉM A COMPANY
    if company_class:
        company = company_class.get_text(" ", strip=True) ## Pega a EMPRESA e formata removendo espaços
    else:
        company="Empresa Confidencial"
    print(company)
    ##------------------------------------------
    
    ##------CAPTURANDO O LOCATION---------------
    location_raw = card.find('div', class_="mb-8").get_text() ## CAPTURA O LOCATION
    split_location = [item.strip() for item in location_raw.split(',')]
    location = split_location[0]
    print(location)
    ##------------------------------------------

    job = {
        'title': card.find('h2', class_="js_vacancyTitle").string.lstrip().rstrip(), ## CAPTURA O TITLE
        'company': company,
        'location': location,
        'how_old': card.find('div', class_="text-medium small text-nowrap").get_text().lstrip().rstrip() ## CAPTURA A IDADE DA VAGA
    }
    jobs.append(job)

print(jobs)

###>> FEITO PELO COPILOT.>>>> for card in cards:
###>> FEITO PELO COPILOT.>>>>     title = card.find('h2', class_="js_vacancyTitle").get_text(strip=True) # pega o título da vaga
###>> FEITO PELO COPILOT.>>>>     company = card.find('div', class_="d-flex align-items-baseline").get_text(strip=True) # pega a empresa
###>> FEITO PELO COPILOT.>>>>     location = card.find('div', class_="mb-8").get_text(strip=True) # pega a localização
###>> FEITO PELO COPILOT.>>>>     how_old = card.find('div', class_="text-medium small text-nowrap").get_text(strip=True) # pega a idade da vaga
###>> FEITO PELO COPILOT.>>>> 
###>> FEITO PELO COPILOT.>>>>     job = {
###>> FEITO PELO COPILOT.>>>>         "title": title,
###>> FEITO PELO COPILOT.>>>>         "company": company,
###>> FEITO PELO COPILOT.>>>>         "location": location,
###>> FEITO PELO COPILOT.>>>>         "how_old": how_old
###>> FEITO PELO COPILOT.>>>>     }
###>> FEITO PELO COPILOT.>>>>     print(job)


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
