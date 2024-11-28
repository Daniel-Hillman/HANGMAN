#REPOSITORY FOR MY HANGMAN GAME (AICORE)

##Description
A simple Hangman game that uses a Python class to manage the game logic. The code has been cleaned up and improved. It now features a fully functional Hangman game with better organization and clear gameplay flow.

##What's included:
A Hangman class that holds all the game data.
Methods like ask_for_letter, check_guess, and others to manage gameplay.
A main function, play_game, to bring it all together.

##Key Features:
Class: Hangman
This is the heart of the game. It holds everything important, including:

The randomly selected word players need to guess.
The current state of the guessed word (letters guessed correctly so far).
The number of unique letters left to guess.
The number of lives left (default: 5).
A list of all available words to choose from.
A list of guesses the player has made to avoid repeats.

##Methods:
check_guess(self, guess)

Checks whether the guessed letter is in the word.
If correct: Updates the guessed word and reduces the number of letters left to guess.
If incorrect: Decreases the number of lives and lets the player know they guessed wrong.

##ask_for_letter(self)

Prompts the player to guess a letter.
Ensures the input is valid (a single alphabetical character).
Passes the valid guess to check_guess for further handling.

##play_game(word_list)

Sets up and runs the game.
Initializes the Hangman class with 5 lives.
Loops until the player either:
Wins by guessing all the letters.
Loses by running out of lives.
Automatically ends the game with a message for either scenario:
"Congratulations, you won the game!"
"LOSER! :("


##Installation Instructions:
Clone this repository.
Make sure Python is installed on your system.
Run the script directly from your Python environment or terminal.

##Usage Instructions:
Call the play_game() function to start the game.
When prompted, guess one letter at a time.
You have 5 lives to guess the word correctly.
The game ends when you either guess the word or run out of lives.
File Structure:
hangman.py: Contains all the game logic, including the Hangman class and associated functions.
##README.md: 
This file, providing an overview of the game.

##License:
Do what you want with it. This is a project that helped me learn and practice Python concepts ;}
