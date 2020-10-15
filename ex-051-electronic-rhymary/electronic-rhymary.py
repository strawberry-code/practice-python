# course: python self training
# exercise: 15
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program that works as a rhymary for a given word set and a word given as input
# filename: electronic-rhymary.py

# define word set
wordSet = ["luna", "sole", "stella", "cielo", "cometa"]

# define main
def main():
	word = getWord()
	return matchesRhyme(wordSet, word)

# define word getter
def getWord():
	word = input("please, give a word: ")
	if(' ' in word):
		print("it seems to be more than a word...")
		getWord()
	else:
		return word

# define rhymary algorithm
'''
Defines what is the lenght of the rhyme that has to be checked. The default is rhymeLength = 3. Since the user could input a word lesser than the default (such as "to" or a "a"), we could no more use rhymeLength = 3. This is the reason of the code labeled ##1.
The algorithm works as follows:
	1. take the last n digits (n = rhymeLength) of the word given by the user
	2. for each word in the pre-defiend word set:
		a. take the last n digits of the i-wordInSet
		b. look if rhyme matches, if yes: return immediately true stopping the for-loop, else: continue with the next workd in the word set
	3. if no rhymes are found: return false
'''
def matchesRhyme(wordSet, word):
	rhymeLength = 3
	if(len(word) < rhymeLength): ##1
		rhymeLength = len(word)
	lastWordChars = giveLastNChars(word, rhymeLength)
	for wordInSet in wordSet:
		if(giveLastNChars(wordInSet, rhymeLength) == lastWordChars):
			print("rhyme found! ({0}, {1})".format(wordInSet, word))
			return True
	print("rhyme not found")
	return False

# define a function that gives last n chars of a give string
def giveLastNChars(string, nChars):
	return string[len(string) - nChars :]

main()


