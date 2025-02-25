## DOCUMENTAÇÃO:
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict


#product = {
#  "id":462672524,
#  "prod_name":"Hard Disk 1TB",
#  "brand":"Western Digital",
#  "stock":14,
#  "inventoried":True,
#  "price":26.80,
#  "comments":None,
#  "sold_in":["Canada", "USA", "Brazil", "South Africa"]
#}
# Um Dict comporta vários tipos de dados. Incluindo além dos tipos de dados, outros Dicts, arrays e etc.

################################## Exibindo o tipo da variável:
#print(type(product))

############################# Exibindo todos os elementos do Dictionaire:
#print(product)

############################# Exibindo item de dentro do Dict:
#print(product["brand"])
#print(product["id"])
#print(product["prod_name"])
#print(product["price"])
#print(product["sold_in"])

############################# OUTROS EXEMPLOS:


############################# Adicionando valores ao Dictionaire
#d = {"vazio":None}
#print("Antes: ",d);
#
#d["centésimo"] = 100
#d["porcentagem"] = "150%"
#d["decimal"] = 0.9999
#d["mil"] = 1000
#d["unidade"] = 1
#d["alfabeto"] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"#,"s","t","u","v","x","w","y","z"]
#
#print("\nDepois: ",d);


############################# Removendo valores ao Dictionaire
#car = {
#  "chassi":"1R23WF96A50BNK5L1",
#  "doors":4,
#  "tipo":"sedã",
#  "trunk":"1.8 litros",
#  "motor":"122 cv",
#  "color":"silver"
#}
#print("Antes de Deletar:\n",car)
## Remove d[key] from d. Raises a KeyError if key is not in the map.
#del car["trunk"]
#print("\nDepois de Deletar:\n",car)
#

############################# Validação Lógica:
#hud={
#  "life":"100%",
#  "stamina":"80%",
#  "mana":"90%"
#}
#print("life" in hud)
#print("stamina" in hud)
#print("mana" in hud)
#print("power" in hud)
#
#print("\n")
#
#print("life" not in hud)
#print("streight" not in hud)
#print("stamina" not in hud)
#print("mana" not in hud)


############################# Inserindo várias dicts a um Vetor
alunos = [
  {"nome":"João","idade":20,"id":"G5A01R","notas":[10,7.5,9,6]},
  {"nome":"Maria","idade":21,"id":"9DW50F","notas":[9,8,7,6]},
  {"nome":"Kaio","idade":22,"id":"M5JY89","notas":[5.5,8.4,9,5.7]},
  {"nome":"Ester","idade":23,"id":"K55GH1","notas":[10,10.8,10,9]},
  {"nome":"Diego","idade":24,"id":"V05E6Q","notas":[7.3,8.6,9,8]},
  {"nome":"Ana","idade":25,"id":"T9Q8WDL","notas":[4.4,10,10,10]},
]

# O comando: print(alunos[0]["nome"]) busca o objeto (dict) na posição zero do array, e exibe o que foi passado no próximo parâmetro, neste caso a variável nome dentro da objeto dict.

# Outros exemplos:

print(alunos[2]["notas"])
# printando em linha

# Listando as Idades dos Alunos
#for aluno in alunos:{
#  print(aluno["nome"],"tem",aluno["idade"],"anos")
#}
##
#print("\n")
#
## Listando a nota apenas do 1ºBimestre
#for aluno in alunos:{
#  print(aluno["nome"],"nota do 1ºBim. :",aluno["notas"][0])
#}
#
#print("\n")
#
### Média Aritmética das Notas dos Alunos
#for aluno in alunos:{
#  print(aluno["nome"],"média final:",(aluno["notas"][0]+aluno["notas"]#[1]+aluno["notas"][2]+aluno["notas"][3])/4)
#}
