texto1="Python"
texto2="a tuple of prefixes"
texto3="Python is amazing"

print(texto1.startswith(("Py"))) # Retorna TRUE pq o texto começa com "Py".

print(texto2.startswith(("at", "a"))) # Retorna TRUE pq o texto começa OU com "at" OU com "a".

print(texto3.startswith(("is", "7"))) # Retorna FALSE pq o texto não começa com os valores passados.