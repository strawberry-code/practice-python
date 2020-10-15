# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

# Given two .txt files that have lists of numbers in them, find the numbers that
# are overlapping. One .txt file has a list of all prime numbers under 1000, and
# the other .txt file has a list of happy numbers up to 1000.  (If you forgot,
# prime numbers are numbers that can’t be divided by any other number. And yes,
# happy numbers are a real thing in mathematics - you can look it up on
# Wikipedia. The explanation is easier with an example, which I will describe
# below.)

# File one: http://www.practicepython.org/assets/primenumbers.txt
# File two: http://www.practicepython.org/assets/happynumbers.txt

# Notes: I decided to read from the file generated in the exercise number 21 and
# to looking for the frequency of some given words

""" # # # # -<( Bootcamp )>- # # # #

with open('file_to_read.txt', 'r') as open_file:
    text = open_file.read()

"""


def getText(filepath):
    with open(filepath, "r") as open_file:
        text = open_file.read()
    return text


def findOverlaps(listOne, listTwo):
    listThree = []
    for e in listOne:
        if e in listTwo:
            listThree.append(e)
    return listThree


def main():
    listOne = getText("happynumbers.txt").split()
    listTwo = getText("primenumbers.txt").split()
    overlaps = findOverlaps(listOne, listTwo)
    print("overlaps: {}".format(overlaps))


main()
