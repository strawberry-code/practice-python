# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20,
# 25]) and makes a new list of only the first and last elements of the given
# list. For practice, write this code inside a function.

import random


def randomInt(_from, _to):
    return random.randint(_from, _to)


def randomArrayInt(size, _from, _to):
    a = []
    for i in range(size):
        a.append(randomInt(_from, _to))
    return a


def sortArray(array):
    sortedArray = set(array)
    return sortedArray


def task1():
    print(" - - - task1 - - -")
    array = randomArrayInt(10, 1, 10)
    print("array is: {}".format(array))
    head = array[0]
    tail = array[len(array) - 1]
    print("head: [{}]\ntail: [{}]".format(head, tail))


def task2():
    print(" - - - task2 - - -")
    array = randomArrayInt(10, 1, 10)
    print("array is: {}".format(array))
    sortedArray = sortArray(array)
    print("sorted array is: {}".format(sortedArray))
    head = min(sortedArray)
    tail = max(sortedArray)
    print("head: [{}]\ntail: [{}]".format(head, tail))


def main():
    task1()
    task2()


main()
