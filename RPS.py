import random


class Rps():

    def __init__(self,choices_list):
        self.choices_list = ['rock','paper','scissors']
        self.user_score = 0
        self.computer_score = 0

    
    def get_winner(self, user_choice, comp_choice):
        if user_choice == "rock":
            if comp_choice == 'scissors':
                self.user_score += 1
                print(f"Nice, {user_choice} beats {comp_choice}, you win!")
            elif user_choice == comp_choice:
                self.user_score +=1
                self.computer_score +=1
                print(f"It's a draw. You both chose {user_choice}")
            else:
                self.computer_score +=1
                print(f"Ouch, {comp_choice} beats {user_choice} You lose this round.")

        if user_choice == "scissors":
                if comp_choice == "paper":
                    self.user_score +=1
                    print(f"You have won, {user_choice} beats {comp_choice}.")
                elif comp_choice == user_choice:
                    self.user_score +=1
                    self.computer_score +=1
                    print(f"You both chose {user_choice}. It's a draw!")
                else:
                    self.computer_score +=1
                    print(f"You have lost, {comp_choice} beats {user_choice}.")

        if user_choice == "paper":
                if comp_choice == "rock":
                    self.user_score +=1
                    print(f"You have won, {user_choice} beats {comp_choice}.")
                elif comp_choice == user_choice:
                    self.user_score +=1
                    self.computer_score +=1
                    print(f"You both chose {user_choice}. It's a draw!")
                else:
                    self.computer_score +=1
                    print(f"You have lost, {comp_choice} beats {user_choice}.")
        
                    
    def get_choices(self):
                while self.user_score <3 and self.computer_score < 3:
                    comp_choice = random.choice(self.choices_list)
                    user_choice = input("Enter a choice: ")
                    self.get_winner(user_choice,comp_choice)

    
                    


game = Rps(['rock','paper','scissors'])
game.get_choices()



        




