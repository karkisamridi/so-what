import random

print("Welcome to the Rock, Paper, Scissors game!")
print("Enter your choice (rock, paper, or scissors):")

choices = ["rock", "paper", "scissors"]
player_choice = input().lower()
computer_choice = random.choice(choices)

print("You chose:", player_choice)
print("The computer chose:", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("You lose! Paper covers rock.")
    else:
        print("You win! Rock smashes scissors.")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("You lose! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")
else:
    print("Invalid input. Please enter either rock, paper, or scissors.")