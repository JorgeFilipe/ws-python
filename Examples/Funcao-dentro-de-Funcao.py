def soma(a, b):
    valorsoma = a /+ b
    return valorsoma

def multiplicacao(a, b):
    valormultiplicacao = a * b
    return valormultiplicacao

a1 = 2
a2 = 3
a3 = 4
a5 = 5

print()
print(multiplicacao(a1,soma(a1,a3))) # Passando função dentro de função, funciona.
temp = soma(a1,a3)
print()
print(multiplicacao(a1,temp)) # Fazendo separado para comprovar que funciona, passando função dentro de função.
print()
print("------------------")

def add_protocolo(url):
    formatado="https://"+url
    return formatado

def add_dot_com(url):
    formatando=url+".com"
    return formatando

url="google"

print()
print(add_protocolo(add_dot_com(url))) # Testando Função dentro de Função usando uma váriável
print()

print("------------------")

# TESTANDO SE AS ORDENS DAS FUNÇÕES AFETAM O RESULTADO COM STRINGS
def first(a):
    temp="Add 1st, "+a
    return temp
def second(a):
    temp="Add 2nd, "+a
    return temp
def third(a):
    temp="Add 3rd, "+a
    return temp
def fourth(a):
    temp="Add 4th, "+a
    return temp

# TESTANDO SE AS ORDENS DAS FUNÇÕES AFETAM O RESULTADO COM INTEIROS
def mult1(val):
    resp=val*1
    return resp
def mult2(val):
    resp=val*2
    return resp
def mult3(val):
    resp=val*3
    return resp
def mult4(val):
    resp=val*4
    return resp

valor=2
a="Winner"

print()

print(fourth(second(first(third(a))))) # A Ordem de execução é da função mais próxima da variável/valor para a mais longe(da direita para a esquerda): 
#(4° em último)<-(2° em terceiro)<-(1° em segundo)<-(3° executou primeiro)

print()

print(mult4(mult1(mult2(mult3(valor))))) # A Ordem de execução é da função mais próxima da variável/valor para a mais longe(da direita para a esquerda):
# primeiro executou a função 3° (2x3=6) que é a mais próxima do valor, depois a função 2°(6x2=12), depois a função 1° (12x1=12) e por último a função 4° (12x4=48) que é a mais longe do valor.

print()

print(mult1(mult3(mult4(mult2(valor-1))))) # A Ordem de execução é da função mais próxima da variável/valor para a mais longe(da direita para a esquerda):
# primeiro executou a função 2° (1x2=2) que é a mais próxima do valor, depois a função 4°(2x4=8), depois a função 3° (8x3=24) e por último a função 1° (24x1=24) que é a mais longe do valor.

print()