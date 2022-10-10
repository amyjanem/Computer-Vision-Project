# %%

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


# %%

