# Exemplo básico
frutas = "maçã,banana,uva"
lista_frutas = frutas.split(',')
print(lista_frutas)  # ['maçã', 'banana', 'uva']

print()
print("------------------------------------------")
print()

# Exemplo com espaços (melhor prática)
dados = "nome, idade, cidade"
lista_limpa = [item.strip() for item in dados.split(',')]
print(lista_limpa)  # ['nome', 'idade', 'cidade']

##### EXPLICAÇÃO DO COMBO:  lista_limpa = [item.strip() for item in dados.split(',')]
#
# Esse exemplo é um "combo" clássico de manipulação de dados em Python. 
# Ele combina três conceitos fundamentais para limpar informações vindas de arquivos ou entradas de usuários:
# 
# 1. O Método .split(',') 
# É o ponto de partida. Ele pega a string original e a transforma em uma lista toda vez que encontra uma vírgula.
# O problema: Como a sua string original tem espaços após as vírgulas (", "), o .split(',') sozinho geraria itens "sujos": ['nome', ' idade', ' cidade']. Repare nos espaços antes de "idade" e "cidade".
# 
# 2. O Método .strip()
# Este método remove todos os espaços em branco (espaços, tabs, quebras de linha) que estão no início ou no fim de uma string. Ele não mexe no que está no meio das palavras.
# " idade".strip() vira "idade".
# 
# 3. List Comprehension (Compreensão de Lista)
# É essa estrutura [item... for item in...]. É uma forma elegante e rápida (mais performática que um for comum) de criar uma nova lista transformando cada elemento de uma lista antiga.
# A leitura "humana" do código seria: 
# "Para cada item gerado pelo split, aplique um strip e guarde o resultado em uma nova lista chamada lista_limpa."
# 
# Por que fazer assim?
# Se você estivesse lendo um arquivo CSV, por exemplo, é comum que os dados venham com espaços irregulares.
# Essa linha garante que você terá apenas o texto "puro" para comparar ou salvar no banco de dados.