"""Some examples of tender, loving function definitions."""

def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name} !"



def spread_love(to: str, n: int) -> str: 
    """"Generates a string that repeats a lovng message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        # Concatenation
        love_note += love(to) + "\n"
        i+= 1
    return love_note  