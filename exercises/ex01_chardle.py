"""EX01 - Chardle - A cute step toward Wordle.""" 

__author__ = "730407722"
 
desired_word: str = input("Enter a 5-character word:") 

if len(desired_word) != 5:
    print("Error: Word must contain 5 characters")
    exit() 
 
entered_character: str = input("Enter a single character:")

if len(entered_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + entered_character + " in " + desired_word)

character_sum: int = 0

if entered_character == desired_word[0]:
    character_sum = character_sum + 1
    print(entered_character + " found at index 0 ")     

if entered_character == desired_word[1]:
    character_sum = character_sum + 1
    print(entered_character + " found at index 1 ")
  
if entered_character == desired_word[2]:
    character_sum = character_sum + 1
    print(entered_character + " found at index 2 ")
      
if entered_character == desired_word[3]:  
    character_sum = character_sum + 1
    print(entered_character + " found at index 3 ")
    
if entered_character == desired_word[4]: 
    character_sum = character_sum + 1
    print(entered_character + " found at index 4 ")  

if character_sum > 1:
    print(str(character_sum) + " instances of " + entered_character + " found in " + desired_word) 

if character_sum == 1:
    print("1 instance of " + entered_character + " found in " + desired_word)

if character_sum == 0:
    print("No instances of " + entered_character + " found in " + desired_word)
