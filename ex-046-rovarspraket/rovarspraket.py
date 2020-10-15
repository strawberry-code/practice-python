# course: python self training
# exercise: 10
# date: Oct 6 2020
# username: shinigami
# name: Cristiano Cavo
# description: implement the famous swedish grammar game
# filename: rovarspraket.py

# define some words
words = ["cane", "melograno", "assomigliare", "lingua", "rovarspraket", "hypoteses", "majestic"]

# define vowels
vowels = "aeiouy"

# define if a carat is a vowel
def isVowel(char):
	if(char in vowels):
		return True
	else:
		return False

# define translater
def rovarspraket(word):
	translatedWord = ""
	for charIndex in range(0, len(word)):
		char = word[charIndex]
		if(isVowel(char)):
			translatedWord = translatedWord + char
		else:
			translatedWord = translatedWord + char + "o" + char
	return translatedWord

# print the results
for word in words:
	print(rovarspraket(word))
