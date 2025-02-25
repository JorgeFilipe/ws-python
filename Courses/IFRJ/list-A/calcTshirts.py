smallCost=10
mediumCost=12
largeCost=15


tshirtSmall = int(input("Enter quantity of small t-shirts to be sold: "))
tshirtMedium = int(input("Enter quantity of medium t-shirts to be sold: "))
tshirtLarge = int(input("Enter quantity of large t-shirts to be sold: "))

sellValue = ( (smallCost * tshirtSmall) + (mediumCost * tshirtMedium) + (largeCost * tshirtLarge) )

print(f"The cost for {tshirtSmall} Small T-shirts ; {tshirtMedium} Medium T-shirts ; {tshirtLarge} Large T-shirts")
print(f"is: {sellValue}.00 USD")