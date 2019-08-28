# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
# Notes: This is a "full predefined cases" version

# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other
# exercises are: Part 1, Part 3, and Part 4.
#
# As you may have guessed, we are trying to build up to a full tic-tac-toe
# board. However, this is significantly more than half an hour of coding, so
# we’re doing it in pieces.
#
# Today, we will simply focus on checking whether someone has WON a game of Tic
# Tac Toe, not worrying about how the moves were made.
#
# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
#         [2, 1, 0],
#         [2, 1, 1]]
#
# where a 0 means an empty square, a 1 means that player 1 put their token in
# that space, and a 2 means that player 2 put their token in that space.
#
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac
# Toe game board, tell me whether anyone has won, and tell me which player won,
# if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a
# diagonal. Don’t worry about the case where TWO people have won - assume that
# in every board there will only be one winner.
#
# Here are some more examples to work with:

winner_is_O = [["O", "O", " "], ["O", "X", " "], ["O", "X", "X"]]

winner_is_X = [["X", "O", " "], ["O", "X", " "], ["O", "X", "X"]]

winner_is_also_X = [[" ", "X", " "], ["O", "X", " "], ["O", "X", "X"]]

no_winner = [["X", "O", " "], ["O", "X", " "], ["O", "X", "O"]]

also_no_winner = [["X", "O", " "], ["O", "X", " "], ["O", "X", " "]]

BOARD_SIZE = 3


def checkWin(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[2][0]
    else:
        return 'anyone'


def main():
    print(checkWin(winner_is_O) + ' wins')
    print(checkWin(winner_is_X) + ' wins')
    print(checkWin(winner_is_also_X) + ' wins')
    print(checkWin(no_winner) + ' wins')
    print(checkWin(also_no_winner) + ' wins')


main()
