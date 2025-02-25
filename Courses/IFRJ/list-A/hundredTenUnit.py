hundred=0
ten=0
unit=0

print()
value=int(input("Inform anything value: "))
print()

if(value <=999):
    hundred=int(value/100)
    ten=int((value%100)/10)
    unit=(value%10)

    print("Hundred | Ten | Unit")
    print("    ",hundred," | ",ten," | ",unit)
    print()
else:
    print("Please, enter a value below 999.")
    print()