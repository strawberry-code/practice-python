# course: python self training
# exercise: 16
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program that works as a rhymary for a given word set and a word given as input
# filename: electronic-rhymary.py

# define menu
def menu():
	print("""
distance converter:
 [1] metres to yards
 [2] yards to metres
 [3] centimetres to inches
 [4] inches to centimetres
 [5] kilometres to miles
 [6] miles to kilometres
 [0] exit
""")
	c = int(input(" > "))
	if(c == 0):
		return
	elif(c == 1):
		val = float(input("give metres: "))
		print(metresToYards(val),"yards")
	elif(c == 2):
		val = float(input("give yards: "))
		print(yardsToMetres(val),"metres")
	elif(c == 3):
		val = float(input("give centimetres: "))
		print(centimetresToInches(val),"inches")
	elif(c == 4):
		val = float(input("give inches: "))
		print(inchesToCentimetres(val),"centimetres")
	elif(c == 5):
		val = float(input("give kilometres: "))
		print(kilometresToMiles(val),"miles")
	elif(c == 6):
		val = float(input("give miles: "))
		print(milesToKilometres(val),"kilometres")
	menu()

def metresToYards(m):
	return float(m*1.09)

def yardsToMetres(y):
	return float(y/1.09)

def inchesToCentimetres(i):
	return float(i*2.54)

def centimetresToInches(c):
	return float(c/2.54)

def kilometresToMiles(k):
	return float(k/1.61)

def milesToKilometres(m):
	return float(m*1.61)

menu()
