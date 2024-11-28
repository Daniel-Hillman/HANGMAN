
#CHECK IF GUESS IS IN RANDOMLY SELECTED WORD & PRINT STATEMENTS

def check_guess(self, guess):
    guess = guess.lower()  
    if guess in self.word:  
        print(f"Good guess! {guess} is in the word.")
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1
    else:
        print(f"Sorry, {letter} is not in the word.")
        print(f"you have {num_lives} left")
        self.num_lives -= 1


#INPUT AND CHECKING IF INPUT IS A VALID GUESS

def ask_for_input(word):
    while True:
        guess = input("Guess a letter: ")  
        if len(guess) == 1 and guess.isalpha():  
            check_guess(guess)  
            break  
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input(word)
