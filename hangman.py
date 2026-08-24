import random

WORDS = ["python", "hangman", "internship", "keyboard", "developer"]
MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def display_state(word, guessed_letters, wrong_guesses):
    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )

    print("\nWord: " + display)
    print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
    print(
        f"Guessed letters: "
        f"{', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
    )


def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(
        f"Try to guess the word. "
        f"You have {MAX_WRONG_GUESSES} wrong guesses allowed."
    )

    while wrong_guesses < MAX_WRONG_GUESSES:
        display_state(word, guessed_letters, wrong_guesses)

        if is_word_guessed(word, guessed_letters):
            print(f"\nCongratulations! You guessed the word: '{word}'")
            return

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    print(f"\nGame over! You ran out of guesses. The word was: '{word}'")


# Corrected main condition
if __name__ == "__main__":
    play_again = "y"

    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").strip().lower()

    print("Thanks for playing!")
