# Rock paper scissors game refactored doing modulazation to be able to debug the code easier, the game plays a user with
# his input and the computer, the options are presented with emojis.
import random

# constants
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
# emojis dictionary
emojis = {ROCK: "🪨", PAPER: "📜", SCISSORS: "✂"}
# get the values from the dictionary into a tuple
choices = tuple(emojis.keys())


def get_user_choices():
    # input value
    user_choice = input("Chose rock, paper or scissors r/p/s:\n").lower()
    # check if it's valid input
    while True:
        if user_choice in choices:
            return user_choice
        else:
            print("Please select a valid option")


def print_choices(user_choice, pc_choice):
    return print(
        f"You chose {emojis[user_choice]} \nComputer chose {emojis[pc_choice]}"
    )


def determine_winner(user_choice, pc_choice):
    if user_choice == pc_choice:
        print("It's a draw!")
    elif (
        (user_choice == ROCK and pc_choice == SCISSORS)
        or (user_choice == PAPER and pc_choice == ROCK)
        or (user_choice == SCISSORS and pc_choice == PAPER)
    ):
        print("You win!")
    else:
        ("You lose!")


def play_game():
    while True:
        try:
            # get user_choice
            user_choice = get_user_choices()
            # computer choice
            pc_choice = random.choice(choices)

            # print choices
            print_choices(user_choice, pc_choice)
            # check who wins
            determine_winner(user_choice, pc_choice)
            # continue y/n
            continue_game = input("Do you want to continue? y/n: \n").lower()
            if continue_game != "y":
                break

        except ValueError:
            print("You selected an invalid choice!")


play_game()

