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

####### Contagem de Operações para Extrato da Conta Corrente
pag_CC = 0
transf_CC = 0
saque_CC = 0
dep_CC = 0
extrato_CC = [{'Pagamentos': pag_CC,'Transferências': transf_CC, 'Saques': saque_CC,'Depósitos': dep_CC}]
############################################################

####### Contagem de Operações para Extrato da Conta Poupança
pag_CP = 0
transf_CP = 0
saque_CP = 0
dep_CP = 0
extrato_CP = [{'Pagamentos': pag_CP,'Transferências': transf_CP, 'Saques': saque_CP,'Depósitos': dep_CP}]
##############################################################

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
    opc = int(input(">> "))

    if opc == 1: # SALDO CONTA CORRENTE
        print()
        print("┌──────────────────────────────────────┐")
        print("│ SALDO DISPONIVEL NA CONTA CORRENTE   │")
        print("├─────┬────────────────────────────────┤")
        print(f"│  R$ │  {saldo_corrente:.2f}         ")
        print("└─────┴────────────────────────────────┘")
        print()# </br>

    if opc == 2: # EXTRATO CONTA CORRENTE
        print("")
        print(" EXTRATO CONTA CORRENTE ")
        print("")
        print(f"Saldo Conta Corrente: R$: {saldo_corrente:.2f}")
        print("")
        print("Operações Realizadas Conta Corrente: ")
        print("-------------------------------------")
        print(f"-- Pagamentos: {extrato_CC[0]['Pagamentos']}")
        print(f"-- Transferências: {extrato_CC[0]['Transferências']}")
        print(f"-- Saques: {extrato_CC[0]['Saques']}")
        print(f"-- Depósitos: {extrato_CC[0]['Depósitos']}")
        print("")

    if opc == 3: # PAGAMENTOS CONTA CORRENTE
        pag_CC+=1
        extrato_CC[0]['Pagamentos'] = pag_CC
        print("")

    if opc == 4: # TRANSFERÊNCIAS CONTA CORRENTE
        transf_CC += 1
        extrato_CC[0]['Transferências'] = transf_CC
        print("")

    if opc == 5: # SAQUE CONTA CORRENTE
        saque_CC += 1
        extrato_CC[0]['Saques'] = saque_CC
        print("")

    if opc == 6: # DEPÓSITO CONTA CORRENTE
        dep_CC += 1
        extrato_CC[0]['Depósitos'] = dep_CC
        print("")

    if opc == 7: # SALDO CONTA POUPANÇA
        print()
        print("┌──────────────────────────────────────┐")
        print("│ SALDO DISPONIVEL NA CONTA POUPANÇA   │")
        print("├─────┬────────────────────────────────┤")
        print(f"│  R$ │  {saldo_poupanca:.2f}         ")
        print("└─────┴────────────────────────────────┘")
        print()# </br>

    if opc == 8: # EXTRATO CONTA POUPANÇA
        print("")
        print(" EXTRATO CONTA POUPANÇA ")
        print("")
        print(f"Saldo Conta Poupança: R$: {saldo_poupanca:.2f}")
        print("")
        print("Operações Realizadas Conta Poupança: ")
        print("-------------------------------------")
        print(f"-- Pagamentos: {extrato_CP[0]['Pagamentos']}")
        print(f"-- Transferências: {extrato_CP[0]['Transferências']}")
        print(f"-- Saques: {extrato_CP[0]['Saques']}")
        print(f"-- Depósitos: {extrato_CP[0]['Depósitos']}")
        print("")

    if opc == 9: # PAGAMENTOS CONTA POUPANÇA
        pag_CP += 1
        extrato_CP[0]['Pagamentos'] = pag_CP
        print("")
    
    if opc == 10: # TRANSFERÊNCIAS CONTA POUPANÇA
        transf_CP += 1
        extrato_CP[0]['Transferências'] = transf_CP
        print("")
    
    if opc == 11: # SAQUE CONTA POUPANÇA
        saque_CP += 1
        extrato_CP[0]['Saques'] = saque_CP
        print("")

    if opc == 12: # DEPÓSITO CONTA POUPANÇA
        dep_CP += 1
        extrato_CP[0]['Depósitos'] = dep_CP
        print("")
        
    if opc == 0:
        print("┌───────────────────────────────────────────┐")
        print("│                                           │")
        print("│         ▲                                 │")
        print("│        / \                                │")
        print("│       /   \     SESSÃO ENCERRADA!         │")
        print("│      /  █  \                              │")
        print("│     /   ▄   \   RETIRE O CARTÃO!          │")
        print("│    /_________\                            │") 
        print("│                                           │")
        print("└───────────────────────────────────────────┘")
        print()
        flag = True
        break


