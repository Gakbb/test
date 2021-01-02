import os
from os import listdir
from os.path import exists,isfile,join


def buildFileTree(path):
    items = listdir(path)
    fileNum = 1

    for item in items:
        print(str(fileNum) + "." + item)
        fileNum += 1
    return [join(path, i) for i in items]

while True:
    mypath = input("Enter path: ")
    if not exists(mypath):
        print("Wrong path")
    else:
        break

choice = ""
pathToOpen = mypath

while choice != "exit":
    items = buildFileTree(pathToOpen)

    choice = input("Choose item 1 - " + str(len(items)) + ": ")


    try:
        chosenItem = items[int(choice)-1]
    except ValueError:
        break

    if isfile(chosenItem):
        os.startfile(chosenItem)
    else:
        pathToOpen = chosenItem

