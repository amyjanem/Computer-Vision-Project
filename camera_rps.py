
import random
import time
import cv2
from keras.models import load_model
import numpy as np

def countdown(time_amount=3):
    """A simple countdown from 3 seconds"""
    
    print("\nIn 3 seconds, pick Rock, Paper or Scissors\n")

    while time_amount != 0:
        mins, secs = divmod(time_amount, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_amount -= 1


class Rock_Paper_Scissors:

    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.rps_choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        '''This chooses the computer's choice of rock, paper, or scissors aand returns it'''
        computer_choice = random.choice(self.rps_choices)
        return computer_choice

    def get_prediction(self, time_amount=3):
        """This interprets the users choice from the webcam and prints rock, paper or scissors based on the highest probability that the user is showing it"""

        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        countdown() #countdown function called here to start countdown while rest works in background?
        end_time = time.time() + 3
        
        while end_time > time.time():
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                 
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    
        rps_prediction_index = np.argmax(prediction)
        user_choice = self.rps_choices[rps_prediction_index]
        return user_choice


    def get_winner(self, user_choice, computer_choice): #needs to be updated to fit class?
        """This compares the users choice and the computers choice, and decides the winner"""

        while True:

            if user_choice == computer_choice:
                print(f"\nYou and the computer both chose {computer_choice}. It's a tie!\n")
                break

            elif user_choice == "rock":
                if computer_choice == "paper":
                    print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou lose!\n")
                    self.computer_wins += 1
                    print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                    break
                else:
                    print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou win!\n")
                    self.user_wins +=1
                    print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                    break
                        
            elif user_choice == "paper":
                    if computer_choice == "scissors":
                        print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou lose!\n")
                        self.computer_wins += 1
                        print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                        break
                    else:
                        print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou win!\n")
                        self.user_wins +=1
                        print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                        break

            elif user_choice == "scissors":
                if computer_choice == "rock":
                    print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou lose!\n")
                    self.computer_wins += 1
                    print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                    break
                else:
                    print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou win!\n")
                    self.user_wins +=1
                    print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                    break

            else:
                break



def play_game(): 
    '''Calling this function will start the game of Rock, Paper, Scissors'''
    
    game = Rock_Paper_Scissors()
    print("Welcome to the Rock-Paper-Scissors Game! \nLet's begin...")

    while True:
        
        if game.user_wins == 2:
            return "Congratulations! You won 3 rounds and are the overall winner!"
            break
        
        elif game.computer_wins  == 2:
            return 'The computer won 3 rounds, and is thus the overall winner. Try again next time!' 
            break
        
        elif game.user_wins < 2 and game.computer_wins < 2:
            computer_choice = game.get_computer_choice()
            user_choice = game.get_prediction()
            game.get_winner(user_choice, computer_choice)
      

print(play_game())

