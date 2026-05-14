## Assume that the month always has 30 days


days=int(input("Insert the days without accidents: "))

if(days >= 30)and(days < 360):
    months = int(days/30)
    days = days%30
    print(f"Working Without Accidents for : {months} months and {days} days")
elif(days >= 360):
    months = int(days/30)
    years = int(months/12)
    mth = days%30
    print(f"Working Without Accidents for: {years} years and {mth} months")
else:
    print("Working Without Accidents for : ",days," days")
