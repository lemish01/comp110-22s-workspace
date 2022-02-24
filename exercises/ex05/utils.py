"""EX05 - List utility functions."""

__author__ = "730407722"


def only_evens(list_a: list[int]) -> list[int]:
    """Given a list of numbers, returns even numbers.""" 
    i: int = 0
    new_list: list[int] = list()
    while i < len(list_a):
        if list_a[i] % 2 == 0:
            new_list.append(list_a[i])
        i = i + 1
    return new_list 


def sub(list_a: list[int], start_i: int, end_i: int) -> list[int]:
    """Given a list and an integer, returns numbers in list at inputted integer."""
    new_list: list[int] = list() 
    i: int = 0 
    if start_i < 0:
        start_i = 0
    if end_i > len(list_a):
        end_i = len(list_a) 
    if len(list_a) == 0:
        return new_list 
    if start_i > len(list_a):
        return new_list
    if end_i <= 0:
        return new_list
    i = start_i
    while i < end_i:
        new_list.append(list_a[i])
        i = i + 1
    return new_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]: 
    """Given two list, generates a new list that contains all the elements from the two lists."""
    new_list: list[int] = list()
    for i in list_a:
        new_list.append(i)
    for i in list_b:
        new_list.append(i)
    return new_list 
     
