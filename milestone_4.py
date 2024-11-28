import random

# DEFINING THE HANGMAN GAME CLASS

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = int(num_lives)
        self.word_list = list(word_list)
        self.list_of_guesses = []

