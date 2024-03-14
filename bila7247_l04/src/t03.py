"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from Food_utilities import read_foods
# Constants


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


fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()
source = [1, 2, 3, 4, 5]
list_test(foods)
