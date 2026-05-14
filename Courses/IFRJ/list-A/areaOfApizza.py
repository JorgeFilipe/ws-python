## Consider radius equal (pi=3.14)
## Formula: A=pi*r²

import math

pi=3.14
radius=float(input("Enter the value of the pizza radius: "))

area = pi * math.pow(radius, 2)

print(f"Area of pizza: {area}m²")