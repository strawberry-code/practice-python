# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no
# divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def getUserInput():
    return int(input("give a number:\n > "))


def isPrime(num):
    prime = True
    mcd = num
    for i in range(2, num):
        if num % i == 0:
            prime = False
            mcd = i
            break
    return prime, mcd


def main():
    num = getUserInput()
    prime, mcd = isPrime(num)
    print("{} is prime: {}\nminimum common divisor is: {}".format(num, prime, mcd))


main()
