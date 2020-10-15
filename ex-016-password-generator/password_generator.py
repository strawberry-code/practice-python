# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

# Write a password generator in Python. Be creative with how you generate
# passwords - strong passwords have a mix of lowercase letters, uppercase
# letters, numbers, and symbols. The passwords should be random, generating a
# new password every time the user asks for a new password. Include your
# run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords,
# pick a word or two from a list.

import random

pool = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_-!£$&"


def randomInt(_from, _to):
    return random.randint(_from, _to)


def userIntnput(message="get a number:\n > "):
    num = int(input(message))
    return num


def generatePassword(passwordLength):
    password = []
    for i in range(passwordLength):
        randomChar = pool[int(randomInt(0, len(pool) - 1))]
        password.append(randomChar)
    password = "".join(password)
    return password


def main():
    passwordLength = userIntnput("give the password length:\n > ")
    password = generatePassword(passwordLength)
    print(password)


main()
