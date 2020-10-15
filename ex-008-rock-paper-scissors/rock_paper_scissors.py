# Author: Cristiano Cavo
# # Date: 2019-08-19
# From: http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using
# input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#
# Remember the rules:
# 1. Rock beats scissors
# 2. Scissors beats paper
# 3. Paper beats rock


def print_menu(choices):
    print("Welcome to rock paper scissors game")
    for choice, entry in choices.items():
        print(" " + str(choice) + ". " + str(entry))
    print(" > ")


def eval(a, b):
    if a == "scissors" and b == "rock":
        return "rock"
    if a == "scissors" and b == "paper":
        return "scissors"
    if a == "scissors" and b == "scissors":
        return "draw"

    if a == "rock" and b == "rock":
        return "draw"
    if a == "rock" and b == "paper":
        return "paper"
    if a == "rock" and b == "scissors":
        return "rock"

    if a == "paper" and b == "rock":
        return "paper"
    if a == "paper" and b == "paper":
        return "draw"
    if a == "paper" and b == "scissors":
        return "scissors"


def play():
    player1 = input("player 1 choice: ")
    player2 = input("player 2 choice: ")
    result = eval(player1, player2)
    if result == player1:
        print("player1 wins!")
    elif result == player2:
        print("player2 wins!")
    else:
        print("unknown command")


def menu():
    choices = {1: "new game", 2: "exit"}
    print("Welcome to rock paper scissors game")
    in_game = True
    while in_game:
        for choice, entry in choices.items():
            print(" " + str(choice) + ". " + str(entry))
        print(" > ")
        choice = int(input())
        if choice == 1:
            play()
        elif choice == 2:
            print("goodbye!")
            in_game = False
        else:
            print("unknown command...")


menu()
