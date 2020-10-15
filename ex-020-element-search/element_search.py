# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/11/11/20-element-search.html

# Write a function that takes an ordered list of numbers (a list where the
# elements are in order from smallest to largest) and another number. The
# function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
#  Extras: Use binary search.

import random
import sys

USE_COMMAND_LINE_ARGUMENT = True
USE_CUSTOM_BINARY_SEARCH = True


def randomInt(_from, _to):
    return random.randint(_from, _to)


def randomSortedArray(size, _from, _to):
    a = []
    for i in range(size):
        a.append(randomInt(_from, _to))
    return sorted(set(a))


def pythonBuiltInSearch(array, key):
    if key in array:
        return True
    else:
        return False


def binarySearch(array, key):
    found = False
    previousPivot = -1
    pivot = int(len(array) / 2)
    backstop = 10
    while found == False:
        if pivot >= len(array) or pivot < 0:
            found = False
            break
        if array[pivot] == key:
            found = True
            break
        elif previousPivot == pivot:
            found = False
            break
        elif array[pivot] > key:
            previousPivot = pivot
            pivot = int(pivot - (pivot / 2))
        elif array[pivot] < key:
            previousPivot = pivot
            pivot = int(pivot + (pivot / 2))
        if backstop == 0:
            break
        backstop = backstop - 1
    return found


def main():
    randomArray = randomSortedArray(200000, 0, 200000)
    key = 0
    if USE_COMMAND_LINE_ARGUMENT:
        key = int(sys.argv[1])  # Use user input from command line argument
    else:
        key = int(input("give a number:\n> "))  # Use user input from stdin

    if USE_CUSTOM_BINARY_SEARCH:
        print(binarySearch(randomArray, key))
    else:
        print(pythonBuiltInSearch(randomArray, key))


main()
