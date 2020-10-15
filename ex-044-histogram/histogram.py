# course: python self training
# exercise: 8
# date: Sat Oct 4 2020
# username: shinigami
# name: Cristiano Cavo
# description: draw a CLI histogram starting from a list of numebrs
# filename: cli-histogram.py

# declare a list of numbers
numbers = [1, 8, 4, 7, 3, 6]

# define the histogram drawer
def histogram(list, symbol):
	for val in list:
		print("[{0}]".format(val),"> ", end="")
		for i in range(val):
			print(symbol, end="")
		print("")

histogram(numbers, "o")
histogram(numbers, "#")
histogram(numbers, "x ")
