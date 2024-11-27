
def check_guess(guess, word):
    guess = guess.lower()  # Convert guess to lowercase
    if guess in word:
        print(f"Good guess!, {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


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
