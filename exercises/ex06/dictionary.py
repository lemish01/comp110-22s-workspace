"""idk."""

__author__ = "730407722"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Given a dictonary will return dictionary that inverts keys and values."""
    output: dict[str, str] = {} 
    for key in input:
        if input[key] in output:   
            raise KeyError("error: two keys were used")
        else:
            output[input[key]] = key 
    return output


def favorite_color(color: dict[str, str]) -> str:
    """Given a dictionary of names and colors, will return with color that is mentioned the most."""
    output: dict[str, int] = {}
    for name in color:
        if color[name] in output:
            output[color[name]] += 1
        else:
            output[color[name]] = 1
    counter: int = 0
    pop_color: str = ""
    for color_a in output:
        if output[color_a] > counter:
            counter = output[color_a]
            pop_color = color_a
    return pop_color 


def count(key: list[str]) -> dict[str, int]:
    """Given a list, will return with a dictionary of unique keys and value associated is count of the times key appears."""
    result: dict[str, int] = {}
    for item in key:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 