# ============================================================================
# FAETEC PBI - LP1 - Trabalho da Disciplina Linguagem de Programação 1.
# Professor: Rogério Alves
# Estagiária: Thalia Souza
# ============================================================================
# Description: Caixa eletrônico simples em Python, utilizando estruturas de controle de fluxo e manipulação de dados.
# Author: Faulkner
# Date: 05/02/2026
# ============================================================================

# ❗Solicitar as 2 senhas de 4 e 8 dígitos para realizar as transações bancárias, nas operações de Saque, Pagamento, Transferência e Depósito.

# Contagem de Operações para Extrato da Conta Corrente
cont_pag_CC=0 
cont_transf_CC=0 
cont_saque_CC=0
cont_dep_CC=0
pag_CC = {'Pagamentos': cont_pag_CC}
pag_CC = {'Pagamentos': cont_pag_CC}
pag_CC = {'Pagamentos': cont_pag_CC}
pag_CC = {'Pagamentos': cont_pag_CC}

# Contagem de Operações para Extrato da Conta Poupança
cont_pag_CP=0 
cont_transf_CP=0 
cont_saque_CP=0
cont_dep_CP=0
pag_CP = {'Pagamentos': cont_pag_CP}


pwd4dig = "1234"  # Senha de acesso ao caixa eletrônico
pwd8dig = "12345678"  # Senha para transações bancárias

saldo_corrente = 4000.00  # Saldo inicial da conta corrente
saldo_poupanca = 5000.00  # Saldo inicial da conta poupança



flag=False

while flag != True:
    print("")
    print("   Caixa Eletrônico 24 Horas   ")
    print("")
    print(" 1. Saldo Conta Corrente")
    print(" 2. Extrato Conta Corrente")
    print(" 3. Pagamentos Conta Corrente") # Solicitar 2 senhas.
    print(" 4. Transferências Conta Corrente") # Solicitar 2 senhas.
    print(" 5. Saque Conta Corrente") # Solicitar 2 senhas.
    print(" 6. Deposito Conta Corrente") # Solicitar 2 senhas.
    print(" 7. Saldo Conta Poupança")
    print(" 8. Extrato Conta Poupança")
    print(" 9. Pagamentos Conta Poupança") # Solicitar 2 senhas.
    print("10. Transferências Conta Poupança") # Solicitar 2 senhas.
    print("11. Saque Conta Poupança") # Solicitar 2 senhas.
    print("12. Deposito Conta Poupança") # Solicitar 2 senhas.
    print("")
    print(" 0. Encerrar Sessão")
    print("")
    opc = int(input("> "))

    if opc == 1:
        print("")
        #print(f"Saldo Disponível Conta Corrente: R$ {saldo_corrente:.2f}")
        print("Saldo Disponível na Conta Corrente:")
        print("")
        print(f"R$: {saldo_corrente:.2f}")
        print("")

    if opc == 2:
        print("")
        print(" EXTRATO CONTA CORRENTE ")
        print("")
        print(f"Saldo Conta Corrente: R$: {saldo_corrente:.2f}")
        print("")
        print("Operações Realizadas Conta Corrente: ", extCC)
        print("")

    if opc == 3:
        extCC += 1
        print("")

    if opc == 4:
        extCC += 1
        print("")

    if opc == 5:
        extCC += 1
        print("")

    if opc == 6:
        extCC += 1
        print("")

    if opc == 7:
        print("")

    if opc == 8:
        print("Saldo Disponível na Conta Poupança:")
        print("")
        print(f"R$: {saldo_poupanca:.2f}")
        print("")
        print("Operações Realizadas na Conta Poupança: ", extCP)

    if opc == 9:
        extCP += 1
        print("")
    
    if opc == 10:
        extCP += 1
        print("")
    
    if opc == 11:
        extCP += 1
        print("")

    if opc == 12:
        extCP += 1
        print("")
        
    if opc == 0:
        flag = True
        break


