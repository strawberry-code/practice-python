# course: python self training
# exercise: 4
# date: Oct 4 2020
# username: shinigami
# name: Cristiano Cavo
# description: discover python potential over string processing and the 'in' keyword
# filename: find-vowels.py

# decalre a string
myRandomString = "qwertyuiopasdfghjklzxcvbnm"

def findVowels(str):
	vowels = "aeiouy"
	for carat in str:
		if carat in vowels:
			print(carat,"is a vowel")
		else:
			print(carat,"is a consonant")

findVowels(myRandomString)