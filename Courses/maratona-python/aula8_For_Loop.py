#students=[
#    {"nome":"Joabe","score":1},
#    {"nome":"Luiza","score":2},
#    {"nome":"David","score":3},
#    {"nome":"Suzan","score":4},
#    {"nome":"Diego","score":5},
#    {"nome":"Clara","score":6},
#    {"nome":"Bruno","score":7},
#    {"nome":"Joana","score":5},
#    {"nome":"Pedro","score":9},
#    {"nome":"Jorge","score":10}
#    ]
#
#### Listagem de todos os elementos do Vetor
#for student in students:
#    print(f"O aluno(a) {student['nome']} tem nota {student['score']}")
#
#
#print()
#
#### Validação de Aprovados ou Reprovados
#for student in students:
#    score=student['score']
#    if score <5:
#        print(f"O aluno(a) {student['nome']} está REPROVADO")
#    else:
#        print(f"O aluno(a) {student['nome']} está APROVADO")
#
#print()
#
#### Preenchendo outra lista dentro do Loop
#aprovados=[]
#reprovados=[]
#
#for student in students:
#    score=student['score']
#    if score <5:
#        reprovados.append(student)
#    else:
#        aprovados.append(student)
#
#print("Aprovados")
#print(aprovados)
#print("Reprovados")
#print(reprovados)
#
#
#print()
#

#### Utilizando Loop em Functions

#turma_janeiro=[
#    {"nome":"Joabe","score":10},
#    {"nome":"Joabe","score":4},
#    {"nome":"Luiza","score":8},
#    {"nome":"David","score":5}
#    ]
#turma_fevereiro=[
#    {"nome":"Abigail","score":6},
#    {"nome":"Joao","score":9},
#    {"nome":"Pedro","score":8},
#    {"nome":"Luiz","score":7}
#    ]
#turma_abril=[
#    {"nome":"Antonio","score":7},
#    {"nome":"Marcos","score":2},
#    {"nome":"Lara","score":10},
#    {"nome":"Samanta","score":4}
#    ]
#
#aprovados=[]
#reprovados=[]
#
#def lista_aprovados_e_reprovados(students):
#    for student in students:
#        score=student["score"]
#        if score <5:
#            reprovados.append(student)
#        else:
#            aprovados.append(student)
#
#print(lista_aprovados_e_reprovados(turma_janeiro))
#print(lista_aprovados_e_reprovados(turma_fevereiro))
#print(lista_aprovados_e_reprovados(turma_abril))


## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## %%%%%%%%%%%       REFAZENDO ESSA AULA  24/03/2026        %%%%%%%%%%%%%%%%%%%%
## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

students = [
    {"name": "bruno", "score": 50},
    {"name":"marcos", "score": 40},
    {"name": "luiza", "score": 70},
    {"name": "jorge", "score": 80},
    {"name": "pedro", "score":99},
    {"name": "lara", "score": 10},
    {"name": "henrique","score": 51},
    {"name": "mr robot", "score": 98},
    {"name":"super man", "score": 60},
    {"name": "vivi", "score": 20},
    {"name": "fernando", "score": 81},
    {"name": "ju", "score":88},
    {"name": "carlos", "score": 55},
    {"name": "noah","score": 11},
    {"name": "tiago", "score": 50}
]

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

print()
print("Descobrindo o total de elementos na Dict")
print("len(students) = ", len(students))
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
print()
for i in [7,10,5]:
    print(i)
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

for student in students: # LISTANDO TODOS OS ITENS
    print(student)
    print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

print()
for student in students: # LISTANDO TODOS OS NOMES DOS ALUNOS
    print(student["name"])
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

print()
for student in students: # LISTANDO NOMES E NOTAS DOS ALUNOS
    print(f" O aluno(a) {student['name']} tem nota {student['score']}")
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

print()
for student in students: # UTILIZANDO CONDICIONAL DENTRO DO LOOP
    score = student['score']
    if score < 50:
        print(f" O aluno(a) {student['name']} está REPROVADO ❌")
    else:
        print(f" O aluno(a) {student['name']} está APROVADO ✅")
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

aprovados = []
reprovados = []
print()
for student in students: # ADICIONANDO APROVADOS E REPROVADOS EM UMA NOVA LISTA DENTRO DO LOOP
    score = student['score']
    if score < 50:
        reprovados.append(student)
    else:
        aprovados.append(student)
print()
print("APROVADOS")
print(aprovados)
print()
print("REPROVADOS")
print(reprovados)
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

