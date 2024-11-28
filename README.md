# HANGMAN

REPOSITORY FOR MY HANGMAN GAME (AICORE)

Description
A simple Hangman game. So far, it consists of 2 functions (ask_for_input and check_guess) and a class called Hangman.

ask_for_input: This function prompts the player to type in a letter, then checks whether the input is valid. If the input is invalid, it asks for a valid input; otherwise, it moves to the next line of code.

check_guess: This function checks if the inputted letter is in the randomly selected word. If the letter is in the word, it updates the guessed letters in the class and notifies the player. The function also keeps track of how many lives are left (set to 5 by default in the Hangman class).
The Hangman class allows me to store important information about the current game, including:


class Hangman:
    def __init__(self, word_list, num_lives=5):   
        self.word = random.choice(word_list)  # The randomly selected word  
        self.word_guessed = ["_" for _ in self.word]  # Letters that have been correctly guessed
        self.num_letters = len(set(self.word))  # Unique letters remaining in the word
        self.num_lives = int(num_lives)  # The number of lives the player has left
        self.word_list = list(word_list)  # List of words in the game
        self.list_of_guesses = []  # The guesses the player has made, which I add to using the append method

        
Installation instructions

Usage instructions

File structure

License
Do what you want with it [:~]
