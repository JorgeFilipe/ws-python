


####################
########      ########
#####            ######       ##################     ####################
####              #####       #################      ###################
####              #####       ####                   #####
########      ########        ####                   #####
#####################         ###########            ############     #######     
#####        ######           ###########            #########      ###     ###     #######  #########
#####         ######          ####                   #####         ####     ####         #   ##  
#####          ######         ####                   #####         #############       #     #######   
#####           ######        #################      #####         ####     ####     #       ##
#####            ######       ##################     #####         ####     ####    #######  ######### 


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

food_list=[
    {"comida":"paçoquinha","descricao":"Um doce de amendoin brasileiro"},
    {"comida":"brigadeiro","descricao":"um doce muito delicioso"},
    {"comida":"pizza","descricao":"um tipo de comida italiana"},
    {"comida":"hamburguer","descricao":"fastfood muito comum nos EUA"},
    {"comida":"a","descricao":"b"}
]

def add_food(chave, valor):
    valido=True

    if chave=="" or valor=="": # Trata o envio de valores vazios
        valido=False
        print()
        print("Para adicionar a comida você não pode enviar um dos 2 valores em branco")
        print()
    
    if type(chave)!=str or type(valor)!=str: # Trata o envio de números/caracteres especiais
        # Depois pensar em utilizar "if not comida.isalpha(): que não permite numeros mesmo sendo string"
        # E para a descrição usar "if not descricao.replace(" ", "").isalpha(): , que permite espaços + letras apenas"
        valido=False
        print()
        print("Para adicionar a comida você não pode enviar números")
        print()

    for comida in food_list: # Trata o cadastro de comidas repetidas
        if comida["comida"]==chave:
            print()
            print(f" {comida['comida']} já está cadastrado no sistema")
            valido=False
            break

    if valido==True:
        #food_list[]={'comida':chave,'descricao':valor}
        print()
        print("COMIDA CADASTRADA ✅")
        print()
        print(food_list)

    
    if valido==False:
        print()
        print("❌🟥 OPERAÇÃO CANCELADA POR CAUSA DE INCONSISTÊNCIAS ❌🟥")
        print()

def delete_food(chave, valor):
    print()

def update_food(chave, valor):
    print()

def get_food(chave, valor):
    print()


nome=input("Insira o nome da comida:   ")
desc=input("Insira a descrição da comida:   ")

print(add_food(nome,desc))