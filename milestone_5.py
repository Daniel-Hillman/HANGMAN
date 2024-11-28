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

num_lives=0 #DELETE AFTER just here to take away errors for now 

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
      if game.num_lives == 0:
        print ("LOSER! :(")
        break
      if game.num_lives > 0:
        ask_for_input()
      if game.num_lives != 0 and game.num_letters != 0:
        print ("Congratulations, you won the game...and hopefully I got on the course")
        break
      
      
play_game(word_list)
