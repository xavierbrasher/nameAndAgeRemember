def makeFileUsable():
    try:
        t = open("savedData.py", "r")
        contents = t.read()
        if contents.__contains__("namesOfPeople ="):
            t.close
        else:
            t.close
            f = open("savedData.py", "w")
            f.write("namesOfPeople = []" + "\n")
            f.write("birthdaysOfPeople = []" + "\n")
            f.write("agesOfPeople = []" + "\n")
            f.close
    except Exception:
        f = open("savedData.py", "w")
        f.write("namesOfPeople = []" + "\n")
        f.write("birthdaysOfPeople = []" + "\n")
        f.write("agesOfPeople = []" + "\n")
        f.close
makeFileUsable()

import os
import time as t
from subprocess import check_call, check_output, call 
def clear():
    try:
        os.system('cls')
    except Exception:
        os.system('clear')
print('\033[94m')
clear()
print("Loading...")
t.sleep(1)
clear()
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
    birthDate = datetime.datetime(int(year), int(month), int(day))
    ageCalculationEnd = str(makeMath(birthDate))
    clear()

    checkageloop = True
    while checkageloop:
        clear()
        print("Is this your age? " + ageCalculationEnd + " (Answer with y or n)")
        checkBirthday = input()
        checkBirthday.lower()
        if checkBirthday == "y":
            clear()
            print("Cool")
            t.sleep(1)
            agesOfPeople.append(ageCalculationEnd)
            namesOfPeople.append(newName)
            birthdaysOfPeople.append(birthdaydate)
            save()
            checkageloop = False
        elif checkBirthday == "Y":
            clear()
            print("Cool")
            t.sleep(1)
            agesOfPeople.append(ageCalculationEnd)
            namesOfPeople.append(newName)
            birthdaysOfPeople.append(birthdaydate)
            save()
            checkageloop = False
        elif checkBirthday == "n":
            clear()
            print("Okay. If you want to try again. Go back to add someone in menu")
            t.sleep(2)
            checkageloop = False
        elif checkBirthday == "N":
            clear()
            print("Okay. If you want to try again. Go back to add someone in menu")
            t.sleep(1)
            checkageloop = False
        else:
            clear()
            print("Try Again")
            t.sleep(1)


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
            except Exception:
                if index == "c" or index == "C":
                    print("Ok. Cancelling.....")
                    done = True
                else:
                    print("Please try again")
                    t.sleep(1)
                    clear()

def refreshAges():
    for i in birthdaysOfPeople:
        newBirthday = ""
        for x in i:
            if x == "/":
                newBirthday += " "
            else:
                newBirthday += x
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
        birthDate = datetime.datetime(int(year), int(month), int(day))
        ageCalculationEnd = str(makeMath(birthDate))
        indexInAges = birthdaysOfPeople.index(i)
        agesOfPeople[indexInAges] = ageCalculationEnd
        save()
        clear()


while quit:
    clear()
    refreshAges()
    clear()
    print("Welcome To The Name and Age Remember")
    print("Type n To put someone in")
    print("Type l to list the names")
    print("Type r to remove a name")
    print("Type h to hack into the mainframe")
    print("Type f to refresh the ages")
    print("Type q to quit")
    decision = input("")
    if decision == "q" or decision == "Q":
        clear()
        save()
        print('\033[99m' + "1")
        input
        clear()
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
    elif decision == "f" or decision == "F":
        clear()
        refreshAges()
        save()
    elif decision == "h" or decision == "H":
        print('\033[92m')
        clear()
        print(os.system("c: & tree"))
        t.sleep(1)
    else:
        clear()
