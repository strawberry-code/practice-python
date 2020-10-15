# course: python self training
# exercise: 14
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program capable of generate random mac addresses
# filename: mac-generator.py

# define digits
digits = "0987654321ABCDEF"

# define generator
import random
import pyperclip
def generator():
	mac = ""
	for i in range(6):
		for j in range(2):
			mac += digits[int(random.randrange(len(digits)))]
		if(i < 5):
			mac += ":"
	pyperclip.copy(mac)
	print("the generate MAC address is: ",mac,"and has been copied to the clipboard")
	return 

generator()