# ADICIONANDO O LOOP DENTRO DE UMA FUNÇÃO PARA USAR EM OUTRAS LISTAS
turma_janeiro = [
    {"name": "Kayo", "score": 88},
    {"name":"John", "score": 49},
    {"name": "Luis", "score": 14},
    {"name": "James", "score": 22},
    {"name": "Piter", "score":10},
    {"name": "Lara", "score": 1},
    {"name": "Henry","score": 40},
    {"name": "Andrew", "score": 10},
    {"name":"Gary", "score": 8},
    {"name": "Julliet", "score": 3},
    {"name": "Ferdinand", "score": 7},
    {"name": "Antony", "score":36},
    {"name": "Charles", "score": 99},
    {"name": "Noah","score": 47},
    {"name": "Tymothy", "score": 36}
]

turma_fevereiro = [
    {"name": "Joaquim", "score": 77},
    {"name":"Severino", "score": 78},
    {"name": "Luzia", "score": 79},
    {"name": "Casemiro", "score": 80},
    {"name": "Junim", "score":49},
    {"name": "Lara", "score": 48},
    {"name": "Henry","score": 47},
    {"name": "Andrew", "score": 46}
]

aprovados = []
reprovados = []
def list_aprovados_reprovados(list):
    for student in list:
        score = student['score']
        if score < 50:
            reprovados.append(student)
        else:
            aprovados.append(student)

list_aprovados_reprovados(turma_janeiro) #AQUI ELE EXECUTA A FUNÇÃO E SALVA OS APROVADOS E REPROVADOS DA TURMA DE JANEIRO EM LISTAS SEPARADAS
print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
print("◘◘  ")
print("◘◘  TURMA DE JANEIRO 2026")
print("◘◘ ")
print("◘◘◘◘ PRINTANDO TODAS A LISTA DE APROVADOS E REPROVADOS ◘◘◘◘")
print()
print("---- APROVADOS")# LISTANDO TODA A LISTA DE APROVADOS DA TURMA DE JANEIRO
print(aprovados)
print()
print("---- REPROVADOS")# LISTANDO TODA A LISTA DE REPROVADOS DA TURMA DE JANEIRO
print(reprovados)
print()
print("◘◘◘◘ APENAS OS NOMES ◘◘◘◘")
print()
print("APROVADOS ✅")
for student in aprovados: # LISTANDO APENAS OS NOMES DOS REPROVADOS E APROVADOS DA TURMA DE JANEIRO
    print(student['name'])
print()
print("REPROVADOS ❌")
for student in reprovados: # LISTANDO APENAS OS NOMES DOS REPROVADOS E APROVADOS DA TURMA DE JANEIRO
    print(student['name'])
print()
print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
print()
aprovados = [] # ZERANDO A LISTA PARA USAR NA TURMA DE FEVEREIRO
reprovados = [] # ZERANDO A LISTA PARA USAR NA TURMA DE FEVEREIRO
print()
list_aprovados_reprovados(turma_fevereiro) #AQUI ELE EXECUTA A FUNÇÃO E SALVA OS APROVADOS E REPROVADOS DA TURMA DE FEVEREIRO EM LISTAS SEPARADAS
print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
print(" TURMA DE FEVEREIRO 2026")
print()
print("♠♠♠♠ PRINTANDO TODAS A LISTA DE APROVADOS E REPROVADOS ♠♠♠♠")
print()
print("---- APROVADOS")# LISTANDO TODA A LISTA DE APROVADOS DA TURMA DE FEVEREIRO
print(aprovados)
print()
print("---- REPROVADOS")# LISTANDO TODA A LISTA DE REPROVADOS DA TURMA DE FEVEREIRO
print(reprovados)
print()
print("♠♠♠♠ APENAS OS NOMES ♠♠♠♠")
print()
print("APROVADOS ✅")
for student in aprovados: # LISTANDO APENAS OS NOMES DOS REPROVADOS E APROVADOS DA TURMA DE FEVEREIRO
    print(student['name'])
print()
print("REPROVADOS ❌")
for student in reprovados: # LISTANDO APENAS OS NOMES DOS REPROVADOS E APROVADOS DA TURMA DE FEVEREIRO
    print(student['name'])
print()
print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
print()
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
print()
print("USANDO O BRAKE e CONTINUE PARA CONTROLAR O LOOP")
print()
sequence=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in sequence:
    print(i)
    if i==4:
        print("loop pausado")
        break
print()

for a in sequence:
    #mod=a%2 # Módulo
    if a%2==0:
        print("O numero: ",a," é Par")
    else:
        continue # Se cair um numero impar ele continua sem sair do loop

print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

# 1. verificar pelo username se ele é VIP (criar uma list com os users VIPs e buscar a cada login)
# 2. pesquisar em uma lista se o token do user está registrado (criar lista com tokens)
# *#