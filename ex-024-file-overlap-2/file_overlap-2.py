# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other
# exercises are: Part 2, Part 3, and Part 4.
# Time for some fake graphics! Let’s say we want to draw game boards that look
# like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other
# sizes (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to
# the screen using Python’s print statement.
#
# Remember that in Python 3, printing to the screen is accomplished by
# print("Thing to show on screen") Hint: this requires some use of functions, as
# were discussed previously on this blog and elsewhere on the Internet, like
# this TutorialsPoint link.

import sys

SQUARE_BOARD_SIZE = (int(sys.argv[1]) * 2) + 1
HORIZONTAL_SYMBOL = "—"
VERTICAL_SYMBOL = "|"
EMPTY_SYMBOL = " "
PAWN_A = "X"
PAWN_B = "O"

board = []


def drawTop():
    for i in range(SQUARE_BOARD_SIZE):
        board.append(HORIZONTAL_SYMBOL)


def drawEmptyRow():
    token = 1
    for i in range(SQUARE_BOARD_SIZE):
        if token == 1:
            board.append(VERTICAL_SYMBOL)
            token = token * -1
        else:
            board.append(EMPTY_SYMBOL)
            token = token * -1


def drawEmptyBoard():
    drawTop()
    token = 1
    for i in range(SQUARE_BOARD_SIZE - 2):
        if token == 1:
            drawEmptyRow()
            token = token * -1
        else:
            drawTop()
            token = token * -1
    drawTop()


def printBoard():
    pivot = 0
    for i in range(SQUARE_BOARD_SIZE * SQUARE_BOARD_SIZE):
        if pivot == SQUARE_BOARD_SIZE:
            pivot = 0
            print()
        pivot = pivot + 1
        print(board[i], end=" ")
    print()


def main():
    drawEmptyBoard()
    printBoard()


main()
