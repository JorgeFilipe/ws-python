def unlock_adult_movies(username, age):
    if age >= 18:
        msg= f"{username} PODE assistir filmes adultos"
    else:
        msg= f"{username} NÃO pode assistir filmes adultos"
    return msg

print("==================================================")
print()
print(unlock_adult_movies("John", 12))
print()
print(unlock_adult_movies("Steve", 18))
print()
print(unlock_adult_movies("Bob", 25))
print()
print(unlock_adult_movies("James", 10))
print()
print(unlock_adult_movies("Alexssander", 11))
print()
print(unlock_adult_movies("Dylan", 13))
print()
print("==================================================")