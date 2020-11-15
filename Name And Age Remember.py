import os
import time as t
from savedData import *
age = ""
quit = True


def clear():
    os.system('cls')



def save():
    f = open("savedData.py", "w")
    f.write("namesOfPeople = "+ str(namesOfPeople) + "\n")
    f.write("agesOfPeople = "+ str(agesOfPeople) + "\n")
    f.close




def newPerson():
    print("Type c as name if you want to cancel")
    newName = input("What is the Name: ")
    if newName == "c" or newName == "C":
        print('Canceled')
        clear()
    else:
        namesOfPeople.append(newName)

        newAge = input("Whats Your Age: ")
        agesOfPeople.append(newAge)
        clear()


def listPeople():
    for x in range(len(namesOfPeople)):
        print("Name: " + namesOfPeople[x] + ". Age: " + agesOfPeople[x] + ".")


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
    elif decision == "n" or decision == "N":
        clear()
        newPerson()
        save()
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
        save()
        clear()
