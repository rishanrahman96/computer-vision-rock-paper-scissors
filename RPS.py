import random

choices = ['rock','paper','scissors']

def get_comp_choice(choices):
    computer_choice = random.choice(choices)
    print(computer_choice)
    return computer_choice

get_comp_choice(choices)