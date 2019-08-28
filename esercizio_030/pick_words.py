# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

# This exercise is Part 1 of 3 of the Hangman exercise series. The other
# exercises are: Part 2 and Part 3.
#
# In this exercise, the task is to write a function that picks a random word
# from a list of words from the SOWPODS dictionary. Download this file and save
# it in the same directory as your Python code. This file is Peter Norvig’s
# compilation of the dictionary of words used in professional Scrabble
# tournaments. Each line in the file contains a single word.
#
# Hint: use the Python random library for picking a random word.

import random
import linecache


# It is assumed that the file structured as one single word for one single line
def countWords(filePath):
    return sum(1 for line in open(filePath))


def pickRandomWord(filePath):
    return str(linecache.getline(filePath, random.randint(0, countWords(filePath))))


def main():
    filePath = "./sowpods.txt"
    word = pickRandomWord(filePath)
    print("Picked word is: {}".format(word))


main()

"""
OR WITHOUT USING linecache LIBRARY:

linenumber = random(0, countWords(filePath))
fp = open("file")
for i, line in enumerate(fp):
    if i == linenumber:
        return line
fp.close()

"""
