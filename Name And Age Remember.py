def makeFileUsable():
    try:
        t = open("savedData.py", "r")
        contents = t.read()
        print(contents)
        input()
        if contents.__contains__("namesOfPeople ="):
            print("true")
            input()
            t.close
        else:
            t.close
            print("false")
            input()
            f = open("savedData.py", "w")
            f.write("namesOfPeople = []" + "\n")
            f.write("birthdaysOfPeople = []" + "\n")
            f.write("agesOfPeople = []" + "\n")
            f.close
    except:
        f = open("savedData.py", "w")
        f.write("namesOfPeople = []" + "\n")
        f.write("birthdaysOfPeople = []" + "\n")
        f.write("agesOfPeople = []" + "\n")
        f.close
makeFileUsable()

import os
import time as t
os.system('cls')
print("Loading...")
t.sleep(2)
os.system('cls')
from savedData import *
from datetime import date, datetime
import datetime

age = ""
quit = True
newBirthday = ""

def save():
    f = open("savedData.py", "w")
    f.write("namesOfPeople = "+ str(namesOfPeople) + "\n")
    f.write("birthdaysOfPeople = "+ str(birthdaysOfPeople) + "\n")
    f.write("agesOfPeople = "+ str(agesOfPeople) + "\n")
    f.close
def clear():
    os.system('cls')



def makeMath(birthDateCalculation):
    today = date.today() 
    age = today.year - birthDateCalculation.year - ((today.month, today.day) < (birthDateCalculation.month, birthDateCalculation.day)) 
    return age 
    
def calculateAge(birthdaydate, newName):
    newBirthday = ""
    newBirthday = ""
    for x in birthdaydate:
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
                month += newBirthday[x + 1]
        elif x >= 6:
            year += newBirthday[x]
    print(day)
    print(month)
    print(year)
    birthDate = datetime.datetime(int(year), int(month), int(day))
    ageCalculationEnd = str(makeMath(birthDate))
    print(ageCalculationEnd)
    print("Is this your correct birthday? " + ageCalculationEnd + " Answer with y or n")
    checkageloop = True
    while checkageloop:
        checkBirthday = input()
        checkBirthday.lower()
        if checkBirthday == "y":
            print("Cool")
            t.sleep(1)
            agesOfPeople.append(ageCalculationEnd)
            namesOfPeople.append(newName)
            birthdaysOfPeople.append(birthdaydate)
            save()
            checkageloop = False
        elif checkBirthday == "Y":
            print("Cool")
            t.sleep(1)
            agesOfPeople.append(ageCalculationEnd)
            namesOfPeople.append(newName)
            birthdaysOfPeople.append(birthdaydate)
            save()
            checkageloop = False
        elif checkBirthday == "n":
            clear()
            print("damn it")
            t.sleep(1)
            checkageloop = False
        elif checkBirthday == "N":
            clear()
            print("damn it")
            t.sleep(1)
            checkageloop = False





            






def newPerson():
    print("Type c as name if you want to cancel")
    newName = input("What is the Name: ")
    if newName == "c" or newName == "C":
        print('Canceled')
        clear()
    else:

        newAge = input("Whats Your Birth date (DD/MM/YYYY): ")

        if len(newAge) == 10 and "/" in newAge:
            calculateAge(newAge, newName)
        else:
            print("Error. Retry")
            t.sleep(2)
            clear()
            newPerson()
        clear()



def listPeople():
    for x in range(len(namesOfPeople)):
        print(str(x+1)+". Name: " + namesOfPeople[x] + ". Age: " + agesOfPeople[x] + ".")



def removePerson():
    done = False
    newIndex = 0
    while done == False:
        if len(namesOfPeople) == 0:
            done = True
            print("There is no one to get rid off!")
            input("Enter to continue")
            clear()
        else:
            print("Which one do you want to remove? From 1 to " + str(len(namesOfPeople)) + " (type c to cancel)")
            listPeople()
            index = input()
            try:
                newIndex = int(index)-1
                namesOfPeople.remove(namesOfPeople[newIndex])
                birthdaysOfPeople.remove(birthdaysOfPeople[newIndex])
                agesOfPeople.remove(agesOfPeople[newIndex])
                done = True
            except:
                if index == "c" or index == "C":
                    print("Ok. Cancelling.....")
                    done = True
                else:
                    print("Please try again")
                    t.sleep(1)
                    clear()


while quit:
    clear()
    print("Welcome To The Name and Age Remember")
    print("Type n To put someone in")
    print("Type l to list the names")
    print("Type r to remove a name")
    print("Type q to quit")
    decision = input("")
    if decision == "q" or decision == "Q":
        clear()
        save()
        print("Goodbye")
        quit = False
        exit()
    elif decision == "n" or decision == "N":
        clear()
        newPerson()
    elif decision == "r" or decision == "R":
        clear()
        removePerson()
        save()
        clear()
    elif decision == "l" or decision == "L":
        clear()
        print("Press enter to continue")
        listPeople()
        input()
        save()
        clear()
    else:
        clear()
