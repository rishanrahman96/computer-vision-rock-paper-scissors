import random
import cv2
from keras.models import load_model
import numpy as np
import time

class Rps():
    """This is the class for the whole game. It lets you track the user and computer score, as well as pass the\n
    choices list as default. This comes in handy later on when predicting if value is rock,paper or scissors"""

    def __init__(self,choices_list = ['rock','paper','scissors']):
        self.choices_list = choices_list[:3]  
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def stop_camera(self):
        """ stops the camera feed"""
        # After the loop release the cap object
        self.cap.release()

        # Destroy all the windows
        cv2.destroyAllWindows()

    def get_prediction(self):
        """Gets prediction which we can assign to user choice later on. Function starts with a countdown, and then uses camera\n
         to allow you to make the appropriate signal. Countdown will repeat every time so you are ready. """
        t = 3
        print("Get ready to make your choice!")
        while t > 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            if t == 0:
                ret, frame = self.cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                self.data[0] = normalized_image
                prediction = self.model.predict(self.data)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        # index of the list
        prediction = self.choices_list[ np.argmax(prediction) ]
        return prediction
    
    def get_winner(self, user_choice, comp_choice):
        """Function provides logic for the winner of RPS"""
        if user_choice == "rock":
            if comp_choice == 'scissors':
                self.user_wins += 1
                print(f"Nice, {user_choice} beats {comp_choice}, you win!")
                print(f"The score is {self.user_wins} {self.computer_wins}")
            elif user_choice == comp_choice:
                self.user_wins +=1
                self.computer_wins +=1
                print(f"It's a draw. You both chose {user_choice}")
                print(f"The score is {self.user_wins} {self.computer_wins}")
            else:
                self.computer_wins +=1
                print(f"Ouch, {comp_choice} beats {user_choice} You lose this round.")
                print(f"The score is {self.user_wins} {self.computer_wins}")

        if user_choice == "scissors":
                if comp_choice == "paper":
                    self.user_wins +=1
                    print(f"You have won, {user_choice} beats {comp_choice}.")
                    print(f"The score is {self.user_wins} {self.computer_wins}")
                elif comp_choice == user_choice:
                    self.user_wins +=1
                    self.computer_wins +=1
                    print(f"You both chose {user_choice}. It's a draw!")
                    print(f"The score is {self.user_wins} {self.computer_wins}")
                else:
                    self.computer_wins +=1
                    print(f"You have lost, {comp_choice} beats {user_choice}.")
                    print(f"The score is {self.user_wins} {self.computer_wins}")

        if user_choice == "paper":
                if comp_choice == "rock":
                    self.user_wins +=1
                    print(f"You have won, {user_choice} beats {comp_choice}.")
                    print(f"The score is {self.user_wins} {self.computer_wins}")
                elif comp_choice == user_choice:
                    self.user_wins +=1
                    self.computer_wins +=1
                    print(f"You both chose {user_choice}. It's a draw!")
                    print(f"The score is {self.user_wins} {self.computer_wins}")
                else:
                    self.computer_wins +=1
                    print(f"You have lost, {comp_choice} beats {user_choice}.")
                    print(f"The score is {self.user_wins} {self.computer_wins}")

        if self.user_wins == 3:
             print("Well done, you have won the game")

        elif self.user_wins ==3 and self.computer_wins ==3:
            print("You both tied the game")

        else: 
             print("Unlucky mate. You lost.")
        
                    
    def get_choices(self):
                """Takes computer and user inputs and passes them to the get_winner() function. Also uses while loop\n
                until criteria is satisfied"""
                while self.user_wins < 3 and self.computer_wins <3:
                    user_choice = self.get_prediction()
                    comp_choice = random.choice(self.choices_list)
                    self.get_winner(user_choice,comp_choice)

game = Rps(['rock','paper','scissors'])
game.get_choices()
game.stop_camera()