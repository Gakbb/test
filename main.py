from os import listdir
from os.path import isfile, join, exists

def buildFileTree(path):
    items = listdir(mypath)
    fileNum = 1

    for item in items:
        print(str(fileNum) + "." + item)
        fileNum += 1
    return items

while True:
    mypath = input("Enter path: ")
    if not exists(mypath):
        print("Wrong path")
    else:
        break

items = buildFileTree(mypath)

choice = input("Choose item 1 - " + str(len(items)))
if choice == items:
