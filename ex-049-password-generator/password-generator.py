# course: python self training
# exercise: 13
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program capable of generate different types of password
# filename: password-generator.py

# define digits
digits = "0987654321"

# define alphabet
alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

# define alphanumeric set
alphanumeric = digits + alphabet

# define symbols
symbols = alphanumeric + "\\!£$%&/()=?"

# define menu
def menu():
	print("""Welcome to the password generator:
 [1] generate a numeric only passowrd")
 [2] generate an alphabetcial passowrd")
 [3] generate an alphanumeric passowrd")
 [4] generate a ascii passowrd""")
	c = int(input("> "))
	l = int(input("password length?\n> "))
	if(c == 1):
		generator(digits, l)
	elif(c == 2):
		generator(alphabet, l)
	elif(c == 3):
		generator(alphanumeric, l)
	elif(c == 4):
		generator(symbols, l)
	else:
		print("command not found")
		return
	print("your password has been saved in the clipboard")

# define generator
import random
import pyperclip
def generator(set, length):
	password = ""
	for i in range(length):
		password += set[int(random.randrange(len(set)))]
	pyperclip.copy(password)


menu()