# Author: Cristiano Cavo
# Date: 2019-08-18
# From: http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program works
# on two lists of different sizes.
# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out
#    at this point - we’ll get to it soon)

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


def findCommonNumbers(a, b):
    c = removeDuplicates(a)
    d = removeDuplicates(b)
    e = []
    for i in range(len(c)):
        for j in range(len(d)):
            if c[i] == d[j]:
                e.append(c[i])
    return e


def main():
    a = randomArrayInt(randomInt(5, 10), 0, 20)
    b = randomArrayInt(randomInt(5, 10), 0, 20)
    c = findCommonNumbers(a, b)
    print("array a: ", a)
    print("array b: ", b)
    print("common values: ", c)


main()
