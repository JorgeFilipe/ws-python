import requests
from bs4 import BeautifulSoup

#def scrapping_gupy(url):


api_gupy="https://employability-portal.gupy.io/api/v1/jobs?jobName=python&limit=10&offset=0"

r_gupy = requests.get(api_gupy)

dados = r_gupy.json()

#print(type(dados))
jobs=[]
for dado in dados['data']:
    job = {
        'title': dado['name'], ## CAPTURA O TITLE
        'company': dado['careerPageName'], ## CAPTURA A COMPANY
        'location': dado['city']+" - "+dado['state']+" - "+dado['country'],
        'how_old':  dado['publishedDate'] ## CAPTURA A IDADE DA VAGA
    }
    jobs.append(job)

print(jobs)

for job in jobs:
    print(job['title'])
    print(job['company'])
    print(job['location'])
    print(job['how_old'])
    print()
    print("-----------------------------")
    print()