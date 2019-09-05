
import datetime
import os


def getInfo():
    author = input(" [1] Give Author Name (def=Cristiano Cavo): ")
    provenience = input(" [2] Give provenience (def=myself): ")
    usemain = input(" [3] Use main (y/n) (def=y): ")
    exercisename = input(" [4] Exercise name: ")
    description = input(" [5] Description: ")

    if author == "" :
        author = "Cristiano Cavo"

    if provenience == "":
        provenience = "myself"

    if usemain == "y" or usemain == "":
        usemain = True
    else:
        usemain = False

    date = "{}-{}-{}".format(datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)

    return author, date, provenience, usemain, exercisename, description

def createNewFolder():
    listAll = os.listdir(".")

    for elem in listAll:
        if "esercizio_" not in elem:
            listAll.remove(elem)

    for i in range(len(listAll)):
        listAll[i] = int(listAll[i].replace("esercizio_", ""))

    foldername = f'esercizio_{max(listAll)+1:03}'
    print("creating nev exercise folder: {}".format(foldername))
    os.mkdir(foldername)
    return foldername

def writeFile(filename, content):
    with open(filename, "w") as text_file:
        text_file.write(content)

def main():
    author, date, provenience, usemain, exercisename, description = getInfo()
    maincode = ""
    if usemain:
        maincode = "\n\ndef main():\n\tprint(\"Hello, World!\")\n\nmain()\n"
    else:
        maincode = ""
    text = "# Author: {}\n".format(author) + "# Date: {}\n".format(date) + "# From: {}\n\n".format(provenience) + "# Description: {}\n".format(description) + maincode

    exerciseFolder = createNewFolder()
    exercisePath = "./{}/{}.py".format(exerciseFolder, exercisename)

    writeFile(exercisePath, text)

main()
