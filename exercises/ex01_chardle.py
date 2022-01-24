"""EX01 - Chardle - A cute step toward Wordle""" 

_author_ = "730407722"
 
desired_word: str = input("Enter a 5-character word:") 
 
entered_character: str = input("Enter a single character:")

print("Searching for "+ entered_character + " in " + desired_word)
