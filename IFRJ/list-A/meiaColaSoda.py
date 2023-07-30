# The Meia-Cola soft drink factory sells products in 3 formats:
# Can (350ml) ;
# bottle (600ml) ;
# bottle (2 liter)
#
# Calculate how many liters of soda will be purchased

def convertToLiters(value):
    liter = (value/1000)
    return liter

can = 350 # in mL
bottle1 = 600 # in mL
bottle2 = 2000 # in mL

amountCans = int(input("Enter the quantity of cans (350mL) you will purchase: "))
amountBottles1 = int(input("Enter the quantity of bottles (600mL) you will purchase: "))
amountBottles2 = int(input("Enter the quantity of bottles (2L) you will purchase: "))

totalLiters = ((amountCans*can)+(amountBottles1*bottle1)+(amountBottles2*bottle2))

print(f"You purchase {totalLiters} Liters")