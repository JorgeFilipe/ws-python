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

paises=[]
pais={}
id=0

for row in table_row:
    #print(row)
    #list_row=[td.string for td in row.find_all('td')] <<< Tentei usar o 'td.string', mas ele não funciona porque tem tags dentro da td, então usei o .get_text(strip=True) que pega o texto e tira os espaços em branco. O problema do .string é que ele só funciona quando existe um único nó de texto dentro da tag. E estava gerando erro porque o conteúdo não é mais um único nó de texto puro e sim as Tags:
    # O problema do .string Ele só funciona quando existe um único nó de texto dentro da tag.
    # 
    # Mas imagine:
    # 
    # <td>
    #     Brazil
    # </td>
    # 
    # Ou:
    # 
    # <td><span>Brazil</span></td>
    # 
    # Nesse caso 'td.string' pode retornar 'None' porque o conteúdo não é mais um único nó de texto puro e isso quebra seu scraper.

    list_row = [td.get_text(strip=True) for td in row.find_all('td')]
    if not list_row:
        continue

    id += 1

    for td in list_row:
        pais={
            'ID': id,
            'Pais': list_row[0],
            'Moeda': list_row[1],
            'Codigo': list_row[2],
            'Numero': list_row[3]
        }
    if pais!={}:
        paises.append(pais)
###
flag=False
flag2=False
while flag!=True:
    print()
    print("Bem-Vindo ao Negociador de Moedas V0.1")
    print()
    print("Escolha pelo n[umero da lista o país que deseja consultar o código da moeda:")
    print()
    for p in paises:
        print(f"#{p['ID']} {p['Pais']}")
    print()
    #print(f"Total de países: {len(paises)}")
    #print()

    while flag2 != True:
        try:
            entrada = int(input("░"))

            if entrada > len(paises):
                print("A opção digitada não existe!")
                continue

            for p in paises:
                if p['ID'] == entrada:
                    print()#Espaço para melhor visualização.
                    print(
                        f"No país {p['Pais']} a moeda é {p['Moeda']} "
                        f"e o código é {p['Codigo']} "
                        f"e número {p['Numero']}."
                    )
                    print()#Espaço para melhor visualização.
                    flag = True
                    flag2 = True
                    break

        except ValueError:
            print("Digite apenas números!")

    #### CODIGO ANTIGO, COM ERROS #########################
    #while flag2!=True:
    #    entrada=int(input(">>"))
    #    if type(entrada)!=int:
    #        print("A opção digitada é String, digite um número!")
    #    if entrada>len(paises):
    #        print("A opção digitada não existe!")
    #    if type(entrada)==int and entrada<=len(paises):
    #        for p in paises:
    #            if p['ID']==entrada:
    #                print(f"No país {p['Pais']} a moeda é {p['Moeda']} e o código é {p['Codigo']} e número {p['Numero']}.")
    #                print()
    #                flag=True
    #                flag2=True
    #                break