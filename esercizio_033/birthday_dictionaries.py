# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

# This exercise is Part 1 of 4 of the birthday data exercise series. The other
# exercises are: Part 2, Part 3, and Part 4.
#
# For this exercise, we will keep track of when our friend’s birthdays are, and
# be able to find that information based on their name. Create a dictionary (in
# your file) of names and birthdays. When you run your program it should ask the
# user to enter a name, and return the birthday of that person back to them. The
# interaction should look something like this:
#
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.
# Happy coding!

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
