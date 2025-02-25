# Taxes = (-10%) on salary
# Hour worked = 10 R$
# work extra hours = 15 R$
# gross salary = (Hour worked*10) + (work extra hours*15)
# net salary = (gross salary - 10% Taxes)

def taxes(salary):
    percent=((salary/100)*10)
    sal=(salary-percent)
    return sal

hour_worked = int(input("Enter the amount of hours worked: "))

opt = input("Did you work overtime? (y/n): ")

if(opt=="y"):
    extra_hours =  int(input("Enter the amount of overtime worked: "))
    gross_salary =( (hour_worked*10) + (extra_hours*15) )
    net_salary = taxes(gross_salary)
    print()
    print("You gross salary: ", gross_salary)
    print("You net salary: ", net_salary)
else:
    gross_salary =(hour_worked*10)
    net_salary = taxes(gross_salary)
    print()
    print("You gross salary: ", gross_salary)
    print("You net salary: ", net_salary)