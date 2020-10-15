# course: python self training
# exercise: 3
# date: Oct 3 2020
# username: shinigami
# name: Cristiano Cavo
# description: learn how to make conditional ifs, be aware of colons, indentation! and elif!
# filename: max-from-2-and-3-integers.py

# declare some integers
apples = 2
watermelons = 3
lemons = 5

# compare apples and lemons, give the max
if(apples > lemons):
	print("we have more apples than lemons")
else:
	print("we have more lemons than apples")

# compare all!
if(apples > lemons and apples > watermelons):
	print("we have many apples!")
elif(lemons > apples and lemons > watermelons):
	print("we have many lemons!")
else:
	print("we have many watermelons!")