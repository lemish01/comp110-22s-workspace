"""Utility class for numerical operations."""

from typing import Union

__author__ = "730407722"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values_list: list[float]):
        """Simpy Constructor."""
        self.values = values_list

    def __str__(self) -> str:
        """Produces a str representation of simpy."""
        return f"({self.values})"

    def fill(self, val_fill: float, num_fill: int) -> None:
        """Mutates simpy by filling in simpy's values with specific number a certain number of times."""
        self.values = []
        i: int = 0
        while i < num_fill:
            self.values.append(val_fill)
            i += 1
        return None
    
    def arange(self, start: float, stop: float, step=1.0) -> None:
        """Mutates simpy by filling in simpy's values with a specific number in a certain number of increments."""
        assert step != 0.0
        self.values = []
        temp = start
        self.values.append(temp)
        while temp < stop: 
            temp = temp + step
            self.values.append(temp)
        return None

    def sum(self) -> float:
        """Compute and return sum of all items in values attribute."""
        i: int = 0 
        while i < len(self.values):
            temp: float = 0.0
            temp = temp + self.values[i]
            i += 1
        return temp

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allows addition of simpy and float options."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.append(self.values[item] + rhs_values[item])
        return Simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload operator that allows the use of *** of simpy and floats."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.append(self.values[item] + rhs_values[item])
        return Simpy

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operation overload that produces a mask."""
        result: list[bool] = []
        i: int = 0
        while i < len(self.values):
            if isinstance(rhs, float):
                result.append(self.values[i] == rhs)
            else:
                result.append(self.values[i] == rhs.values)
            i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the greater relationship beteen each item in values attribute with some other simpy or float."""
        result: list[bool] = []
        i: int = 0
        while i < len(self.values):
            if isinstance(rhs, float):
                if self.values[i] >= rhs:
                    result.append(True)
                else:
                    result.append(False)
            i += 1
        return result

    def __getitem___(self, rhs: int) -> float:
        """Allows for the usage of the subscription operator on Simpy objects."""
        called: float = 0.0
        called = self.values[rhs]
        return called
    
    # def __getitem__(self, rhs: Union[unt, list[bool]]) -> Union[float, Simpy]:
    #"""Given a list of bools, expression will return a new Simpy Object of masked values."""
