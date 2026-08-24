# CodeAlpha_HangmanGame

A simple text-based **Hangman** game built in Python as part of the
CodeAlpha Python Programming Internship (Task 1).

## Description

The player tries to guess a secret word one letter at a time.
The word is chosen randomly from a small predefined list. The
player has 6 wrong guesses before the game ends.

## Features

- Random word selection from a predefined list of 5 words
- Tracks guessed letters and wrong guess count
- Displays the word progress (`_ _ t h _ n`) after every guess
- Handles invalid input (non-letters, repeated guesses)
- Option to play again after each round

## Concepts Used

`random`, `while` loops, `if-else`, strings, lists, sets

## How to Run

bash
python3 hangman.py

## Example
Welcome to Hangman!
Try to guess the word. You have 6 wrong guesses allowed.

Word: _ _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: None

Guess a letter: p
Good guess! 'p' is in the word.

## CodeAlpha_HangmanGame/
├── hangman.py
└── README.md
