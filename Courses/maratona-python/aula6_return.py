def printPlus(n1, n2):
  print(n1 + n2)

def returnPlus(n1, n2):
  #total = n1 + n2
  #return total
  return n1 + n2

printResult = printPlus(15, 25) # Não retornará o valor da soma.
returnResult = returnPlus(25, 35) # Retornará o valor da soma.

print(printResult)
print(returnResult)

print(10 + returnResult) 
#print(10 + printResult) # Irá gera um erro pois o retorno da função é apenas a impressão do valor.

print()####################################################

# Under the return
# There is no life
def underReturn(a=0, b=0):
  return a + b
  print("Message")

print(underReturn(15, 15))
# Tudo abaixo do return é ignorado na execução.

print()####################################################

def welcome(nome, email, id):
  msg = f"Olá {nome}! seu email: {email} e ID: {id}"
  return msg

print(
  welcome(1578, "John", "john@email.com")
)
# Na impressão do print acima é possível ver como a função funciona através do positional argument onde cada argumento deve estar na mesma ordem dos parâmetros.

print(
  welcome(id=1578, nome="John", email="john@email.com")
)
# Já utilizando o keyworded, é possível definir para cada argumento um "nome" correspondente aos parâmetros.
