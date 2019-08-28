# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# Notes: this exercise is exactly the same of the previous one, just skip to 35

# In the previous exercise we created a dictionary of famous scientists’
# birthdays. In this exercise, modify your program from Part 1 to load the
# birthday dictionary from a JSON file on disk, rather than having the
# dictionary defined in the program.
# 
# Bonus: Ask the user for another scientist’s name and birthday to add to the
# dictionary, and update the JSON file you have on disk with the scientist’s
# name. If you run the program multiple times and keep adding new names, your
# JSON file should keep getting bigger and bigger.

import json


def getBirthdays(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
    return data


def printBirthdays(birthdays):
    print("stored birthdays are:")
    i = 0
    for k in birthdays.keys():
        print(" {}. {}".format(i, k))
        i = i + 1


def printBirthday(birthdays, someone):
    print("{} was born in {}".format(someone, birthdays[someone]))


def askBirthday(birthdays):
    choice = int(input("choose someone: > "))
    if choice < len(birthdays):
        someone = list(birthdays.keys())[choice]
        printBirthday(birthdays, someone)
    else:
        print("invalid input")


def main():
    birthdays = getBirthdays("birthdays.json")
    printBirthdays(birthdays)
    askBirthday(birthdays)


main()
