# REPOSITORY FOR MY HANGMAN GAME (AICORE)

## Description

A simple Hangman game. Right now, it has a class called Hangman and a few functions: ask_for_input, check_guess, and a few others to run the game.

## ask_for_input: 
This function asks the player to guess a letter. It checks if the input is valid (a single letter). If it's not valid, it asks the player to try again; otherwise, it moves to the next part of the game.


## check_guess: 
This function checks if the letter guessed by the player is in the randomly selected word. If the letter is correct, it updates the guessed word and notifies the player. It also tracks how many lives the player has left (5 lives by default). The Hangman class stores all the important info about the game, like the word to guess, the number of lives left, and the current state of the guessed word.


## play_game: 
This function ties everything together and runs the game. It sets up the number of lives, initializes the Hangman game, and continuously loops until the player either wins or loses the game. It checks if the player has no lives left (loss condition) or if they’ve guessed the word correctly (win condition).


## check_guess (updated): 
Checks if the guessed letter is in the word, updates the guessed word and decreases the number of lives if the guess is incorrect. It also ensures the game continues based on the number of lives and correct guesses.


class Hangman:
This class is used to store all the essential game information, such as:


The randomly chosen word.
The letters the player has guessed correctly so far.
The number of unique letters left to guess.
The number of lives the player has remaining.
The list of words available to choose from.
The list of guesses the player has made.
def check_guess(self, guess):
This function checks whether the guessed letter is in the word. If correct, it updates the guessed word and reduces the number of letters left to guess. If incorrect, it decreases the player's lives.


def ask_for_input(word):
This function asks the player for a letter guess, ensures it’s a valid input, and then calls the check_guess function to evaluate the guess.


def play_game(word_list):
This function sets up and runs the game. It initializes the Hangman class, starts with 5 lives, and continues to loop until the player either wins by guessing the word or loses by running out of lives.


## Installation instructions
Clone repository.
Make sure you have Python installed.
just run the script directly.
Usage instructions

Run the play_game() function to start the game.
Guess a letter when prompted.
You have 5 lives to guess the word correctly. Once you run out of lives or guess the word, the game will end.

#File structure
hangman.py: The main game logic including the Hangman class and functions.
README.md: This file, giving you a basic overview of the game.
License
Do what you want with it [:~
