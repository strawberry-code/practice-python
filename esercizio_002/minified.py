number = input("give me a number: ")
check = input("give me a check: ")
modulus = int(number) % 2
if modulus == 1:
    print("this number is odd 💛")
else:
    print("this number is even 💚")
modulus4 = int(number) % 4
if modulus4 == 0:
    print("this number is a multiple of 4 💚")
else:
    print("this number is not a multiple of 4 💛")
modulusCheck = int(number) % int(check)
if modulusCheck == 0:
    print("number " + str(number) + " is a multiple of " + str(check) + " 💚")
else:
    print("number " + str(number) + " is not a multiple of " + str(check) + " 💚")
# Created by pyminifier (https://github.com/liftoff/pyminifier)
