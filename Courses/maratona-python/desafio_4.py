import requests
import httpstatuscodelib # módulo criado para mapear os status codes HTTP com seus significados.

url_indeed = requests.get("https://br.indeed.com/jobs?q=python")
r=requests.get("https://www.google.com/")

print(r.status_code,": ",httpstatuscodelib.status_code_meaning(r.status_code)) 
print(url_indeed.status_code,": ",httpstatuscodelib.status_code_meaning(url_indeed.status_code)) 

flag=False
flag2=False

while flag==False:
    flag=False
    flag2=False
    print()
    print("Bem-vindo ao Verificador de Sites 1.0!")
    print()
    print("Insira as URLs dos sites que deseja verificar o status. (separadas por vírgula)")
    print()
    urls=input()
    print()
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
            flag=False
            flag2=True
        else:
            flag2=False
            flag=False
            print()
            print("Opção inválida!")
