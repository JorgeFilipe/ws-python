# Converting degrees Celsius to Fahrenheit
# Formula {x є Z | (x°C * 1.8) + 32 }

def conversion_to_fahrenheit(celsius):
    fahrenheit=((celsius*1.8)+32)
    return fahrenheit

print()
celsius = int(input("Enter the temperature value in degrees Celsius: "))
print()
print(f"{celsius}°C in Fahrenheit is: ",conversion_to_fahrenheit(celsius),"°F")
print()