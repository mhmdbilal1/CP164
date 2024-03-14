"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants
matrix = [
    [1.5, 2.0, 3.0],
    [4.5, 5.5, 6.0],
    [7.5, 8.0, 9.5]
]


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


small, large, total, average = matrix_stats(matrix)

print("Smallest:", small)
