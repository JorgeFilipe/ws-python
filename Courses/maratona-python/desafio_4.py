import requests
import httpstatuscodelib # módulo criado para mapear os status codes HTTP com seus significados.

url_indeed = requests.get("https://br.indeed.com/jobs?q=python")
r=requests.get("https://www.google.com/") ## O Google é um site que tem alta disponibilidade, ou seja, dificilmente fica offline.
print("Status HTTP:", r.status_code) ## O status code 200 é o código de
print(httpstatuscodelib.status_code_meaning(r.status_code)) ## O status code 200 é o código de "OK", ou seja, a requisição foi bem sucedida.

