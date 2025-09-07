# This is the classical game rock, papers, scissors playing against the computer using emojis

import random

# set up 3 values (rock, paper, scissors)
choices = ("r", "p", "s")
# emojis dictionary
emojis = {"r": "🪨", "p": "📜", "s": "✂"}


while True:
    # input value
    user_choice = input("Chose rock, paper or scissors r/p/s:\n").lower()
    # check if it's valid input
    try:
        if user_choice not in choices:
            print("Please select a valid option")
            continue
        # computer choice
        pc_choice = random.choice(choices)

        # print you chose -
        print(f"You chose {emojis[user_choice]}")
        # print computer chose
        print(f"Computer chose {emojis[pc_choice]}")

        # check who wins
        if user_choice == pc_choice:
            print("It's a draw!")
        elif (
            (user_choice == "r" and pc_choice == "s")
            or (user_choice == "p" and pc_choice == "r")
            or (user_choice == "s" and pc_choice == "p")
        ):
            print("You win!")
        else:
            ("You lose!")

        # continue y/n
        continue_game = input("Do you want to continue? y/n: \n").lower()
        if continue_game != "y":
            break

    except ValueError:
        print("You selected an invalid choice!")
