# Author: Cristiano Cavo
# Date: 2019-08-19
# From: http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or
# exactly right. (Hint: remember to use the user input lessons from the very
# first exercise)
# Extras:
# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends,
#    print this out.

import random

min = 1
max = 3
number = random.randint(min, max)
msg = "try to guess a number from {} to {}"
guess = int(input("Try to guess a number from {} to {}:\n > ".format(min, max)))
if guess >= min and guess <= max:
    if guess == number:
        print("you win!")
    else:
        print("you lose")
else:
    print("please give a number from {} to {}".format(min, max))
