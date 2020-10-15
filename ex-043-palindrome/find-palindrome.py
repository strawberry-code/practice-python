# course: python self training
# exercise: 7
# date: Oct 4 2020
# username: shinigami
# name: Cristiano Cavo
# description: something boring on find palindrome strings
# filename: find-palindrome.py

# define some strings
str1 = "apples"
str2 = "peches, pommes et poitres"
str3 = "radar"
str4 = "never odd or even"
str5 = "kayak"
str6 = "not a palindrome"

# define the string reverter function
def stringReverter(str):
	return str[::-1]

# define palindrome finder
def isPalindrome(str):
	if(str == stringReverter(str)):
		return True
	else:
		return False

print(str1,"is palindrome?",isPalindrome(str1))
print(str2,"is palindrome?",isPalindrome(str2))
print(str3,"is palindrome?",isPalindrome(str3))
print(str4,"is palindrome?",isPalindrome(str4))
print(str5,"is palindrome?",isPalindrome(str5))
print(str6,"is palindrome?",isPalindrome(str6))