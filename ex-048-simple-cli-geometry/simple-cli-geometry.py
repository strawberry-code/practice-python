# course: python self training
# exercise: 12
# date: Oct 6 2020
# username: shinigami
# name: Cristiano Cavo
# description: implement a program be able to calculate area of a circle from given radius, area of a square from given edge, a rectangle form given edges and of a equilateral triangle froma given edge
# filename: char-counter.py

# define area of a circle with given radius
def circleArea(r):
	area = 3.14 * r * r
	return area

def squareArea(s):
	area = s * s
	return area

def rectangleArea(a, b):
	area = a * b
	return area

import math
def triangleArea(s):
	area = (math.sqrt(3)/4) * s * s
	return area

# define main menu
def menu():
    print("""
    Welcome to Simple CLI Geometry!
    Make a choice:
     [1] circlea area
     [2] square area
     [3] rectangle area
     [4] triangle area
    """)
    c = int(input('=> '))
    if(c == 1):
    	circleRadius = float(input("give the circle radius: "))
    	print("area of a circle with radius length of",circleRadius,"is: ",circleArea(circleRadius))
    elif(c == 2):
    	squareSide = float(input("give the square side: "))
    	print("area of a square with side length of",squareSide,"is: ",squareArea(squareSide))
    elif(c == 3):
    	rectangleSideA = float(input("give the rectangle side A: "))
    	rectangleSideB = float(input("give the rectangle side B: "))
    	print("area of a rectangle with side A of",rectangleSideA,"and side B of",rectangleSideB,"is: ",rectangleArea(rectangleSideA, rectangleSideB))
    elif(c == 4):
    	triangleSide = float(input("give the triangle side: "))
    	print("area of a triangle with side length of",triangleSide,"is: ",triangleArea(triangleSide))
    else:
    	print("undefined command, exit")

menu()
