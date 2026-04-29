# Utilizando o módulo/projeto: Requests
# Documentação do projeto: https://requests.readthedocs.io/en/latest/
# Página do projeto: https://pypi.org/project/requests/

import requests

##url_catho = "https://www.catho.com.br/vagas/python/"
url_indeed = "https://br.indeed.com/jobs?q=python"
##request2 = requests.get(url_catho)
r = requests.get(url_indeed) ## Realiza um GET na URL

#print(request2.status_code) ## Retorna o status HTTP da conexão.
#print(request2.text) ## Retorna o texto de resposta da requisição.

#print(r.status_code) ## Retorna o status HTTP da conexão.
#print(r.text) ## Retorna o texto de resposta da requisição.

if r.status_code == 200:
    print("Site Funcionando!")
else:
    print("Site Offline")

print#LINEBREAKER💣💥
print#LINEBREAKER💣💥

#¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_¨#_#¨#_

url_teste_status_200=requests.get("https://icanhazip.com/") ## O IcanhazIP retorna o IP Público.
print()
print("URL Acessada", url_teste_status_200)
print("Status HTTP:", url_teste_status_200.status_code)
print("TEXTO DE RESPOSTA:")
print#LINEBREAKER💣💥
print(url_teste_status_200.text)


