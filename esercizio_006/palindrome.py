# Author: Cristiano Cavo
# Date: 2019-08-18
# From: http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

# Ask the user for a string and print out whether this string is a palindrome or
# not. (A palindrome is a string that reads the same forwards and backwards.)


def inputString():
    return input("write something:\n > ")


def isPalindrome(a):
    palindrome = True
    for i in range(int(len(a) / 2)):
        if a[i] != a[len(a) - 1 - i]:
            palindrome = False
            break
    return palindrome


def main():
    string = inputString()
    print(isPalindrome(string))


main()
