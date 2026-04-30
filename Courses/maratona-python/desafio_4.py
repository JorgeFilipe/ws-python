import requests
import DES4HTTPStatusCodeLib

r=requests.get("https://www.google.com/") ## O Google é um site que tem alta disponibilidade, ou seja, dificilmente fica offline.
print("Status HTTP:", r.status_code) ## O status code 200 é o código de
print(status_code_lib[r.status_code]) ## O status code 200 é o código de "OK", ou seja, a requisição foi bem sucedida.

