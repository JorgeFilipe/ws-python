#### Este é o Desafio Prático do dia 23/05! 🐍 
#### 
#### 🔥 O Desafio de Hoje
#### Hoje você precisa fazer a parte 1 do programa: Negociador de Moedas
#### O programa deve fazer um scrapping no site do IBAN (https://www.iban.com/currency-codes) e capturar a listagem de países e suas respectivas moedas.
#### Após isso deve apresentar a lista de países para o usuário e permitir que o usuário consulte qual é o código da moeda do país selecionado.
#### Veja no vídeo da aula como o programa deve funcionar.
#### As outras funcionalidades (parte 2) faremos nos próximos dias.
#### 
#### ⚱️ Dicas de Ouro
#### • É deste site que você deve pegar os países e suas moedas: https://www.iban.com/currency-codes
#### • Faça o Scraping usando o Requests e Beautiful Soup (como ensinado no conteúdo do dia).
#### • No site do IBAN, no HTML a listagem é feita em uma tabela (table).
#### • Crie uma lista [ ] para armazenar os países e seus códigos de moeda.
#### • Cada país pode ser um dicionário dentro da lista, contendo as chaves 'nome' e 'código da moeda'. (uma dica de organização 🙂 )
#### • Alguns países não possuem moeda universal (No universal currency), não adicione esses países na lista.
#### • A input do usuário deve ser apenas números e não pode ser maior do que a listagem do menu (opções do menu).
#### • Use try: / except: quando converter a input do usuário para int. (pode ajudar).
#### • Após o usuário selecionar um país, informe o código da moeda daquele país.
#### 🥇 Conteúdo que pode te ajudar muito:
#### https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

import requests
from bs4 import BeautifulSoup

html_iban=requests.get("https://www.iban.com/currency-codes").text
soup = BeautifulSoup(html_iban, 'html.parser')
table=soup.find('table', class_="table table-bordered downloads tablesorter")
table_row=table.find_all('tr')
count=0
for row in table_row:
    list_row=row.find_all('td')
    # for td in list_row:
    #     td.string=td.string.replace('<td>','').replace('</td>','')
    print(list_row)