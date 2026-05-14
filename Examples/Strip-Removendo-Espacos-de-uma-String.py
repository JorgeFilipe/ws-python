
texto = "Olá, Mundo! Python"
print("Texto com Espaços: ", texto)
# Remove todos os espaços
texto_sem_espacos = texto.replace(" ", "")
print("Texto sem Espaços: ", texto_sem_espacos)  # Resultado: Olá,Mundo!Python

print()
print("-----------------------------------------------------------------------")
print()

print("Aqui estão as variações para cenários específicos:")
print("Remover todos os espaços (entre palavras): Use string.replace(" ", "").")
print("Remover espaços no início e no final: Use string.strip().")
print("Remover apenas no início (esquerda): Use string.lstrip().")
print("Remover apenas no final (direita): Use string.rstrip().")
texto_com_muitos_espacos="Ei! Você Aí! Pare Agora Mesmo! Em Nome da Lei!"
texto_espaco_no_inicio_e_fim=" <-tem um espaço aqui no inicio | e aqui também no final-> "
texto_espaco_no_inicio=" <-tem um espaço aqui no inicio."
texto_espaco_no_fim="tem um espaço aqui no final-> "
print()
print(texto_com_muitos_espacos)
print(texto_com_muitos_espacos.replace(" ",""))
print()
print(texto_espaco_no_inicio_e_fim)
print(texto_espaco_no_inicio_e_fim.strip()) # Remover espaços no início e no final: Use string.strip()
print()
print(texto_espaco_no_inicio)
print(texto_espaco_no_inicio.lstrip()) # Remover apenas no início (esquerda): Use string.lstrip()
print()
print(texto_espaco_no_fim)
print(texto_espaco_no_fim.rstrip()) # Remover apenas no final (direita): Use string.rstrip()
print()