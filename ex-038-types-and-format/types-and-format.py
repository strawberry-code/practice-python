# course: python self training
# exercise: 2
# date: Oct 3 2020
# username: shinigami
# name: Cristiano Cavo
# description: learn how to declare variables of different types and how to formet-print them
# filename: types-and-format.py

# declare an integer
apples = 5

# declare a string
auntie = "Auntie Cleo"

# delcare a float
price = 2.7


def myFormattedPrint(a, b, c):
	print("{0} bought {1} apples and paid {2} euros for them".format(a, b, c))

myFormattedPrint(auntie, apples, price)