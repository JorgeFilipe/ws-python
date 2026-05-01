import requests
import httpstatuscodelib

list_urls=['google', 'icanhazip.com', 'ip-api', 'youtube.com']
for i in list_urls:
    if "." in i in list_urls: # PESQUISA SE DENTRO DO ITEM POSSUI PONTO.
        print()#QUEBRALINHA
        print(i," é uma URL válida! ✅")
    else:
        print()#QUEBRALINHA
        print(i,"é uma URL inválida! ❌")

print()#QUEBRALINHA
print()#QUEBRALINHA

list_words=['asa', 'parede', 'assobio', 'porta', 'asfalto', 'janela', 'assimétrico']
for w in list_words:
    if "as" in w in list_words: # PESQUISA SE DENTRO DO ITEM POSSUI "as".
        print()#QUEBRALINHA
        print(w," é uma palavra que contém \"as\" ✅")
    else:
        print()#QUEBRALINHA
        print(w," é uma palavra que NÃO contém \"as\" ❌")


print()#QUEBRALINHA
print("-------------------------------------------")#QUEBRALINHA
print()#QUEBRALINHA

# PESQUISANDO SE AS URLS POSSUEM PONTO "." E SE SÃO VÁLIDAS E DEPOIS SEPARANDO EM LISTAS DIFERENTES.
urls_invalidas=[]
urls_validas=[]
urls=['google.com', 'https://ip-api.com', 'dd2d2wed233423', 'icanhazip.com', 'Wasd18dw1', 'janela', 'https://bitly.com/']

for url in urls:
    if "." in url in urls: # PESQUISA SE DENTRO DO ITEM POSSUI "as".
        urls_validas.append(url)
    else:
        urls_invalidas.append(url)

# NOVA LISTA = urls_validas + urls_inválidas


print()#QUEBRALINHA
print("URLs Válidas ✅:")
print(urls_validas)
print()#QUEBRALINHA
print("URLs Inválidas ❌:")
print(urls_invalidas)
print()#QUEBRALINHA