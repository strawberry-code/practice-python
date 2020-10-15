# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

#  Given a .txt file that has a list of a bunch of names, count how many of each
#  name there are in the file, and print out the results to the screen. I have a
#  .txt file for you, if you want to use it!
#  Extra:
#  1. Instead of using the .txt file from above (or instead of, if you want the
#     challenge), take this .txt file, and count how many of each “category” of
#     each image there are. This text file is actually a list of files
#     corresponding to the SUN database scene recognition database, and lists the
#     file directory hierarchy for the images. Once you take a look at the first
#     line or two of the file, it will be clear which part represents the scene
#     category. To do this, you’re going to have to remember a bit about string
#     parsing in Python 3. I talked a little bit about it in this post.

# Notes: I decided to read from the file generated in the exercise number 21 and to looking for the frequency of some given words

""" # # # # -<( Bootcamp )>- # # # #

with open('file_to_read.txt', 'r') as open_file:
    text = open_file.read()

"""


def getText(filepath):
    with open(filepath, "r") as open_file:
        text = open_file.read()
    return text


def getQuerySet():
    userInput = True
    querySet = []
    while userInput:
        word = input("give a word (type 'stop' ti finish):\n > ")
        if word != "stop":
            querySet.append(word)
        else:
            userInput = False
    return querySet


def countFrequencies(text, querySet):
    for word in querySet:
        print(" - {} found {} times".format(word, text.count(word)))


def main():
    querySet = getQuerySet()
    fileText = getText("../esercizio_021/output.txt")
    countFrequencies(fileText, querySet)


main()

""" # # # # -<( EXAMPLE USAGE )>- # # # #

╭─ ~/Programming/python/self-training/esercizi_python/esercizio_022 ▓▒░──────────────────────────────░▒▓ ✔ | took 11s ─╮
╰─ py read_from_file.py                                                                                               ─╯
give a word (type 'stop' ti finish):
 > gatto
give a word (type 'stop' ti finish):
 > gatta
give a word (type 'stop' ti finish):
 > gatti
give a word (type 'stop' ti finish):
 > gatte
give a word (type 'stop' ti finish):
 > stop
 - gatto found 4 times
 - gatta found 1 times
 - gatti found 2 times
 - gatte found 2 times

"""
