def corpoDaFuncao():
  print(" ◸ ►►►►►►►►►►►►►►◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄ ◹ ")
  print(" ↑ Estou dentro da função        ↑")
  soma=1+999
  print(" ↓ ",soma,"                        ↓")
  print(" ◺ ►►►►►►►►►►►►►►◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄ ◿ ")
print("Estou fora da função")
corpoDaFuncao()
# In the example above, the indentation delimits the function body.

print()##################################################

def concatenando():
  a=5
  b=10
  c=15
  d=20
  e=25
  f="Resultado: "
  if(b==10): # First Condition
    b=b+c-a
    if(b==20): # Second Condition
      b=b-d
      if(b==0): # Third Condition
        print(f,e+a)
concatenando()
# To concatenate more code blocks inside of the function body, insert (:) colon/two-points in the condition.

print()##################################################

# Lessons

student1="John"
student2="Roger"
def welcome(name):
  exibe_msg="Olá "+ name
  print(exibe_msg)

welcome(student1)
welcome(student2)

print()##################################################

def WordUpperCase(name):
  msg="Bem-Vindo "+ name.capitalize()
  print(msg)
WordUpperCase("phillip")
WordUpperCase("jason")
WordUpperCase("thomas")
# how to change the first letter of the word to capital

print()##################################################

def titleUpperCase(name):
  msg="Hi, "+name.title()+" !"
  print(msg)
titleUpperCase("thomas anderson")
titleUpperCase("abraham lincoln")
titleUpperCase("teodore roosevelt")
print()
msg="out of sight! out of mind!"
print(msg.title())
print("no pain! no gain!".title()) # Using the function direct in string.
# how to change each of first letter of the word to capital. Add .title() after the declaration of variable

print()##################################################

def plus(n1, n2):
  soma=n1+n2
  print("Soma A + B = ", soma)

n1=input("Insira um valor: ")
n2=input("Insira outro valor: ")
plus(n1, n2)
print("Without converting the input() function the captured value will be of type string : ",type(n1))
# The input function get the value write by user, but the value is in string type.
# So need convert the string value to int value. The conversion can do directly in declaration of input function.
n3 = int( input("Insira o valor de A: "))
n4 = int( input("Insira o valor de B: "))
plus(n3, n4)

print()##################################################

# while one of arguments is send without value, a error is return in the function.
def faltandoAlgo(x, y, z):
  result=(x^x)+(x^y)+(x^z)+(y^y)+(y^z)+(z^z)+(z^y)
  print(result)
a=0
b=0
#faltandoAlgo(a, b, ) # line commented for avoid stops code execution
# To bypass this error, just set default parameter. See the example below:
def defaultParameter(x=0, y=0, z=0): # Defining default values for the three parameters
  result=(x + y + z)*(z - y - x)
  print("Calc: ", result)
a = int(input("Insira um valor para X: "))
b = int(input("Insira um valor para Y: "))
c = int(input("Insira um valor para Z: "))
defaultParameter(a, b, c)

# Same example above, Similar an login scenario where we have a message for user loggeds using your username. If the user does not inform your name, there will be a message default:
def greatings(name="anonymous"):
  print("Hi "+name+" !!")
greatings("Jonh") # Send argument to the fuction
greatings() # without sending argument to the fuction

print()##################################################

# How formating strings inside print function:
# Using the letter (F) before "". Example: print(f"")
name="Josiah"
age=56
birthYear=1934
print("Name: {name}") # Whithout insert f before "".
print("Age: {age}") # Whithout insert f before "".
print(f"Name: {name}") # Inserting f before "".
print(f"Age: {age}") # Inserting f before "".
print()
# calculations can be performed inside print() using f for formatting.
print(f"Age in 2022: {2022-birthYear}")
