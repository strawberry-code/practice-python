# course: python self training
# exercise: 9
# date: Oct 6 2020
# username: shinigami
# name: Cristiano Cavo
# description: this is a program that, passed as a parameter a list of integers, outputs the greater of the numbers contained in the list.
# filename: number-list-find-max.py

# declare a list of random numbers from 0 to 100 having 50 elements

import random # import random library
numbers = random.sample(range(0, 100), 50) # generate 50 random numbers between 0 and 100
print(numbers) # print the generated list
maxNumber = max(numbers) # pick the greatest number in the list
print("the max in the list is:",maxNumber)