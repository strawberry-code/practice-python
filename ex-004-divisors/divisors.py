# Author: Cristiano Cavo
# Date: 2019-08-17
# From: http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don’t know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor
# of 26 because 26 / 13 has no remainder.)


def isInt(value):
    try:
        integer = int(value)
    except:
        print("you must enter an integer")
        sys.exit()


def findDivisors(number):
    divisors = []
    for i in range(int(number)):
        dividend = int(number)
        divisor = int(number) - int(i)
        modulus = int(dividend) % int(divisor)
        msg = "{} = {} / {}"
        print(msg.format(modulus, dividend, divisor))
        if modulus == 0:
            divisors.append(divisor)
    return divisors


def main():
    number = input(
        "Insert a number and I will get you all the divisors for that number:\n > "
    )
    isInt(number)
    print(number)
    divisors = findDivisors(number)
    print(divisors)


main()
