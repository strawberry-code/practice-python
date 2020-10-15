# Author: Cristiano Cavo
# Date: 2019-08-17
# From: http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd
# number react differently when divided by 2?
# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one
#    number to divide by (check). If check divides evenly into num, tell that to
#    the user. If not, print a different appropriate message.

number = input("give me a number: ")

check = input("give me a check: ")

modulus = int(number) % 2

if modulus == 1:
    print("this number is odd 💛")
else:
    print("this number is even 💚")

modulus4 = int(number) % 4

if modulus4 == 0:
    print("this number is a multiple of 4 💚")
else:
    print("this number is not a multiple of 4 💛")

modulusCheck = int(number) % int(check)
if modulusCheck == 0:
    print("number " + str(number) + " is a multiple of " + str(check) + " 💚")
else:
    print("number " + str(number) + " is not a multiple of " + str(check) + " 💚")
