# 
# Ref: https://www.w3schools.com/python/python_functions.asp
# 




def my_function():
  print("Hello from a function")

my_function()


# Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Arbitrary Arguments, *args
#   If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#   This way the function will receive a tuple of arguments, and can access the items accordingly:
#
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments, **kwargs
#   If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#
#   This way the function will receive a dictionary of arguments, and can access the items accordingly:
#
# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



# Default Parameter Value
#   The following example shows how to use a default parameter value.
#   If we call the function without argument, it uses the default value:

# Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



# Passing a List as an Argument
#   You can send any data types of argument to a function (string, number, list, dictionary etc.),
#   and it will be treated as the same data type inside the function.
#   E.g. if you send a List as an argument, it will still be a List when it reaches the function:
# 
# Example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
#   To let a function return a value, use the return statement:
# Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))