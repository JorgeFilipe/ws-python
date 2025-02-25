#  _________________________________________________________________________________
# | cheese = 50 grams                                                               |
# | ham = 50 gram                                                                   |
# | hamburguer = 100 gram                                                           |
# |---------------------------------------------------------------------------------|
# | To make the sandwich we need 2 slices of cheese, 1 slice of ham and 1 hamburger |
# |_________________________________________________________________________________|

def kilogram(value):
    newValue = (value/1000)
    return newValue

sandwich = int(input("Enter the number of sandwiches you will make today:"))

cheese=((2*50)*sandwich)
ham=(50*sandwich)
hamburguer=(100*sandwich)

print(f"For a total of {sandwich} sandwiches, you will need:")
print()
print("Cheese: ",kilogram(cheese),"Kilograms")
print("Ham: ",kilogram(ham),"Kilograms")
print("Hamburguer: ",kilogram(hamburguer),"Kilograms")
print()