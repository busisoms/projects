def level():
    import random as r
    easy_words = ['cat', 'dog', 'tree', 'sun', 
                  'book', 'cup', 'hat', 
                  'car', 'bike', 'bird']
    medium_words = ['ocean', 'mountain', 'piano', 'camera', 
                    'diamond', 'violin', 'guitar', 
                    'jacket', 'restaurant', 'umbrella']
    hard_words = ['serendipity', 'onomatopoeia', 'supercilious', 'ubiquitous'
                  , 'idiosyncrasy', 'paradoxical', 'perfunctory', 
                  'quintessential', 'antediluvian', 'antediluvian']
    
    pick = input("Pick a difficulty:(easy, meduim, or hard) ").lower()
    if pick == "easy":
        return r.choice(easy_words)
    elif pick == "medium":
        return r.choice(medium_words)
    elif pick == "hard":
        return r.choice(hard_words)
    else:
        return f"Invalid entry, {pick} is not a valid difficulty.\nPlease pick a valid difficulty level."

def game():
    selected_word = level()
    display = ["_"]*len(selected_word)
    hangman = {1:"head", 2:" torso", 3:"left-arm", 4:"right-arm", 5:"left-leg", 6:"right-leg"}
    count_part = len(hangman)
    wrong_guesses = 0
    while count_part > 0:
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
                print(f"The word was {selected_word}")
        elif guess == selected_word:
            print("You Won!!")
            print(f"The word was {selected_word}")
            return True
        else:
            wrong_guesses += 1
            if wrong_guesses == 1:
                print(f"{hangman[1]}")
            elif wrong_guesses == 2:
                print(f"{hangman[1]}, {hangman[2]}")
            elif wrong_guesses == 3:
                print(f"{hangman[1]}, {hangman[2]}, {hangman[3]}")
            elif wrong_guesses == 4:
                print(f"{hangman[1]}, {hangman[2]}, {hangman[3]}, {hangman[4]}")
            elif wrong_guesses == 5:
                print(f"{hangman[1]}, {hangman[2]}, {hangman[3]}, {hangman[4]}, {hangman[5]}")
            elif wrong_guesses == 6:
                print(f"{hangman[1]}, {hangman[2]}, {hangman[3]}, {hangman[4]}, {hangman[5]}, {hangman[6]}")
                print("\nYou Lose, the man is hanged (x_x ;)")
                print(f"The word was {selected_word}")
                return False
            else:
                print("Invalid entry, please enter a letter.")
    quit()


while (game() == False or game() == True):
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        continue
    else:
        play_again.lower() == "n"
        print("Thanks for playing!")
        quit()
