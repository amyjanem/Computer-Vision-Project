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


## Milestone 5

- In this milestone, the webcam is made use of to play Rock, Paper, Scissors. The Teachable Machine model is imported and returns a list of probabilities of which sign the computer thinks the user is showing.

- The highest probability is extracted from this list using the argmax() function as shown in the code below:
```
  rps_prediction_index = np.argmax(prediction)
  user_choice = self.rps_choices[rps_prediction_index]
  return user_choice
```
This is then compared to the computer's choice, and a winner is returned.

- A countdown function is also created as below:
```
def countdown(time_amount=3):
    """A simple countdown from 3 seconds"""
    
    print("\nIn 3 seconds, pick Rock, Paper or Scissors\n")

    while time_amount != 0:
        mins, secs = divmod(time_amount, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_amount -= 1
```

- This is called in the get_prediction method, where the machine learning model is used, as below:
```
def get_prediction(self, time_amount=3):
        """This interprets the users choice from the webcam and prints rock, paper or scissors based on the highest probability that the user is showing it"""

        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        countdown()  
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
                 
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    
        rps_prediction_index = np.argmax(prediction)
        user_choice = self.rps_choices[rps_prediction_index]
        return user_choice
```

- The code also keeps track of how many wins each player has, as well as how many rounds have been played. This is with the addition of the below after each round:
```
self.computer_wins += 1
self.round +=1
```

or

```
self.user_wins += 1
self.round +=1
```

- The overall winner is then announced after a player wins 3 rounds. The below function is created:
```
def play_game(): 
    '''Calling this function will start the game of Rock, Paper, Scissors'''
    
    game = Rock_Paper_Scissors()
    print("Welcome to the Rock-Paper-Scissors Game! \nLet's begin...")

    while True:
        
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
```


- Some additional features were also added, namely the current round is shown in text on the webcam each time the camera opens. Also the amounts of wins for the user and the computer are displayed so that the user can visually keep track. These features were implemented using the putText() function.

## Conclusions

- This project improved my understanding of Python a lot more. I was exposed to the cv2 module, the argmax() function, and the putText() function, which are all very useful. I also understood the importance of creating classes and using branches to test out new bits of code. 
- Perhaps ways to further improve the code could be to show the countdown clock on the webcam screen rather than in the terminal, or perhaps the user could enter a key to continue to the next round when they are ready. 
