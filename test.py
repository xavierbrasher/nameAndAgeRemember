from datetime import date
import datetime

birthday = input()
newBirthday = ""

for x in birthday:
    if x == "/":
        newBirthday += " "
    else:
        newBirthday += x
print(newBirthday)

day = ""
month = ""
year = ""
for x in range(len(newBirthday)):
    if x <= 2:
        day += newBirthday[x]
    elif x == 4:
        month += newBirthday[x]
    elif x == 5:
        month += newBirthday[x]
    elif x >= 6:
        year += newBirthday[x]
print(day)
print(month)
print(year)

datetdy = date.today().strftime("%d/%m/%Y")
birthDate = datetime.datetime(int(year), int(month), int(day))
def calculateAge(birthDateCalculation): 
    today = date.today() 
    age = today.year - birthDateCalculation.year - ((today.month, today.day) < (birthDateCalculation.month, birthDateCalculation.day)) 
    return age 

print(calculateAge(birthDate))
