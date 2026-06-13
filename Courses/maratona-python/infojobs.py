import requests
from bs4 import BeautifulSoup

def scrapping_infojobs(url):
    ## URL + Request
    r_infojobs = requests.get(url)
    ## Salva o HTML da página em uma variável
    html_infojobs=r_infojobs.text
    ## Cria uma "sopa", ou seja um objeto BeautifulSoup para manipular o HTML
    soup=BeautifulSoup(html_infojobs,'html.parser')
    ## Filtrar os cards
    cards = soup.find_all('div', class_="js_vacancyLoad") # procurar DIV com CLASS contais = vacancyLoad
    jobs=[]
    for card in cards:
        ##-------CAPTURANDO A EMPRESA---------------
        company_class = card.find('a', class_="text-body text-decoration-none") ## SALVA A TAG INTEIRA Q CONTÉM A COMPANY
        if company_class:
            company = company_class.get_text(" ", strip=True) ## Pega a EMPRESA e formata removendo espaços
        else:
            company="Empresa Confidencial"
        ##------CAPTURANDO O LOCATION---------------
        location_raw = card.find('div', class_="mb-8").get_text() ## CAPTURA O LOCATION
        split_location = [item.strip() for item in location_raw.split(',')]
        location = split_location[0]
        job = {
            'title': card.find('h2', class_="js_vacancyTitle").string.lstrip().rstrip(), ## CAPTURA O TITLE
            'company': company,
            'location': location,
            'how_old': card.find('div', class_="text-medium small text-nowrap").get_text().lstrip().rstrip() ## CAPTURA A IDADE DA VAGA
        }
        jobs.append(job)
    return jobs