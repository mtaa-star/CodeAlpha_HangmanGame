
import random

def play_hangman():
    words = ["python", "computer", "internship", "program", "coding"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\nWelcome to the Hangman Game!")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_incorrect_guesses} incorrect guesses available.")

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Guessed letters:", ", ".join(guessed_letters) or "None")
        print("Incorrect guesses:", incorrect_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    else:
        print("\nGame over! You ran out of guesses.")
        print("The correct word was:", secret_word)

    print("\nThanks for playing!")


if __name__ == "__main__":
    play_hangman()
