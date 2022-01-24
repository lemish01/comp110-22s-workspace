"""EX01 - Chardle - A cute step toward Wordle""" 

_author_ = "730407722"
 
desired_word: str = input("Enter a 5-character word:") 

if len(desired_word) != 5:
    print("Error: Word must contain 5 characters")
    exit() 
 
entered_character: str = input("Enter a single character:")

print("Searching for "+ entered_character + " in " + desired_word)

sum: int = 0

if entered_character == desired_word[0]:
    sum = sum + 1
    print(entered_character + " found at index 0 ")     

if entered_character == desired_word[1]:
    sum = sum + 1
    print(entered_character + " found at index 1 ")
  
if entered_character == desired_word[2]:
    sum = sum + 1
    print(entered_character + " found at index 2 ")
      
if entered_character == desired_word[3]:  
    sum = sum + 1
    print(entered_character + " found at index 3 ")
    
if entered_character == desired_word[4]:
    sum = sum + 1
    print(entered_character + " found at index 4 ")  

if sum > 1:
    print(sum + " instance of " + entered_character + " found in " + desired_word) 

if sum == 1:
    print("1 instance of " + entered_character + " found in " + desired_word)

if sum == 0:
    print("No instance of " + entered_character + " found in " + desired_word )