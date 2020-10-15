# course: python self training
# exercise: 21
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program that acts as little librarian
# filename: electronic-rhymary.py

import json

def loadLibrary():
	with open('library.json') as json_file:
	    library = json.load(json_file)
	    for book in library['books']:
	        print('Title: ',book['name'])
	        print('Author: ',book['author'])
	        print('----')

loadLibrary()