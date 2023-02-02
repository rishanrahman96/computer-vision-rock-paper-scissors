import random

choices = ['rock','paper','scissors']

user_score = 0
computer_score = 0


def get_comp_choice(choices):
    computer_choice = random.choice(choices)
    return computer_choice


def get_user_input():
    user_choice = input("Choose your option: ")
    user_choice_validated = user_choice.lower()
    if user_choice_validated not in choices:
        print("Please choose a valid option")
    else:
        return user_choice_validated


def get_winner(user_input,comp_input):
    if user_input == "rock":
        if comp_input == "scissors":
            global user_score
            user_score += 1
            print(f"You have won, {user_input} beats {comp_input}.")
        elif comp_input == user_input:
            user_score +=1
            global computer_score
            computer_score +=1
            print(f"You both chose {user_input}. It's a draw!")
        else:
            computer_score += 1
            print(f"You have lost, {comp_input} beats {user_input}.")

    if user_input == "scissors":
        if comp_input == "paper":
            user_score +=1
            print(f"You have won, {user_input} beats {comp_input}.")
        elif comp_input == user_input:
            user_score +=1
            computer_score +=1
            print(f"You both chose {user_input}. It's a draw!")
        else:
            computer_score +=1
            print(f"You have lost, {comp_input} beats {user_input}.")

    if user_input == "paper":
        if comp_input == "rock":
            user_score +=1
            print(f"You have won, {user_input} beats {comp_input}.")
        elif comp_input == user_input:
            user_score +=1
            computer_score +=1
            print(f"You both chose {user_input}. It's a draw!")
        else:
            computer_score +=1
            print(f"You have lost, {comp_input} beats {user_input}.")

    if user_score == 3:
        print("Well done, you won")
    
    if computer_score == 3:
        print("Unlucky pal")



