# course: python self training
# exercise: 19
# date: Oct 12 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program that returns the ASCII code of a given character
# filename: electronic-rhymary.py

def findAscii():
	c = input("give a charcater: ")
	a = ord(c)
	output = f"ASCII valuea of '{c}' is {a}"
	return output

print(findAscii())