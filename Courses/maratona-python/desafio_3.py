print()
#*
# USANDO O type()
#  
# if type(x) == str:
#    print("Variavel é do tipo String")
# 
# Resumo dos Tipos:
# String: str
# Integer: int
# Float: float
# Boolean: bool 
# 
# *#


def add_food(chave, valor):
    if chave=="" or valor=="": # Trata o envio de valores vazios
        print()
        print("Para adicionar a comida você não pode enviar um dos 2 valores em branco")
        print()
    
    if type(chave)!=str or type(valor)!=str: # Trata o envio de números/caracteres especiais
        # Depois pensar em utilizar "if not comida.isalpha(): que não permite numeros mesmo sendo string"
        # E para a descrição usar "if not descricao.replace(" ", "").isalpha(): , que permite espaços + letras apenas"
        print()
        print("Para adicionar a comida você não pode enviar números")
        print()

    print()
    print(f"Mais detalhes sobre a comida {chave}. {valor}")

def delete_food(chave, valor):
    print()

def update_food(chave, valor):
    print()

def get_food(chave, valor):
    print()


nome=input("Insira o nome da comida:   ")
desc=input("Insira a descrição da comida:   ")

print(add_food(nome,desc))