# Computer Vision - Rock, Paper, Scissors Game

> This project creates the game of Rock, Paper, Scissors. This is firstly done using purely code, and the end result is using a camera to play against the computer.

## Milestone 1, 2 & 3

- Teachable Machine, a web-based tool used to make machine learning models, is used to gather examples in the form of pictures of the different classes of "Rock", "Paper", "Scissors", and "Nothing" (no sign shown)
- Data was collected using this tool and exported to be used at a later stage in the project.
- Further information on Teachable Machine can be found here: https://teachablemachine.withgoogle.com/
- A virtual environment was then created, and pip was used to install the following libraries: opencv-python, tensorflow, and ipykernel

## Milestone 4

- This task involved creating the game of Rock, Paper, Scissors manually. Ie. without the use of a camera, simply just code.
- This was done by creating two functions, get_computer_choice, which involved the computer randomly selecting between rock, paper or scissors, and get_user_choice, which asks the user for their choice and returns it.
- A function called get_winner is then used to compare these two choices to determine who wins.
- All three of these functions are then called within a function called play() where the code will print the winner.

```python

import random

rps_choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    '''This chooses the computer's choice of rock, paper, or scissors aand returns it'''
    computer_choice = random.choice(rps_choices)
    return computer_choice
            
def get_user_choice():
    '''This asks the user for their choise between rock, paper, or scissors, and returns it'''
        
    user_choice = input("Rock, paper, or scissors?")
    user_choice.lower()

    if user_choice in rps_choices:
        return user_choice
    else:
        print("Invalid. Please type rock, paper, or scissors")
        get_user_choice()
    

def get_winner(user_choice, computer_choice):
    """This compares the users choice and the computers choice, and decides the winner"""

    while True:

        if user_choice == computer_choice:
            print(f"You and the computer both chose {computer_choice}. It's a tie!")
            break

        elif user_choice == "rock":
            if computer_choice == "paper":
                print(f"You chose {user_choice} and the computer chose {computer_choice}.\nYou lose!")
                break
            else:
                print(f"You chose {user_choice} and the computer chose {computer_choice}.\nYou win!")
                break
                      
        elif user_choice == "paper":
                if computer_choice == "scissors":
                    print(f"You chose {user_choice} and the computer chose {computer_choice}.\nYou lose!")
                    break
                else:
                    print(f"You chose {user_choice} and the computer chose {computer_choice}.\nYou win!")
                    break

        elif user_choice == "scissors":
            if computer_choice == "rock":
                print(f"You chose {user_choice} and the computer chose {computer_choice}.\n You lose!")
                break
            else:
                print(f"You chose {user_choice} and the computer chose {computer_choice}.\nYou win!")
                break

        else:
            break
                
def play():
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        result = get_winner(user_choice, computer_choice)
        break

play()

```

> Insert screenshot of what you have built working.

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
