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


url_infojobs = "https://www.infojobs.com.br/empregos.aspx?palabra=Python"
url_empregare = "https://www.empregare.com/pt-br/vagas?query=python"
url_catho = "https://www.catho.com.br/vagas/python/"
url_gupy = "https://portal.gupy.io/job-search/term=python"

lsturl=[url_catho,url_empregare,url_gupy,url_infojobs]

teste = requests.get(url_gupy)
html_teste = requests.get(url_gupy)

for u in lsturl:
    r = requests.get(u)
    print(u," 🌏 ","Status:",requests.get(u), "-",httpstatuscodelib.status_code_meaning(r.status_code))

print()
print()


