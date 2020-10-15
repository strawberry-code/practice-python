# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, except with
# the words in backwards order. For example, say I type the string:
#       My name is Michele
# Then I would see the string:
#       Michele is name My
# shown back to me.


def getUserInput(message="give a string:\n > "):
    string = input(message)
    return string


def splitString(string):
    splittedString = string.split()
    return splittedString


def reverseWordOrder(string):
    reversedString = reversed(string)
    return reversedString


def joinSplittedString(string):
    joinedString = " ".join(string)
    return joinedString


def main():
    string = getUserInput()
    splittedString = splitString(string)
    reversedString = reverseWordOrder(splittedString)
    joinedString = joinSplittedString(reversedString)
    print(joinedString)


main()
