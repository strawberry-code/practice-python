# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

# Create a program that will play the “cows and bulls” game with the user. The
# game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they
# have a “cow”. For every digit the user guessed correctly in the wrong place is
# a “bull.” Every time the user makes a guess, tell them how many “cows” and
# “bulls” they have. Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and
# tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could
# look like this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
#
# Until the user guesses the number.

import random
import re

WORD_SIZE = 3


def intro():
    print("- - - - Welcome to the Bulls and Cows game! - - - -")
    print("- - This version of the game")
    print("- - is based on {}-digits words.".format(WORD_SIZE))


def generateNewWord():
    word = []
    for i in range(WORD_SIZE):
        word.append(random.randint(0, 9))
    return word


def playerInput():
    playerWord = ""
    goodInput = False
    while goodInput == False:
        playerWord = input("Guess the {}-digits word:\n > ".format(WORD_SIZE))
        if not re.search("^[0-9]{" + str(WORD_SIZE) + "}$", playerWord):
            print("please give a {}-digits word...".format(WORD_SIZE))
        else:
            goodInput = True
    return playerWord


def countBulls(word, playerWord):
    score = ["n"] * 20
    for i in range(WORD_SIZE):
        for j in range(WORD_SIZE):
            if int(playerWord[i]) == int(word[j]) and int(i) == int(j):
                score[i] = "b"
    return score


def countCows(word, playerWord, score):
    for i in range(WORD_SIZE):
        for j in range(WORD_SIZE):
            if (
                int(playerWord[i]) == int(word[j])
                and int(i) != int(j)
                and score[i] != "b"
            ):
                score[i] = "c"
    return score


def play(word, playerWord):
    score = []
    score = countBulls(word, playerWord)
    score = countCows(word, playerWord, score)

    print(
        "you get:\n - {} bulls\n - {} cows".format(score.count("b"), score.count("c"))
    )
    if score.count("b") == WORD_SIZE:
        print("-<( YOU WIN! )>-")
        return True
    else:
        print("retry")
        return False


def main():
    intro()
    word = generateNewWord()
    win = False
    while win == False:
        print(" --- CHEATS ENABLED! Word is >{}<".format(word))
        playerWord = playerInput()
        win = play(word, playerWord)


main()