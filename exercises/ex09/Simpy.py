"""Utility class for numerical operations."""

from __future__ import annotations
from optparse import Values

from typing import Union

__author__ = "730407722"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __innit__(self, values_list: list[float]):
        """Simpy Constructor"""
        self.values = values_list

    def __str__(self) -> str:
        """Produces a str representation of simpy."""
        return f"({self.values})"

    # def fill(self, val_fill: float, num_fill: int) -> None:
    #     """Mutates simpy by filling in simpy's values with specific number."""
    
    #def arrange

    def sum(self) -> float:
        """Compute and return sum of all items in values attribute."""
        sum = sum(Values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        print("__add__ was called")
        return Union(self.values)
    
    def __pow__
