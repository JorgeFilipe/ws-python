#  Jogo da Forca
# Implemente um jogo da forca em que o programa escolhe uma palavra aleatória de uma lista de palavras e o usuário deve adivinhar a palavra, fornecendo letras em cada tentativa.


# 
# x. Lista com várias palavras
# x. Perguntar ao usuário qual a letra
# x. Ler resposta do usuário
# x. verificar letras na palavra 
# x. Contador de erros
# x. Contador de chances(7 chances: Cabeça; corpo; braço direito; braço esquerdo; perna direirta; perna esquerda; e o último é o enforcamento;)
# x. Exibir letras erradas já informadas pelo usuário
# x. Percorrer vetor e comparar letra informada com a letra/valor dentro de cada indice
# x. 
# x. 
# x. 
# x. 
# x. 
# 
# Array com várias dicts sendo as dicts letras que formam palavras por exemplo[ ]
# palavra["P","A","L","A","V","R","A"]
# 
#############################
#
# palavras = [
#   {"queijo":["q","u","e","i","j","o"]},
#   {"musica":["m","u","s","i","c","a"]},
#   {"artropode":["a","r","t","r","o","p","o","d","e"]},
#   {"constitucional":["c","o","n","s","t","i","t","u","c","i","o","n","a","l"]},
#   {"ar":["a","r"]},
#   {"notas":["n","o","t","a","s"]},
# ]
#
#############################
#
# queijo = ["q","u","e","i","j","o"]
# musica = ["m","u","s","i","c","a"]
# artropode = ["a","r","t","r","o","p","o","d","e"]
# ar = ["a","r"]
# notas = ["n","o","t","a","s"]
#
# palavras = [queijo, musica, artropode, ar, notas] 
# 
#############################
#
#  palavras = [
#    ["q","u","e","i","j","o"],
#    ["m","u","s","i","c","a"],
#    ["a","r","t","r","o","p","o","d","e"],
#    ["a","r"],
#    ["n","o","t","a","s"]
#]
#
#valor_usuario = input("Digite um valor: ")
#
#for palavra in palavras:
#    for letra in palavra:
#        if letra == valor_usuario:
#            print(f"A letra '{valor_usuario}' foi encontrada na palavra {palavra}.")
##


#================= TESTE ======================

#cont=0
#acerto=0

#palavras = ["a","r"]  <<-- Voltar para este exemplo, pois o jogo vai correr com apenas uma lista que virá aleatória do [.Random()]

#palavras = [
#    ["q","u","e","i","j","o"],
#    ["m","u","s","i","c","a"],
#    ["a","r","t","r","o","p","o","d","e"],
#    ["a","r"],
#    ["n","o","t","a","s"]
#]

#valor_usuario = input("Digite um valor: ")

#for palavra in palavras:
#    for letra in palavra:
#        if letra == valor_usuario:
#            print(f"A letra '{valor_usuario}' foi encontrada na palavra {palavra}.")
#
#
#print()
#print("Contador: ",cont)
#print("Acertos: ",acerto)

#=============== REMOVENDO LETRAS  =============================================================
valor_usuario = input("Insira uma letra: ");   
            
palavra = ["p","a","l","a","v","r","a"]

for letra in palavra:
    if letra == valor_usuario:
        print(f"A letra '{valor_usuario}' foi encontrada na palavra {palavra}.")
        palavra.remove(letra)
        break
            
print(f"palavra {palavra}")      

#================================================================================================
            
#  WHILE (chances == 15) {
#         
#    
#  } 
# 
# 
# 
# 
# 
# 
# 
# #

