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

turma_janeiro=[
    {"nome":"Joabe","score":10},
    {"nome":"Joabe","score":4},
    {"nome":"Luiza","score":8},
    {"nome":"David","score":5}
    ]
turma_fevereiro=[
    {"nome":"Abigail","score":6},
    {"nome":"Joao","score":9},
    {"nome":"Pedro","score":8},
    {"nome":"Luiz","score":7}
    ]
turma_abril=[
    {"nome":"Antonio","score":7},
    {"nome":"Marcos","score":2},
    {"nome":"Lara","score":10},
    {"nome":"Samanta","score":4}
    ]

aprovados=[]
reprovados=[]

def lista_aprovados_e_reprovados(students):
    for student in students:
        score=student["score"]
        if score <5:
            reprovados.append(student)
        else:
            aprovados.append(student)

print(lista_aprovados_e_reprovados(turma_janeiro))
print(lista_aprovados_e_reprovados(turma_fevereiro))
print(lista_aprovados_e_reprovados(turma_abril))