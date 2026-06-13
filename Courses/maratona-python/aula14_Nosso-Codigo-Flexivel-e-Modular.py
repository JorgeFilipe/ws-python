#######################################################
### IMPORTANDO O MÓDULO QUE CRIEI
from infojobs import scrapping_infojobs

print()#Breakline

jobs_python_infojobs=scrapping_infojobs("https://www.infojobs.com.br/empregos.aspx?palabra=Python")
print(jobs_python_infojobs)

print()#Breakline
print("-------------------------------------------------------------------")
print()#Breakline

jobs_javascript_infojobs=scrapping_infojobs("https://www.infojobs.com.br/empregos.aspx?palabra=Java+Script")
print(jobs_javascript_infojobs)

print()#Breakline
print("-------------------------------------------------------------------")
print()#Breakline

jobs_java_infojobs=scrapping_infojobs("https://www.infojobs.com.br/empregos.aspx?palabra=java")
print(jobs_java_infojobs)

print()#Breakline