from datetime import date

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
birthDate = datetime.datetime(year, month, day)
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 

print(calculateAge(birthday))
