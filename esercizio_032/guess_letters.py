# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

import os

def guessWord(word):
    secretLetters = list(word)
    del secretLetters[-1] # removes the \n
    guessedLetters = ["_"] * len(secretLetters)
    stop = False
    attempts = 6
    while not stop:
        if attempts == 0:
            print("you lose...")
            print("word was: {}".format(word))
            stop = True
        elif "_" not in guessedLetters:
            print("you win!")
            print(word)
            stop = True
        else:
            print(' '.join(guessedLetters))
            # print("cheats eabled:\n{}".format(secretLetters))
            userLetter = input("give a letter (0 to stop) (lefts attemps {})> ".format(attempts))
            os.system("clear")
            if userLetter == "0":
                stop = True
            elif userLetter in secretLetters:
                if attempts < 3: attempts = attempts + 1 # Easy mode: ON 😜
                for i in range(len(secretLetters)):
                    if secretLetters[i] == userLetter:
                        guessedLetters[i] = userLetter
            else:
                attempts = attempts - 1


def main():
    word = "EVAPORATE"
    guessWord(word)


# main()
