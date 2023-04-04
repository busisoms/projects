# Guess the Number Game

import random as r


def play_game():
    start_range = int(input("Choose a starting range: "))
    end_range = int(input("Choose an ending range: "))

    number_of_attempts = 3
    generated_number = r.randint(start_range, end_range)

    for attempt in range(1, number_of_attempts + 1):
        user_guess = int(
            input(f"\nGuess a number in the range of {start_range} to {end_range}: "))
        if user_guess < generated_number:
            print(
                f"Your guess is too low. You have {number_of_attempts - attempt} attempt(s) left.")
        elif user_guess > generated_number:
            print(
                f"Your guess is too high. You have {number_of_attempts - attempt} attempt(s) left.")
        else:
            print(
                f"Congratulations! You guessed the number in {attempt} attempt(s).\n")
            return True
    else:
        print(
            f"Sorry, you ran out of attempts. The number was {generated_number}.")
        return False


while True:
    if play_game():
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            play_again.lower() == "n"
            print("Thanks for playing!")
            quit()
# it was an enjoyable project
