## 3. imprima os 100 primeiros números pares. 
num = 1
resto=0

for i in range(100):
    resto=num%2 # o '%' pega o resto da divisão.
    if(resto==0):
        print(num)
    num=num+1
