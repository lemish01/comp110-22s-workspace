"""EX02 - One Shot Wordle - budget wordle."""

__author__= "730407722"

secret_word = str("python") 

guess_word: str = input("What is your 6-letter guess?") 

print("What is your 6-letter guess?")

while len(guess_word) != len(secret_word):
    guess_word: str = input("That was not 6-letters! Try again: ")
    
i: int = 0

while i < len(secret_word):
    guess_word[i] == secret_word[i]





