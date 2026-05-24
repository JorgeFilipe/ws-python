#   
#   
# https://www.infojobs.com.br/empregos.aspx?palabra=Python
# https://www.empregare.com/pt-br/vagas?query=python
# https://www.catho.com.br/vagas/python/
# https://portal.gupy.io/job-search/term=python
#   
#   
#   
import requests
import httpstatuscodelib
from bs4 import BeautifulSoup


url_infojobs = "https://www.infojobs.com.br/empregos.aspx?palabra=Python"
url_empregare = "https://www.empregare.com/pt-br/vagas?query=python"
url_catho = "https://www.catho.com.br/vagas/python/"
url_gupy = "https://portal.gupy.io/job-search/term=python"

lsturl=[url_catho,url_empregare,url_gupy,url_infojobs]

teste = requests.get(url_gupy)
html_teste = teste.text

ij = requests.get(url_infojobs)
html_ij = ij.text

#for u in lsturl:
#    r = requests.get(u)
#    print(u," 🌏 ","Status:",requests.get(u), "-",httpstatuscodelib.status_code_meaning(r.status_code))

#print()

##ℹ️--- DOCUMENTAÇÃO do BEAUTIFUL SOUP -----------------------------------------
##ℹ️ link: https://beautiful-soup-4.readthedocs.io/en/latest/#
##ℹ️____________________________________________________________________________

soup= BeautifulSoup(html_teste,'html.parser') # Parseia o resultado do teste.text (que trás todo código HTML da página), semelhante ao 'identar' do VScode. 

soup2= BeautifulSoup(html_ij,'html.parser') # Parseia o resultado do teste.text (que trás todo código HTML da página), semelhante ao 'identar' do VScode. 

#print(soup.prettify()) # Exibe o código "identado bonitinho"
#print()

## -----------------------------------------------------------------------

###### Pega o title da página
#print(soup.title)
#print()

## -----------------------------------------------------------------------

####### Busca todas as Tags 'a' no HTML (exemplo da tag a = <a> valor </a>).
#print(soup.find_all('a')) 
#print()

## -----------------------------------------------------------------------

#todos_os_as = soup.find_all('a') # Por padrão o BS trás a "soup", ou seja a resposta, em forma de lista (exemplo soup=['<a>valor 1</a>','<a>valor 2</a>','<a>valor 3</a>', etc])
#print(todos_os_as[0]) # Pega o primeiro valor da lista de tags 'a' encontradas no código HTML da página.
#print()
#print(todos_os_as[9]) # Pega o décimo valor da lista de tags 'a' encontradas no código HTML da página.
#print()

## -----------------------------------------------------------------------

###### FILTRANDO O CÓDIGO HTML
#links = soup.find_all('a')
#for link in links: # Filtrando o código HTML pegando só os links de dentro do 'href'.
#    print(link.get('href')) # Pega o 'href' dos links, para onde está direcionando.
#print()

## -----------------------------------------------------------------------

#########  Filtrando informação específica em uma página
## NÃO CONSEGUI FAZER ESSA PARTE, POIS OS SITES QUE USEI NÃO TINHAM 'id' nas Tags
## NO EXEMPLO DA AULA FICA ASSIM
## Tag no site:  <a target="_blank" id="a8wd4a654" href="www.google.com" title="Desenvolvedor Python" />
#title = soup2.find(id="a8wd4a654") # Encontra e armazena a tag que possui essa ID, no caso id="a8wd4a654"
#title_text = title.get('title') # Acessou a TAG e pega só o texto do title, no caso "Desenvolvedor Python".
#print(title_text)

#>> NOVOS TESTES USANDO A IDEIA ACIMA, SÓ QUE EM OUTROS SITES, POIS OS QUE USEI NÃO TINHAM 'id' NAS TAGS:
#>> SITE ALVO: https://www.w3schools.com/html/html_id.asp
#>> TAG ALVO = <a id="navbtn_certified" title="Certificates" role="button">Certificates</a>
#>> ID DO ALVO = id="navbtn_certified"
#>> ALVO = Certificates
novo_alvo = requests.get("https://www.w3schools.com/html/html_id.asp")
html_alvo = novo_alvo.text
soup_alvo = BeautifulSoup(html_alvo,'html.parser')
encontrando_title_alvo = soup_alvo.find(id="navbtn_certified")  # Encontra e armazena a tag que possui essa ID.
title_alvo_capturado = encontrando_title_alvo.get('title') # # Acessou a TAG e pega só o texto do title, no caso "Certificates".
print(title_alvo_capturado) # Exibe o valor capturado, nesse exemplo é "Certificates"












