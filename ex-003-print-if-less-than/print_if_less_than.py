# Author: Cristiano Cavo
# Date: 2019-08-17
# From: http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less
# than 5.
# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all
#    the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements
#    from the original list a that are smaller than that number given by the
#    user.


check = int(input("give me a check: "))
raw_array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
processed_array = []
for elem in raw_array:
    if int(elem) < check:
        processed_array.append(elem)
# print(processed_array)

# tip: il tutto si poteva risolvere in una sola riga
# di codice, secondo il seguente pattern:
#   [output] for [item] in [list] if [filter]
# questa tecnica viene chiamata 'list comprehension'.
print([aa for aa in raw_array if aa < 5])
