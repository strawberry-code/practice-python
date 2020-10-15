# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html


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


# main()
