
import random
import time
import cv2
from keras.models import load_model
import numpy as np


class Rock_Paper_Scissors:

    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.rps_choices = ["rock", "paper", "scissors", "nothing"]
        self.round = 1

    @staticmethod                                    # no need to pass 'self' as this method essentially stands alone and is not related to the instance of the class
    def countdown(time_amount=3):
        """A simple countdown from 3 seconds"""
    
        print("\nIn 3 seconds, pick Rock, Paper or Scissors\n")

        while time_amount != 0:
            mins, secs = divmod(time_amount, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            time_amount -= 1
           
    def get_computer_choice(self):
        '''This chooses the computer's choice of rock, paper, or scissors aand returns it'''
        computer_choice = random.choice(self.rps_choices[0:3])          #range through list of rps_choices from 'rock', 'paper' and 'scissors', excluding 'nothing'
        return computer_choice

    def get_prediction(self, time_amount=3):
        """This interprets the users choice from the webcam and prints rock, paper or scissors based on the highest probability that the user is showing it"""

        model = load_model('keras_model.h5')               #these 3 lines could be in the init method (w/out initialising them) for if we'd like to see the model/data info
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        end_time = time.time() + 5
        
        while end_time > time.time():
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)

            cv2.putText(frame, f"Round {self.round}", (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(frame, f"Your wins: {self.user_wins}", (60, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.putText(frame, f"Computer wins: {self.computer_wins}", (60, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.imshow('frame', frame)
            
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                 
    
        rps_prediction_index = np.argmax(prediction)
        user_choice = self.rps_choices[rps_prediction_index]
        return user_choice


    def get_winner(self, user_choice, computer_choice): 
        """This compares the users choice and the computers choice, and decides the winner"""


        if user_choice == computer_choice:
            print(f"\nYou and the computer both chose {computer_choice}. It's a tie!\n")
            self.round +=1


        elif user_choice == "rock" and computer_choice == "paper":
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou lose!\n")
            self.computer_wins += 1
            self.round +=1
            print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                
        elif user_choice == "rock" and computer_choice == "scissors":
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou win!\n")
            self.user_wins +=1
            self.round +=1
            print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                                    
        elif user_choice == "paper" and computer_choice == "scissors":
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou lose!\n")
            self.computer_wins += 1
            self.round +=1
            print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                    
        elif user_choice == "paper" and computer_choice == "rock":
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou win!\n")
            self.user_wins +=1
            self.round +=1
            print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                    

        elif user_choice == "scissors" and computer_choice == "rock":
            print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou lose!\n")
            self.computer_wins += 1
            self.round +=1
            print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')
                
        elif user_choice == "scissors" and computer_choice == "paper":
                print(f"\nYou chose {user_choice} and the computer chose {computer_choice}.\n\nYou win!\n")
                self.user_wins +=1
                self.round +=1
                print (f'You have {self.user_wins} wins and the computer has {self.computer_wins} wins.\n')


def play_game(): 
    '''Calling this function will start the game of Rock, Paper, Scissors'''
    
    game = Rock_Paper_Scissors()
    print("Welcome to the Rock-Paper-Scissors Game! \nLet's begin...")
    
    while True:

        game.countdown()  
        
        if game.user_wins == 3:
            return "Congratulations! You won 3 rounds and are the overall winner!"
            break
        
        elif game.computer_wins == 3:
            return 'The computer won 3 rounds, and is thus the overall winner. Try again next time!' 
            break
        
        elif game.user_wins < 3 and game.computer_wins < 3:
            computer_choice = game.get_computer_choice()
            user_choice = game.get_prediction()
            game.get_winner(user_choice, computer_choice)

    # keeping the below lines in the play_game function keeps the camera window open and doesn't close it at each instance
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
      

print(play_game())

