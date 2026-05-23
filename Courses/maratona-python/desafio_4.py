## 
## 💡Proximas Ideias:
##  | 
##  | AO RETORNAR O STATUS DE CADA URL, MOSTRAR O CÓDIGO HTTP RETORNADO
##  | E O SIGNIFICADO DO STATUS CODE RETORNADO.
##  | 
##  | 
##  | 
## 
## 
## 


import requests
import httpstatuscodelib # módulo criado para mapear os status codes HTTP com seus significados.

url_indeed = requests.get("https://br.indeed.com/jobs?q=python")
r=requests.get("https://www.google.com/")

print(r.status_code,": ",httpstatuscodelib.status_code_meaning(r.status_code)) 
print(url_indeed.status_code,": ",httpstatuscodelib.status_code_meaning(url_indeed.status_code)) 

def valida_url(entrada):
    r=requests.get(entrada)
    if r.status_code==200:
        result="🟢 Site Online "
    else:
        result="🔴 Site Offline "
    return result

flag=False
flag2=False
lista_de_urls=[]
urls_validas=[]
urls_invalidas=[]

while flag==False:
    lista_de_urls.clear()
    urls_validas.clear()
    urls_invalidas.clear()
    flag=False
    flag2=False
    print()
    print("Bem-vindo ao Verificador de Sites 1.0!")
    print()
    print("Insira as URLs dos sites que deseja verificar o status. (separadas por vírgula)")
    print()
    urls=input()
    print()
    
    lista_de_urls = [item.strip() for item in urls.split(',')] # Pega cada valor separando por vírgula (split) e trata removendo os espaços do inicio e do final de cada item com o strip(), depois adiciona os itens tratados em uma nova lista.

    for u in lista_de_urls:
        if "." in u in lista_de_urls: # PESQUISA SE DENTRO DO ITEM POSSUI PONTO.
            if u.startswith("https://") or u.startswith("http://"):
                urls_validas.append(u)
            else:
                urls_validas.append("https://"+u) # ADICIONA AS URLS VÁLIDAS EM UMA NOVA LISTA.
        else:
            urls_invalidas.append(u+" URL Inválida") # ADICIONA AS URLS INVÁLIDAS EM UMA NOVA LISTA.
    #urls_tratadas = [u if u.startswith(("http://", "https://")) else f"https://{u}" for u in lista_de_urls]

    #print(urls_validas)
    #print(urls_invalidas)
    for u in urls_validas:
        print(f"{u} ",valida_url(u))
    for u in urls_invalidas:
        print(f"{u}")

    while flag2==False: #Loop para tratar opção inválidas e/ou sair do programa.
        print()
        op=input("Precisa verificar mais algum site? s/n: ")
        if op=="n" or op=="N":
            flag=True
            flag2=True
            print()
            print("Programa Encerrado!")
            print()
        elif op=="s" or op=="S":
            #lista_de_urls.clear
            #urls_validas.clear
            #urls_invalidas.clear
            flag=False
            flag2=True
        else:
            flag2=False
            flag=False
            print()
            print("Opção inválida!")