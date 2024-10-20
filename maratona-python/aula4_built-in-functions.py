#  Check the documentation in:
#  https://docs.python.org/3/library/functions.html
#
# BUILT-IN FUNCTIONS = Funções Embutidas, ou seja funções que vem por padrão no Python.
#
# Built-in functions exemplos:
print("A maior palavra da lingua portuguesa tem:",len("pneumoultramicroscopicossilicovulcanoconiótico"),"letras")
# A função len() = Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
#pneumoultramicroscopicossilicovulcanoconiótico - descreve indivíduo que possui doença pulmonar causada pela inspiração de cinzas vulcânicas.

print("\n")


# Convertendo Valores:

##### bool() - retorna o valor booleano
# Here are most of the built-in objects considered false:
# • constants defined to be false: None and False.
# • zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# • empty sequences and collections: '', (), [], {}, set(), range(0)
sim=1
nao=0
dict1={"yes":1}
dict2={"no":0}
vazio1=[]
vazio2={}
print(bool(sim)) # True
print(bool(dict1["yes"])) # True
print(bool(dict2["no"])) # False
print(bool(nao)) # False
print(bool(vazio1)) # False
print(bool(vazio2)) # False
#####///////////////////////

print("\n")

###### str() - Converte o valor para string.
print("H"+str(3)+"L"+"L"+str(0), "W"+str(0)+"R"+"L"+"D")


#####///////////////////////

print("\n")

###### int() - converte para inteiro
print("Valor é igual a 3")
print("Valor é igual a", int("3") + 3)

# Bom para situações onde há varreduras em páginas web ou programas de integração, onde temos que fazer um cálculo, porém o valor que foi capturado do HTML de uma página está em tipo texto/string e não em número. Neste caso há como converter para inteiro, float e várias outros tipos.

pi=3.141387536
anoNasc="1998"

print("A idade é:", 2022 - int(anoNasc), "anos")
print((int("4") + 4)/2)
print( int("10") + int("20") + int("30") )
print(int(pi))
print(int(5.5))
print(int(0.9999))
print(int(9*(3/4)))
#####///////////////////////

print("\n")
