# Caracteres para criar a "tela" no terminal
# ┌ ─ ┐ │ └ ─ ┘ ├ ─ ┤ ┬ ┴ ┼
#
# copiado do "Mapa de Caracteres" fonte 'Arial'
#


####### <junk>
# def action(opcao):
#     match opcao:
#         case 1:
#             return "Saldo de R$ 1.000"
#         case 2:
#             val=input("Insira o valor do saque: ")
#             saldo=100-val
#             return f"Valor de {val} será emitido. Saldo restante: {saldo}"
#         case 5:
#             return True
####### </junk>

flag=False
senhaStoragedDataBase="2010" #senha armazenada no banco de dados
nameStoragedDataBase="John Faulkner" #Nome do usuário armazenado no banco de dados

print("Welcome to Liberty City Bank")
print()# </br>
print("┌──────────────────────────────┐")
print("│ Welcome to Liberty City Bank │")
print("├──────────────────────────────┤")
print("│ Senha de 4 dígitos:          │")
print("├──────────────────────────────┘")
print("│")
senha=input("└► ")
print()# </br>

if senha==senhaStoragedDataBase:
    while flag != True:
        print("┌─────────────────────────────")
        print(f"│ Welcome  {nameStoragedDataBase}")
        print("├────────────────────────────┐")
        print("│ 1. Extrato                 │")
        print("│ 2. Saque                   │")
        print("│ 3. Alterar senha           │")
        print("│ 4. Alterar nome            │")
        print("│ 5. Sair                    │")
        print("└────────────────────────────┘")
        opc=int (input(">> "))
        if opc==1:
            print()# </br>
            print("┌────────────────────┐")
            print("│ SALDO DISPONIVEL   │")
            print("├─────┬──────────────┤")
            print("│  R$ │  1.000.000   │")
            print("└─────┴──────────────┘")
            print()# </br>
        if opc==2: 
            val=float(input("Insira o valor do saque: "))
            saldo=1000000-val
            print()
            print("┌───────────────────────────────────────────────────────────────────────┐")
            print(f"│  Valor de {val} será emitido em instantes. Saldo restante: {saldo}")
            print(f"├───────────────────────────────────────────────────────────────────────┤")
            print(f"│  Saldo restante: {saldo}")
            print("└───────────────────────────────────────────────────────────────────────┘")
            print()
        if opc==3:
            print()
            print(f"Senha atual: {senhaStoragedDataBase}")
            print()
            newPass=input("Insira a nova senha de 4 dígitos: ")
            senhaStoragedDataBase=newPass
            print()
            print("Senha Alterada!")
            print(f"Lembre de anotar a nova senha: {senhaStoragedDataBase}")
            print()
        if opc==4:
            print()
            print(f"Olá, {nameStoragedDataBase}! Faça a correção do seu nome abaixo")
            newName=input("Novo nome: ")
            print()
            print("Nome Alterado!")
            print(f"Lembre-se você usará: {nameStoragedDataBase} na próxima vez que realizar Login!")
            print()
        if opc==5: 
            print()
            print("       ▲ ")
            print("      / \ ")
            print("     /   \ ")
            print("    /  █  \ ")
            print("   /   ▄   \ ")
            print("  /_________\ ")
            print()
            print(">> Sessão Encerrada! Retire o Cartão! <<")
            print()
            break
else:
    print()
    print("Senha Errada!")
    print()
    print("Retire o Cartão e Tente Novamente")
    print()