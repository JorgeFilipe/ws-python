#lista_de_urls = [item.strip() for item in urls.split(',')]

#lista_final = [u if u.startswith(("http://", "https://")) else f"https://{u}" for u in lista_de_urls]

list_urls=['google.com', 'icanhazip.com', 'ip-api.com']
lista_nova=[]
for u in list_urls:
    lista_nova.append("https://"+u)# Realiza a "Soma" de strings e armazena como novo item na nova lista.

print()
print("Lista bruta sem o \"https://\"")
print()
print(list_urls)
print()
print("Lista final 'somando string' ou seja 'https://' + item da lista antiga:")
print()
print(lista_nova)
print()
print()