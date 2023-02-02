import random

choices = ['rock','paper','scissors']

def get_comp_choice(choices):
    computer_choice = random.choice(choices)
    print(computer_choice)
    return computer_choice


def get_user_input():
    user_choice = input("Choose your option: ")
    user_choice_validated = user_choice.lower()
    if user_choice_validated not in choices:
        print("Please choose a valid option")
    else:
        print(user_choice_validated)
        return user_choice_validated

get_user_input()