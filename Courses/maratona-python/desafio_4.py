import requests
import httpstatuscodelib # módulo criado para mapear os status codes HTTP com seus significados.

url_indeed = requests.get("https://br.indeed.com/jobs?q=python")
r=requests.get("https://www.google.com/")

print(r.status_code,": ",httpstatuscodelib.status_code_meaning(r.status_code)) 
print(url_indeed.status_code,": ",httpstatuscodelib.status_code_meaning(url_indeed.status_code)) 

