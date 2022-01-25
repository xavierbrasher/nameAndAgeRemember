def make_file_usable():
    try:
        t = open("savedData.py", "r")
        contents = t.read()
        if contents.__contains__("namesOfPeople ="):
            t.close()
        else:
            t.close()
            f = open("savedData.py", "w")
            f.write("namesOfPeople = []" + "\n")
            f.write("birthdaysOfPeople = []" + "\n")
            f.write("agesOfPeople = []" + "\n")
            f.close()
    except Exception:
        f = open("savedData.py", "w")
        f.write("namesOfPeople = []" + "\n")
        f.write("birthdaysOfPeople = []" + "\n")
        f.write("agesOfPeople = []" + "\n")
        f.close()


make_file_usable()

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
from sys import platform
from savedData import *
from datetime import date, datetime
import datetime

age = ""
newBirthday = ""


def save():
    f = open("savedData.py", "w")
    f.write("namesOfPeople = " + str(namesOfPeople) + "\n")
    f.write("birthdaysOfPeople = " + str(birthdaysOfPeople) + "\n")
    f.write("agesOfPeople = " + str(agesOfPeople) + "\n")
    f.close()


def make_math(birth_date_calculation):
    today = date.today()
    age = today.year - birth_date_calculation.year - (
            (today.month, today.day) < (birth_date_calculation.month, birth_date_calculation.day))
    return age


def calculate_age(birthday_date, new_name):
    newBirthday = ""
    newBirthday = ""
    for x in birthday_date:
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
    ageCalculationEnd = str(make_math(birthDate))
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
            namesOfPeople.append(new_name)
            birthdaysOfPeople.append(birthday_date)
            save()
            checkageloop = False
        elif checkBirthday == "Y":
            clear()
            print("Cool")
            t.sleep(1)
            agesOfPeople.append(ageCalculationEnd)
            namesOfPeople.append(new_name)
            birthdaysOfPeople.append(birthday_date)
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


def new_person():
    print("Type c as name if you want to cancel")
    newName = input("What is the Name: ")
    if newName == "c" or newName == "C":
        print('Canceled')
        clear()
    else:

        newAge = input("Whats Your Birth date (DD/MM/YYYY): ")

        if len(newAge) == 10 and "/" in newAge:
            calculate_age(newAge, newName)
        else:
            print("Error. Retry")
            t.sleep(2)
            clear()
            new_person()
        clear()


def list_people():
    for x in range(len(namesOfPeople)):
        print(str(x + 1) + ". Name: " + namesOfPeople[x] + ". Age: " + agesOfPeople[x] + ".")


def remove_person():
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
            list_people()
            index = input()
            try:
                newIndex = int(index) - 1
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


def refresh_ages():
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
        ageCalculationEnd = str(make_math(birthDate))
        indexInAges = birthdaysOfPeople.index(i)
        agesOfPeople[indexInAges] = ageCalculationEnd
        save()
        clear()


def list_files(start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def main():
    running = True
    while running:
        clear()
        print('\033[94m')
        refresh_ages()
        clear()
        print("Welcome To The Name and Age Remember")
        print("Type n To put someone in")
        print("Type l to list the names")
        print("Type r to remove a name")
        print("Type h to hack into the mainframe (Do control-c to stop it)")
        print("Type f to refresh the ages")
        print("Type q to quit")
        decision = input("")
        if decision == "q" or decision == "Q":
            clear()
            save()
            print('\033[99m' + "1")
            clear()
            print("Goodbye")
            running = False
            exit()
        elif decision == "n" or decision == "N":
            clear()
            new_person()
        elif decision == "r" or decision == "R":
            clear()
            remove_person()
            save()
            clear()
        elif decision == "l" or decision == "L":
            clear()
            print("Press enter to continue")
            list_people()
            input()
            save()
            clear()
        elif decision == "f" or decision == "F":
            clear()
            refresh_ages()
            save()
        elif decision == "h" or decision == "H":
            try:
                print('\033[92m')
                clear()
                if platform == "linux" or platform == "linux2":
                    list_files("/")
                elif platform == "darwin":
                    list_files("/")
                else:
                    os.system("c:")
                    print(os.system("tree"))
                t.sleep(1)
            except:
                clear()
                print('\033[94m')
                print("HAHA fine it will stop")
                t.sleep(2)
        else:
            clear()


if __name__ == "__main__":
    main()
