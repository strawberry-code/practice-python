# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

# Implement a function that takes as input three variables, and returns the
# largest of the three. Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python
# normally takes care of for us. All you need is some variables and if
# statements!


def userInput():
    rawNumbers = input("give three numbers:\n > ").split()
    a = int(rawNumbers[0])
    b = int(rawNumbers[1])
    c = int(rawNumbers[2])
    return a, b, c


def findMax(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > a:
        return c


def main():
    a, b, c = userInput()
    print("the max of three is: {}".format(findMax(a, b, c)))


main()
