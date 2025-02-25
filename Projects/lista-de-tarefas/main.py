#### Testar funcionalidade

import datetime

# Lista vazia para armazenar as tarefas
lista_de_tarefas = []

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite uma nova tarefa: ")
    data = input("Digite a data de conclusão (DD/MM/AAAA): ")
    data_formatada = datetime.datetime.strptime(data, '%d/%m/%Y').date()
    lista_de_tarefas.append({"tarefa": tarefa, "data": data_formatada})
    print("Tarefa adicionada com sucesso!")

# Função para visualizar todas as tarefas na lista
def visualizar_tarefas():
    if len(lista_de_tarefas) == 0:
        print("A lista de tarefas está vazia.")
    else:
        for tarefa in lista_de_tarefas:
            print("Tarefa:", tarefa["tarefa"])
            print("Data de conclusão:", tarefa["data"].strftime("%d/%m/%Y"))
            print("-" * 20)

# Função para atualizar uma tarefa existente na lista
def atualizar_tarefa():
    if len(lista_de_tarefas) == 0:
        print("A lista de tarefas está vazia.")
    else:
        tarefa_atual = input("Digite o nome da tarefa que deseja atualizar: ")
        for tarefa in lista_de_tarefas:
            if tarefa_atual == tarefa["tarefa"]:
                nova_tarefa = input("Digite a nova tarefa: ")
                nova_data = input("Digite a nova data de conclusão (DD/MM/AAAA): ")
                nova_data_formatada = datetime.datetime.strptime(nova_data, '%d/%m/%Y').date()
                tarefa["tarefa"] = nova_tarefa
                tarefa["data"] = nova_data_formatada
                print("Tarefa atualizada com sucesso!")
                return
        print("Tarefa não encontrada na lista.")

# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar nova tarefa")
    print("2. Visualizar todas as tarefas")
    print("3. Atualizar uma tarefa existente")
    print("4. Sair do programa")
    opcao = input("> ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        visualizar_tarefas()
    elif opcao == "3":
        atualizar_tarefa()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

print("Programa encerrado.")
