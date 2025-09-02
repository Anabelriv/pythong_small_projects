# this is a game to guess a random number from 1 to 100 with user input and using the random library
import random

# create a random number
secret_number = random.randint(1, 100)

while True:
    try:
        # user input and change to int type
        user_value = int(input("Guess a number between 1 to 100:\n"))

        if user_value > secret_number:  # check if it's higher
            print("Number is too high")

        elif user_value < secret_number:  # check if it's lower
            print("Number is too low")

        elif user_value == secret_number:  # end of game!
            print("You guessed the right number!")
            break

    except ValueError:  # value type not integer was entered
        print("Please enter a valid number")
