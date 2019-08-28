# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

# This exercise is Part 3 of 4 of the birthday data exercise series. The other
# exercises are: Part 1, Part 2, and Part 4.
#
# In the previous exercise we saved information about famous scientists’ names
# and birthdays to disk. In this exercise, load that JSON file from disk,
# extract the months of all the birthdays, and count how many scientists have a
# birthday in each month.
#
# Your program should output something like:
#
# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

import json
import datetime


def getBirthdays(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
    return data


def printBirthdays(birthdays):
    monthFrequencies = {}
    for v in birthdays.values():
        date = datetime.datetime.strptime(v, "%d/%m/%Y")
        if date.month in monthFrequencies:
            monthFrequencies[date.month] += 1
        else:
            monthFrequencies[date.month] = 1
    return monthFrequencies


def main():
    birthdays = getBirthdays("birthdays.json")
    months = printBirthdays(birthdays)
    print("{month}\t{frequency}")
    for e in months.keys():
        print("|{}\t|{}".format(e, months[e]))


main()
