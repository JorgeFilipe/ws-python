
name=input("What is the name of the student? ")
discipline=input("what is the name of the discipline: ")
note1=float(input("Enter the first note: "))
note2=float(input("Enter the second note: "))
note3=float(input("Enter the third note: "))

weightedAverage=( ( (note1*1.5) + (note2*1.6) + (note3*1.7) ) /3)

print(f"The student {name} in the discipline {discipline} reached")
print(f"the average score {weightedAverage:,.2f}")
