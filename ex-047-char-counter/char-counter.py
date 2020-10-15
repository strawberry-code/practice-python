# course: python self training
# exercise: 11
# date: Oct 6 2020
# username: shinigami
# name: Cristiano Cavo
# description: implement a function that returns the occurences of charaters in a give string
# filename: char-counter.py

# define some strings
s1 = "apples"
s2 = "il rintocco della campana di gion"
s3 = "heike monogatari"
s4 = "appomattox"

# define the char counter
def charCounter(s):
	occurences = {}
	for c in s:
		if(c != " "):
			if c in occurences:
				occurences[c] += 1
			else:
				occurences[c] = 1
	return occurences

# do it
print(charCounter(s1))
print(charCounter(s2))
print(charCounter(s3))
print(charCounter(s4))