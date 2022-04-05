"""Dictionary related utility functions."""

__author__ = "730407722."

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows fo a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")
   
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Reach each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(no_mut: dict[str, list[str]], rows_amt: int) -> dict[str, list[str]]:
    """Produces a new colum based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in no_mut:
        M: list[str] = []
        i: int = 0
        if len(no_mut[column]) < rows_amt:
            return no_mut
        while i < rows_amt:
            M.append(no_mut[column][i])
            i += 1
        result[column] = M
    return result 


def select(og: dict[str, list[str]], copy_over: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in copy_over:
        result[column] = og[column]
    return result 


def count(key: list[str]) -> dict[str, int]:
    """Given a list, will return with a dictionary of unique keys and value associated is count of the times key appears."""
    result: dict[str, int] = {}
    for item in key:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 


def filter(exp: list[str], threshold: str) -> list[bool]:
    result: list[bool] = []
    for student in exp:
        if student == threshold:
            result.append(True)
        else:
            result.append(False)
    return result 


def mask(understanding: list[str], check: list[bool]) -> list[str]:
    result: list[str] = []
    i: int = 0
    while i < len(check):
        if check[i]:
            result.append(understanding[i])
        i += 1
    return result


def mean(final: dict[str, list[str]]) -> dict[str, float]:
    results: dict[str, float] = {}
    for item in final:
        i: int = 0
        answer: int = 0
        if len(final[item]) == 0:
            results[item] = 0
        else:
            while i < len(final[item]):
                answer = int(final[item][i]) + answer
                i += 1
            results[item] = answer / len(final[item])
    return results
