# course: python self training
# exercise: 17
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: Write a simply cryptographic program based on the rot13 algorithm (rotate each charater of a string by 13 positions in the alphabet). The program must be capable of encrypt and decrypt.
# filename: electronic-rhymary.py

# define alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

# define the encrypt operator
def encrypt(plaintext):
	ciphertext = ""
	for c in plaintext:
		if(c in alphabet):
			ciphertext += alphabet[alphabet.find(c) + 13]
		else:
			ciphertext += c
	return ciphertext

# define the decrypt operator
def decrypt(ciphertext):
	plaintext = ""
	for c in ciphertext:
		if(c in alphabet):
			plaintext += alphabet[alphabet.find(c) + 13]
		else:
			plaintext += c
	return plaintext

# define cli menu
def menu():
	print("""
		Make your choice:
			- [1] encrypt
			- [2] decrypt
			- [3] exit
		""")
	c = int(input(" > "))
	if(c == 1):
		ciphertext = encrypt(input("please, give the plaintext:\n"))
		print("the cipertext is:\n------")
		print(ciphertext)
		print("------")
	elif(c == 2):
		plaintext = decrypt(input("please, give the ciphertext\n"))
		print("the plaintext is:\n------")
		print(plaintext)
		print("------")
	elif(c == 3):
		return
	else:
		print("operation not recognized")
	menu()

menu()

