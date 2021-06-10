"""
Name:       Rock Paper Scissors
Purpose:    This is a game of rock paper scissors
Author:     Shelley Zeng
Created:     21.05.2021
"""
import random
# List of computer moves
COMPUTER_MOVES = ["Rock", "Paper", "Scissors"]

# Quick little intro of game and what to type to play certain moves
print("This is a game of rock paper scissors.")
print("If you want to play rock type 'R'. \nIf you want to play paper type 'P'. \nIf you want to play scissors type 'S'")
print("Rock beats scissors. Scissors beats paper. Paper beats rock.")

# Ask user to type chosen move
user_rps_move = input("Type your choice: ")

# Randomises a choice from the list of computer moves and prints move
computer_move = random.choice(COMPUTER_MOVES)
print(computer_move)

# If user and program type same move it is a tie
if user_rps_move == "r" and computer_move == "Rock" or user_rps_move == "p" and computer_move == "Paper" or user_rps_move == "s" and computer_move == "Scissors":
    print("tie")

# If program uses a move that beats user print "i win!"
elif user_rps_move == "r" and computer_move == "Paper" or user_rps_move == "p" and computer_move == "Scissors" or user_rps_move == "s" and computer_move == "Scissors":
    print ("I win! ")

# If user uses a move that beats program print "Good game! You win"
else:
    print("Good game! You win.")
