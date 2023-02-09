import random

user_score = 0
computer_score = 0


def get_computer_choice():
    choices = ['Rock','Paper','Scissors']
    computer_choice = random.choice(choices)
    return computer_choice


def get_user_choice():
    user_input = input("Please select an option: ")
    return user_input
   

def get_winner(computer_choice,user_choice):
    if user_choice == "Rock":
        if computer_choice == "Scissors":
            global user_score
            user_score += 1
            print("You won!")
        elif computer_choice == user_choice:
            user_score +=1
            global computer_score
            computer_score +=1
            print("It is a tie!")
        else:
            computer_score += 1
            print("You lost")

    if user_choice == "Scissors":
        if computer_choice == "Paper":
            user_score +=1
            print("You won!")
        elif computer_choice == user_choice:
            user_score +=1
            computer_score +=1
            print("It is a tie!")
        else:
            computer_score +=1
            print("You lost")

    if user_choice == "Paper":
        if computer_choice == "Rock":
            user_score +=1
            print("You won!")
        elif computer_choice == user_choice:
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