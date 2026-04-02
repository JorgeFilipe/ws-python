
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

#food_list=[
#    {"comida":"paçoquinha","descricao":"Um doce de amendoin brasileiro"},
#    {"comida":"brigadeiro","descricao":"um doce muito delicioso"},
#    {"comida":"pizza","descricao":"um tipo de comida italiana"},
#    {"comida":"hamburguer","descricao":"fastfood muito comum nos EUA"},
#    {"comida":"a","descricao":"b"}
#

food_list= {
    'paçoquinha':'Um doce de amendoin brasileiro',
    'brigadeiro':'um doce muito delicioso',
    'pizza':'um tipo de comida italiana',
    'hamburguer':'fastfood muito comum nos EUA',
    'a':'b'
}

# ADICIONAR
def add_food(chave, valor):
    valido=True

    if chave=="" or valor=="": # Trata o envio de valores vazios
        valido=False
        print()
        print("🟡 Para adicionar a comida você deve enviar 2 valores, nome da comida e descrição 🟡")
        print()

    if type(chave)!=str or type(valor)!=str: # Trata o envio de números/caracteres especiais
        # Depois pensar em utilizar "if not comida.isalpha(): que não permite numeros mesmo sendo string"
        # E para a descrição usar "if not descricao.replace(" ", "").isalpha(): , que permite espaços + letras apenas"
        valido=False
        print()
        print("🟡 Para adicionar a comida você não pode enviar números 🟡")
        print()

    for comida in food_list:# Trata o cadastro de comidas repetidas
        if comida == chave:
            valido=False
            print()
            print(f"🟡 {comida} já está cadastrado no sistema 🟡")
            print()
            break

    if valido==True:
        food_list[chave]=valor
        print()
        print("COMIDA CADASTRADA ✅")
        print()

    if valido==False:
        print()
        print("❌ OPERAÇÃO CANCELADA POR CAUSA DE INCONSISTÊNCIAS ❌")
        print()

# DELETE
def delete_food(chave):
    valido=True
    cont=0

    if chave=="": # Trata o envio de valores vazios
        valido=False
        print()
        print("🔴 Para deletar a comida você não pode enviar valores em branco 🔴")

    if type(chave)!=str: # Trata o envio de números/caracteres especiais
        valido=False
        print()
        print("🔴 Para deletar a comida você não pode enviar números 🔴")

    for comida in food_list: # Busca no Dict se a comida existe
        if comida!=chave:
            cont=cont+1
    if cont==len(food_list): # Busca no Dict se a comida existe
        print()
        print(f"🔴 {chave} não foi encontrado no sistema 🔴")

    if valido==True:
        for comida in food_list:# Remove a comida do dicionario
            if comida == chave:
                print()
                print(f"🟥 {comida} foi removido do sistema 🟥")
                del food_list[comida]
                break           

    if valido==False:
        print()
        print("❌ OPERAÇÃO CANCELADA POR CAUSA DE INCONSISTÊNCIAS ❌")

# ATUALIZAR
def update_food(chave, valor):
    print()

# BUSCAR DESCRIÇÃO
def get_food(chave, valor):
    print()
flag=False
while flag==False:
    print()
    print(" ______________________________________________")
    print("|  BEM-VINDO AO SISTEMA DO MENU DIGITAL")
    print("|----------------------------------------------")
    print("|  1. Adicionar comida ao Menu Digital")
    print("|  2. Deletar comida do Menu Digital")
    print("|  3. Atualizar detalhes da comida no Menu Digital")
    print("|  4. Buscar detalhes da comida no Menu Digital")
    print("|  5. Listar comidas cadastradas no Menu Digital")
    print("|  ")
    print("|  0. Sair")
    print("|_______________________________________________")
    print("|")
    opt=input("|>> ")

    if opt=="0" or opt=="":
        flag=True

    if opt=="1":
        chave=input("Informe o nome da comida: ")
        valor=input("Informe a descrição da comida: ")
        add_food(chave,valor)

    if opt=="2":
        print()
        chave=input("Informe o nome da comida que quer Deletar: ")
        delete_food(chave)

    if opt=="3":
        print()

    if opt=="4":
        print()

    if opt=="5": # Lista os itens do Dict food_list
        print()
        for comida in food_list:
            print(comida,"-",food_list[comida])
        #print(food_list)
        print()
    
    
print()
#print(food_list)