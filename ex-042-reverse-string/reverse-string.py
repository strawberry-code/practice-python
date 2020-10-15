# course: python self training
# exercise: 6
# date: Oct 4 2020
# username: shinigami
# name: Cristiano Cavo
# description: learn some useful python tricks
# filename: reverse-string.py

# declare some strings
str1 = "apples"
str2 = "peches, pommes et poitres"
str3 = "radar"

# define the string reverter function
def stringReverter(str):
	return str[::-1]

print(str1,"> reverted is >",stringReverter(str1))
print(str2,"> reverted is >",stringReverter(str2))
print(str3,"> reverted is >",stringReverter(str3))