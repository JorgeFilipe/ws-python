def readjustment(value):
    a = (value/100)*15
    b = (value/100)*8
    c = (value+a)-b
    return c

payment = float(input("Inform the amount of your payment: "))
print()
print("Your payment will increase  15%, and decrease 8%, because of Taxes! ")
print()
print("Your Salary (after readjustment): ","$ ",readjustment(payment))
print()



