import random

word_list = ["grape", "apple", "banana", "guava", "mango"]
word = random.choice(word_list)

guess = input("Enter a single letter: ")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


