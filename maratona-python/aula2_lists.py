#
# Materiais de Apoio:
#
# https://www.w3schools.com/python/python_lists.asp
#
# https://www.w3schools.com/python/python_tuples.asp
# 
# 


# Estrutura do array:
cars = ["Volvo", "Mazda", "BMW", "Dodge", "Ford"]

# Exibindo o valor do índice:
print(cars[3])

# O array comporta tipos diferentes de dados:
crazy = [10, "Cavalo", False, 488, "Chá", "!#$%@", "1597532", 9731, "Hospital", 51, True, 000, "753"]

# Exibindo o valor contido no índice:
print(crazy[10])

# há o recurso de inverter o array digitando índices negativos,
# neste caso o conta de forma inversa,
# o último índice se torna -1, o penúltimo -2, antepenúltimo -3,
# e assim por diante.
# array normal = [ "a" indice = 0 , "b" indice = 1 , "c" indice = 2]
# array inverso = [ "a" indice = -3 , "b" indice = -2 , "c" indice = -1]
print(crazy[-4])

# MANIPULANDO O ÚLTIMO ELEMENTO DO ARRAY
# O último elemento de uma lista sempre é o -1, ou seja arrayname[-1].
# Por exemplo uma lista automática de cadastro, onde precisamos manipular o último valor .
estoqueSapatos = ["All-Star","Vans","Olympikus","Nike"]

# https://docs.python.org/3/library/stdtypes.html#list

# Descobrindo o tamanho do array:
print("Tamanho do array 'crazy': ",len(crazy))

# ADICIONANDO VALORES AO ARRAY:
# https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
estoqueSapatos.append("Adidas")
cars.append("Chevrolet")

novo_elemento="Futebol"
crazy.append(novo_elemento)

# O .append(valor) adiciona novos valores a última posição do array.

print()
print("Venha conhecer a nova marca em nossa loja!")
print("Tudo da", estoqueSapatos[-1], "por um preço baixo!")
print()
print("Todos os modelos de veículos da",cars[-1])
print("com desconto no valor de entrada!")
print()
print("Último add:",crazy[-1])
print()

# Removendo o último valor do array
alunos=["Zebulom","Artaxerxes","Salomão","Melquisedeque","Matusalém","Nabucodonosor","Estevão"]
alunos.pop()
print("Array alunos:",alunos)

# Removendo valor pelo valor
alunos.remove("Artaxerxes")
print()
print("Array alunos:",alunos)

# Inserindo valores em um índice desejado:
alunos.insert(0,"Colosenses")
print()
print(">> Inserindo valores em um índice desejado:")
print()
print("Array alunos:",alunos)

cars.insert(3,"Ferrari")
print()
print("Array Cars:",cars)

crazy.insert(6,"Floresta")
print()
print("Array Crazy:",crazy)

# Inverter valores no array
numero=[1,2,3,4,5,6,7,8,9,10]
numero.reverse()
print()
print(numero)

# Criando lista com valores travados (sem a possibilidade de alteração)
# TUPLE é um recurso do Python, que cria uma lista com valores que não podem se alterados, apenas lidos.
# Como o array utiliza colchetes[] o Tuple utiliza o parêntesis()
days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
# Se tentar dar um days.append("valor") irá retornar erro


# VARIFICAÇÕES BOOLEANAS
# in = se o valor está presente no array, retorna True, se não False
print()
print("Apolo" in alunos)
print("Floresta" in crazy)
print("Ford" in cars)

# not in = se o valor está dentro do array retorna False, se não True
print()
print("Apolo" not in alunos)
print("Floresta" not in crazy)
print("Ford" not in cars)
