def word_game():
    import random as r

    words = [
        'happiness', 'adventure', 'chocolate',
        'universe', 'elephant', 'mountain',
        'harmony', 'rainbow', 'butterfly',
        'kindness', 'cathedral', 'mysterious',
        'fantastic', 'delicious', 'majestic',
        'brilliant', 'vibrant', 'delicate',
        'elegant', 'passionate'
    ]

    selected_word = r.choice(words)
    display = ["_"] * len(selected_word)
    attempts = 6

    while attempts > 0:
        guess = input("Enter a letter: ")
        found_letter = False
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                display[i] = guess
                found_letter = True

        if found_letter:
            print(" ".join(display))
            if "_" not in display:
                print("You won!")
                return True
        elif guess == selected_word:
            print("You Won!!")
            return True

        else:
            attempts -= 1
            print(
                f"{guess} is not in the word. Guess again.\nYou have {attempts} attempts left.")
            if "_" in display and attempts == 0:
                print("You Lose")
                return True


while True:
    if word_game():
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            play_again.lower() == "n"
            print("Thanks for playing!")
            quit()
