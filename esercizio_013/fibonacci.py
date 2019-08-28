# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

# Write a program that asks the user how many Fibonnaci numbers to generate and
# then generates them. Take this opportunity to think about how you can use
# functions. Make sure to ask the user to enter the number of numbers in the
# sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers
# in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def getInt(message="give a number: "):
    return int(input(message))


def fibonacci(num):
    serie = []
    if num == 1:
        serie.append(1)
    else:
        serie.append(1)
        for i in range(num):
            serie.append(i + serie[i - 1])
    return serie


def main():
    print(fibonacci(getInt()))


main()
