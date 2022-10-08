# %%
# %%


import random

rps_choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    '''This chooses the computer's choice of rock, paper, or scissors aand returns it'''
    computer_choice = random.choice(rps_choices)
    return computer_choice
            
def get_user_choice():
    '''This asks the user for their choise between rock, paper, or scissors, and returns it'''
        
    user_choice = input("Rock, paper, scissors?\n For Rock: type r, for paper: type p, for scissors: type s")
    user_choice.lower()

    if user_choice.isalpha() == False or len(user_choice) != 1:
        print("Invalid. Please, enter r, p, or s.\n")
    else:
        return user_choice


def get_winner(user_choice, computer_choice):
    while True:

        if user_choice == computer_choice:
            print(f"The computer chose {computer_choice}. It's a tie!")
            break

        elif user_choice == "rock":
            if computer_choice == "paper":
                print(f"The computer chose {computer_choice}. You lose!")
                break
            else:
                print(f"The computer chose {computer_choice}. You win!")
                break

                                
        elif user_choice == "paper":
                if computer_choice == "scissors":
                    print(f"The computer chose {computer_choice}. You lose!")
                    break
                else:
                    print(f"The computer chose {computer_choice}. You win!")

        else:
            if computer_choice == "rock":
                print(f"The computer chose {computer_choice}. You lose!")
                break
            else:
                print(f"The computer chose {computer_choice}. You win!")
                

def play():
     
    while True:

        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        result = get_winner(user_choice, computer_choice)
        break

play()


# %%
