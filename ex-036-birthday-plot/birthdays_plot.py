# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

# This exercise is Part 4 of 4 of the birthday data exercise series. The other
# exercises are: Part 1, Part 2, and Part 3.
#
# In the previous exercise we counted how many birthdays there are in each month
# in our dictionary of birthdays.
#
# In this exercise, use the bokeh Python library to plot a histogram of which
# months the scientists have birthdays in! Because it would take a long time for
# you to input the months of various scientists, you can use my scientist
# birthday JSON file. Just parse out the months (if you don’t know how, I
# suggest looking at the previous exercise or its solution) and draw your
# histogram.
#
# If you are using a purely web-based interface for coding, this exercise won’t
# work for you, since it requires installing the bokeh Python package. Now might
# be a good time to install Python on your own computer.


import json
import datetime
from bokeh.plotting import figure, show, output_file

output_file("plot.html")


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
    x = []
    y = []
    birthdays = getBirthdays("birthdays.json")
    months = printBirthdays(birthdays)
    print("{month}\t{frequency}")
    for e in months.keys():
        print("|{}\t|{}".format(e, months[e]))
        x.append(e)
        y.append(months[e])
    p = figure()
    p.vbar(x=x, top=y, width=0.5)
    show(p)


main()
