import calc # importa o module

# Desta forma podemos usar a função diretamente, sem passar tbm o nome do module.
from calc import soma

 # pode definir um "nome local" para a função importada.
from calc import multiplicacao as mult

print()
print(soma(10, 20)) # Funciona pois especifica a função na importação
print(calc.sub(10, 20))
print(mult(10, 20)) # Originalmente a função se chama 'multiplicacao'
print(calc.div(10, 20))
print()
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
print()

# Um módulo é um single file
# Já um package é uma coleção de módulos 
# pypi.org é um site que lista pacotes criados pela comunidade