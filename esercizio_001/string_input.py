# Author: Cristiano Cavo
# Date: 2019-08-17
# From: http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Create a program that asks the user to enter their name and their age. Print
# out a message addressed to them that tells them the year that they will turn
# 100 years old.
# Extras:
# 1. Add on to the previous program by asking the user for another number and
#    printing out that many copies of the previous message. (Hint: order of
#    operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.
#    (Hint: the string "\n is the same as pressing the ENTER button)

name = input("insert your name: ")
print(name)

age = input("insert your age: ")
print(age)


counter = input("how many copies of the messages do you want? ")

left_years = 100 - int(age)
msg1 = "there are left " + str(left_years) + " to be a centenarian"
print(msg1)

current_year = 2019
next_year = 2019 + int(left_years)
msg2 = "you will be 100 years old in " + str(next_year)
print(msg2)

for i in range(int(counter)):
    print(msg1)
    print(msg2)
