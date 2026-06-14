import requests
from bs4 import BeautifulSoup

#def scrapping_gupy(url):


api_gupy="https://employability-portal.gupy.io/api/v1/jobs?jobName=python&limit=10&offset=0"

r_gupy = requests.get(api_gupy)

html_gupy=r_gupy.text
print(html_gupy[:5000])

soup=BeautifulSoup(html_gupy,'html.parser')

cards = soup.find_all('div', class_="sc-fjvvzt tyvCs sc-3b0b8240-5 FPfdd") # procurar DIV com CLASS contais = sc-cwHptR cgrzzg sc-3b0b8240-2 kUpsCU

#print(soup.prettify())
#print(soup.find('div', class_="sc-fjvvzt tyvCs sc-3b0b8240-5 FPfdd"))

#jobs=[]
#for card in cards:
#    ##-------CAPTURANDO A EMPRESA---------------
#    company_class = card.find('a', class_="text-body text-decoration-none") ## SALVA A TAG INTEIRA Q CONTÉM A COMPANY
#    if company_class:
#        company = company_class.get_text(" ", strip=True) ## Pega a EMPRESA e formata removendo espaços
#    else:
#        company="Empresa Confidencial"
#    ##------CAPTURANDO O LOCATION---------------
#    location_raw = card.find('div', class_="mb-8").get_text() ## CAPTURA O LOCATION
#    split_location = [item.strip() for item in location_raw.split(',')]
#    location = split_location[0]
#    job = {
#        'title': card.find('h2', class_="js_vacancyTitle").string.lstrip().rstrip(), ## CAPTURA O TITLE
#        'company': company,
#        'location': location,
#        'how_old': card.find('div', class_="text-medium small text-nowrap").get_text().lstrip().rstrip() ## CAPTURA A IDADE DA VAGA
#    }
#    jobs.append(job)
#