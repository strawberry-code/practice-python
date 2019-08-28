# Author: Cristiano Cavo
# Date: 2019-08-28
# From: http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
# Notes: unfortunately I got a lot of fun and so I went beyond the goals of the
# proposed exercise

# This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other
# exercises are: Part 1, Part 2, and Part 4.
#
# In a previous exercise we explored the idea of using a list of lists as a
# “data structure” to store information about a tic tac toe game. In a tic tac
# toe game, the “game server” needs to know where the Xs and Os are in the
# board, to know whether player 1 or player 2 (or whoever is X and O won).
#
# There has also been an exercise about drawing the actual tic tac toe gameboard
# using text characters.
#
# The next logical step is to deal with handling user input. When a player (say
# player 1, who is X) wants to place an X on the screen, they can’t just click
# on a terminal. So we are going to approximate this clicking simply by asking
# the user for a coordinate of where they want to place their piece.
#
# As a reminder, our tic tac toe game is really a list of lists. The game starts
# out with an empty game board like this:
#
# game = [[0, 0, 0],
#         [0, 0, 0],
# 	      [0, 0, 0]]

# The computer asks Player 1 (X) what their move is (in the format row,col), and
# say they type 1,3. Then the game would print out
#
# game = [[0, 0, X],
# 	      [0, 0, 0],
#         [0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.
#
# Things to note:
#
# For this exercise, assume that player 1 (the first player to move) will always
# be X and player 2 (the second player) will always be O.  Notice how in the
# example I gave coordinates for where I want to move starting from (1, 1)
# instead of (0, 0). To people who don’t program, starting to count at 0 is a
# strange concept, so it is better for the user experience if the row counts and
# column counts start at 1. This is not required, but whichever way you choose
# to implement this, it should be explained to the player.  Ask the user to
# enter coordinates in the form “row,col” - a number, then a comma, then a
# number. Then you can use your Python skills to figure out which row and column
# they want their piece to be in.  Don’t worry about checking whether someone
# won the game, but if a player tries to put a piece in a game position where
# there already is another piece, do not allow the piece to go there.  Bonus:
#
# For the “standard” exercise, don’t worry about “ending” the game - no need to
# keep track of how many squares are full. In a bonus version, keep track of how
# many squares are full and automatically stop asking for moves when there are
# no more valid moves.

import tic_tac_toe_v1 as ttt
import os

BOARD_SIZE = 3

board = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]


def printSimpleBoard(board):
    os.system("clear")
    for i in range(BOARD_SIZE):
        print()
        for j in range(BOARD_SIZE):
            print(board[i][j] + " ", end="")
    print()


def playerMove(board, player):
    printSimpleBoard(board)
    done = False
    while not done:
        move = input(
            "player {} make a move (x, y) > ".format(player)
        ).split()  # I assume input is always valid two digits without comma, for example: 0 1
        row = int(move[0])
        col = int(move[1])
        if board[row][col] == "·":
            board[row][col] = player
            done = True
            printSimpleBoard(board)
        else:
            printSimpleBoard(board)
            print("you can't make this move (cell already occupied)")


def swap(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player


def play(board):
    player = "X"
    gameOver = False
    moves = 0
    winner = "·"
    while not gameOver:
        if moves == BOARD_SIZE * BOARD_SIZE:
            gameOver = True
        elif ttt.checkWin(board) == "X" or ttt.checkWin(board) == "O":
            gameOver = True
            winner = ttt.checkWin(board)
        else:
            playerMove(board, player)
            player = swap(player)
            moves = moves + 1
    return winner


def main():
    winner = play(board)
    if winner == "·":
        print("Withdraw")
    elif winner == "X":
        print("player X wins")
    elif winner == "O":
        print("player O wins")


main()
