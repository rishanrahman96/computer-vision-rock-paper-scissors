import random

user_score = 0
computer_score = 0


def get_computer_choice():
    choices = ['rock','paper','scissors']
    computer_choice = random.choice(choices)
    return computer_choice


def get_user_choice():
    user_input = input("Please select an option: ")
    return user_input
   

def get_winner(user_input,comp_input):
    if user_input == "rock":
        if comp_input == "scissors":
            global user_score
            user_score += 1
            print("You won!")
        elif comp_input == user_input:
            user_score +=1
            global computer_score
            computer_score +=1
            print("It is a tie!")
        else:
            computer_score += 1
            print("You lost")

    if user_input == "scissors":
        if comp_input == "paper":
            user_score +=1
            print("You won!")
        elif comp_input == user_input:
            user_score +=1
            computer_score +=1
            print("It is a tie!")
        else:
            computer_score +=1
            print("You lost")

    if user_input == "paper":
        if comp_input == "rock":
            user_score +=1
            print("You won!")
        elif comp_input == user_input:
            user_score +=1
            computer_score +=1
            print("It is a tie!")
        else:
            computer_score +=1
            print("You lost")

#     if user_score == 3:
#         print("Well done, you won")

#     if user_score ==3 and computer_score ==3:
#         print("You have both drawn the game.")

#     if computer_score ==3:
#         print("Unlucky pal")


# def play():
#     while user_score <3 and computer_score <3:
#         comp_choice = get_computer_choice()
#         user_choice = get_user_choice()
#         get_winner(user_choice,comp_choice)

# play()