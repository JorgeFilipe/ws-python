# formula=
import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = int(input("Enter the value of x of point A: "))
x2 = int(input("Enter the value of y of point A: "))
y1 = int(input("Enter the value of x of point B: "))
y2 = int(input("Enter the value of y of point B: "))

pontoA=(x1, y1)
pontoB=(x2, y2)

distancia = calcular_distancia(pontoA[0], pontoA[1], pontoB[0], pontoB[1])

print(f"A distancia entre os pontos A e B é: {distancia}")