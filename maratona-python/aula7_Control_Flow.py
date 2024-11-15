def unlock_adult_movies(username, age):
    if age >= 18:
        msg= f"{username} PODE assistir filmes adultos"
    else:
        msg= f"{username} NÃO pode assistir filmes adultos"
    return msg

print("==================================================")
print() ## QUEBRA DE LINHA
print(unlock_adult_movies("John", 12))
print() ## QUEBRA DE LINHA
print(unlock_adult_movies("Steve", 18))
print() ## QUEBRA DE LINHA
print(unlock_adult_movies("Bob", 25))
print() ## QUEBRA DE LINHA
print(unlock_adult_movies("James", 10))
print() ## QUEBRA DE LINHA
print(unlock_adult_movies("Alexssander", 11))
print() ## QUEBRA DE LINHA
print(unlock_adult_movies("Dylan", 13))
print() ## QUEBRA DE LINHA
print("==================================================")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print() ## QUEBRA DE LINHA
username=input("Nome de Usuário:")
senha=input("Senha:")

## INFORMAÇÔES ARMAZENADAS DENTRO DO BANCO DE DADOS ##
senhaStoredBD="123abc"
usuarioStoredBD="admin"
#####################################################

def verificar_senha(username, senha):
    if username != usuarioStoredBD and senha != senhaStoaredBD:
        msg="Falha no Login"
    else:
        msg="Login com Sucesso"
    return msg


print() ## QUEBRA DE LINHA
print(verificar_senha(username, senha))
print() ## QUEBRA DE LINHA