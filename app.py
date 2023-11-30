# The interaction of the user will be in the console where the user will be able to choose the option to choose paper, scissor or rock. And the user should be warned if he chooses an option that is not valid.
# The computer will choose randomly between the three options.
# At each round, the user must enter on of the optiones.
# Tha choice and the computer will be compared, and the winner will be informed if they won, lost, or tied with the opponent.
# The game will be played until the user chooses to stop playing.
# At the end of the game, the user will be informed of the number of games won, lost and tied.
# The algorithm must handle user inputs, putting them in lowercase and removing spaces, and informing the user if the input is not valid.

# Importing libraries
import random
import os
import time

# Defining variables
user_choice = ""
computer_choice = ""
user_wins = 0
computer_wins = 0
ties = 0
rounds = 0
valid_options = ["rock", "paper", "scissors"]
winner = ""

# Defining functions
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def print_rounds():
    print(f"Round: {rounds}")

def print_score():
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")

def print_choices():
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

def print_winner():
    print(f"Winner: {winner}")

def print_game():
    print_winner()
    print_choices()

def print_final_score():
    print("Final score:")
    print_rounds()
    print_score()
    if user_wins > computer_wins:
        print("You won!")

def print_intro():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("Good luck!")

# Defining game

# Intro 
clear()
print_intro()
time.sleep(3)
clear()

# Game

while True:
    clear()
    user_choice = input("Choose rock, paper or scissors: ").lower().strip()
    if user_choice not in valid_options:
        print("Invalid choice. Please choose rock, paper or scissors.")
        time.sleep(1)
        continue
    computer_choice = random.choice(valid_options)
    if user_choice == computer_choice:
        ties += 1
        winner = "tie"
        rounds += 1
    elif user_choice == "rock":
        if computer_choice == "paper":
            computer_wins += 1
            winner = "computer"
            rounds += 1
        else:
            user_wins += 1
            winner = "user"
            rounds += 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            computer_wins += 1
            winner = "computer"
            rounds += 1
        else:
            user_wins += 1
            winner = "user"
            rounds += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            computer_wins += 1
            winner = "computer"
            rounds += 1
        else:
            user_wins += 1
            winner = "user"
            rounds += 1
    clear()
    print_game()
    time.sleep(3)
    wish_2_continue = input("Do you want to play again? (y/n): ").lower().strip()
    while wish_2_continue!= "y" and wish_2_continue != "n":
        wish_2_continue = input("Invalid choice. Do you want to play again? Please choose y or n: ")
        time.sleep(1)

    if wish_2_continue == "n":
        clear()
        print_final_score()
        break
    else:
        continue
