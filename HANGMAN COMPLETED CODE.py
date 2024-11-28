
# IMPORTING RANDOM MODULE TO ALLOW RANDOM CHOOSING OF HANGMAN GAME WORD
import random 

# LIST OF FRUIT TO BE RANDOMLY CHOSEN WITH EACH GAME
word_list = ["grape", "apple", "banana", "guava", "mango"]


# DEFINING THE HANGMAN GAME CLASS. Here I can group everything necessary for a game.

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = int(num_lives)
        self.word_list = list(word_list)
        self.list_of_guesses = []

#HERE IS A FUNCTION THAT CHECKS THE PLAYERS GUESS TO SEE IF LETTER IS IN RAND WORD. IT ALSO STORES LETTER GUESSES TO STOP REOCCURING GUESSES

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:  
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

# HERE I DEFINE A FUNCTION FOR WHEN THE GAME NEEDS TO ASK THE PLAYER FOR A LETTER. IF LETTER HAS ALREADY BEEN GUESSED THE WHILE LOOP IS TRIGGERED            

    def ask_for_letter(self):
        while True:
            guess = input("Guess a letter: ")  
            if len(guess) == 1 and guess.isalpha():  
                if guess in self.list_of_guesses:
                    print("You already guessed that letter.")
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)  
                break  
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

# THIS IS THE MAIN FUNCTION TO START THE GAME, IT REGULATES WETHER THE GAME SHOULD CARRY ON OR END.                 

def play_game(word_list):
    game = Hangman(word_list, num_lives=5) # NUM_LIVES=5 : CHANGE THIS TO ADJUST HOW MANY LIVES THE PLAYER GETS
    print("Welcome to Hangman!")
    print("The word is: " + " ".join(game.word_guessed))
    
    while True:
        if game.num_lives == 0:
            print(f"Game over! The word was '{game.word}'.")
            break
        if game.num_letters == 0:
            print("Congratulations, you won the game!")
            break
        game.ask_for_letter()
        print("Current word: " + " ".join(game.word_guessed))

#FUNCTION TO GROUP OTHER FUNCTIONS AND BEGIN HANGMAN!

play_game(word_list)

