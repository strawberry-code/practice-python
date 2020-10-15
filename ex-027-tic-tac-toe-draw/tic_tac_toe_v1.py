# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
# Notes: This is a "computational" version

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


BOARD_SIZE = 3


def getRow(board, row_number):
    row = []
    for i in range(BOARD_SIZE):
        row.append(board[row_number][i])
    return row


def getRows(board):
    rows = [[], [], []]
    for i in range(BOARD_SIZE):
        rows[i] = getRow(board, i)
    return rows


def getColumn(board, column_number):
    column = []
    for i in range(BOARD_SIZE):
        column.append(board[i][column_number])
    return column


def getColumns(board):
    columns = [[], [], []]
    for i in range(BOARD_SIZE):
        columns[i] = getColumn(board, i)
    return columns


def getDiags(board):
    diags = [[], []]
    for i in range(BOARD_SIZE):
        diags[0].append(board[i][i])
        diags[1].append(board[i][2 - i])
    return diags


def makeSoup(rows, columns, diags):
    soup = []
    soup = rows + columns + diags
    return soup


def checkWin(board):
    soup = makeSoup(getRows(board), getColumns(board), getDiags(board))
    X_HIT = ["X", "X", "X"]
    O_HIT = ["O", "O", "O"]
    if X_HIT in soup:
        return "X"
    if O_HIT in soup:
        return "O"
    else:
        return "·"
