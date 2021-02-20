name = ["hi","test"]
print(name)
newBirthday = ""
for i in name:
    for x in i:
        if x == "/":
            newBirthday += " "
        else:
            newBirthday += x
    print(newBirthday)