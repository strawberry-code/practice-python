# course: python self training
# exercise: 5
# date: Oct 4 2020
# username: shinigami
# name: Cristiano Cavo
# description: learn how to declare lists and how to iterate them
# filename: unstoppable-summation.py

# declare a list of numbers
myList = [1, 1, 2, 4]

# print the list
print(myList)

# declare a summatory that calculate the sum of all items of a given list
def unstoppableSummation(numbers):
	result = 0
	for number in numbers:
		result = result + number
	return result

print("the overall sum of the items in the list above results:",unstoppableSummation(myList))
