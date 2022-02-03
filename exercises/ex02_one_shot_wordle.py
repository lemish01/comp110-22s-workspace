"""EX02 - One Shot Wordle - budget wordle."""

__author__ = "730407722"

secret_word = str("python") 

guess_word: str = input(f"What is your {len(secret_word)}-letter guess?") 

while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)}-letters! Try again: ")
    
i: int = 0
box: str = ("")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while i < len(secret_word):
    if guess_word[i] == secret_word[i]:
        box = box + GREEN_BOX
    else:
        j: int = 0
        found: bool = False 
        while j < len(secret_word):
            if guess_word[i] == secret_word[j]:
                found = True 
            j = j + 1
        if found:
            box = box + YELLOW_BOX
        else: 
            box = box + WHITE_BOX 
    i = i + 1

print(box)

if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon")
