# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.
# Extras:
# 1. Write two different functions to do this - one using a loop and
#    constructing a list, and another using sets.
# 2. Go back and do Exercise 5 using sets, and write the solution for that in a
#    different function.

import random


def randomInt(_from, _to):
    return random.randint(_from, _to)


def randomArrayInt(size, _from, _to):
    a = []
    for i in range(size):
        a.append(randomInt(_from, _to))
    return a


def removeDuplicates(a):
    return list(dict.fromkeys(a))


def removeDuplicatesAndSort(a):
    return set(a)


def main():
    array = randomArrayInt(30, 1, 20)
    withouDuplicates = removeDuplicates(array)
    withouDuplicatesAndSorted = removeDuplicatesAndSort(array)
    print(
        "input array: {}\nwithout duplicates: {}\nwithout duplicates and sorted: {}".format(
            array, withouDuplicates, withouDuplicatesAndSorted
        )
    )


main()
