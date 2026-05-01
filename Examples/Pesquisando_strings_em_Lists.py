


list_urls=['google', 'icanhazip.com', 'ip-api', 'youtube.com']
for i in list_urls:
    if "." in i in list_urls: # PESQUISA SE DENTRO DO ITEM POSSUI PONTO.
        print()#QUEBRALINHA
        print(i," é uma URL válida! ✅")
    else:
        print()#QUEBRALINHA
        print(i,"é uma URL inválida! ❌")

print()#QUEBRALINHA
print()#QUEBRALINHA

list_words=['asa', 'parede', 'assobio', 'porta', 'asfalto', 'janela', 'assimétrico']
for w in list_words:
    if "as" in w in list_words: # PESQUISA SE DENTRO DO ITEM POSSUI "as".
        print()#QUEBRALINHA
        print(w," é uma palavra que contém \"as\" ✅")
    else:
        print()#QUEBRALINHA
        print(w," é uma palavra que NÃO contém \"as\" ❌")

print()#QUEBRALINHA