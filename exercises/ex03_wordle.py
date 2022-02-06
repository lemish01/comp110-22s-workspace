"""EX03 - Structured Wordle - improved budget wordle."""

__author__ = "730407722"


def contains_char(search_string: str, sing_char: str) -> bool:
    """Determines if character is found in guess word."""
    assert len (sing_char) == 1
    i: int = 0
    j: int = 0
    while i <= 2:
        if sing_char[i] == search_string[j]:
            return True 
    else:
        i += 1
        return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess_word: str, secret_word: str) -> str:
    """Determining accuracy of guess word to secret word through g/w/y boxes."""
    assert len(guess_word) == len(secret_word)
    i: int = 0
    box: str = ""
    while i < len(secret_word):
        if guess_word[i] == secret_word[i]:
            box += GREEN_BOX
        elif contains_char(secret_word, guess_word[i]):
            box += YELLOW_BOX
        else:
            box += WHITE_BOX  
        i += 1          
    return box 

# def input_guess (expected_length: int) -> str:
    """Prompting user for guess until word meets expected length"""
    
    

    