"""EX03 - Structured Wordle - improved budget wordle."""

__author__ = "730407722"


def contains_char(secret_word: str, sing_char: str) -> bool:
    """Determines if character is found in guess word."""
    assert len(sing_char) == 1
    i: int = 0
    while i < len(secret_word):
        if sing_char == secret_word[i]:
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


def input_guess(expected_length: int) -> str:
    """Prompting user for guess until word meets expected length."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1
    secret_word: str = "codes"
    Win: bool = False
    while N <= 6 and not Win:
        print(f" === Turn {N}/6 === ")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            Win = True
        else:
            N += 1
    if Win is True:
        print(f"You won in {N}/6 turns!")
    else:
        print(" X/6 - Sorry, try again tomorrow!")    


if __name__ == "__main__":
    main()

    