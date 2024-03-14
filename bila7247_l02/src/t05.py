"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Food_utilities import read_foods
# Constants


fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

stack_test(foods)
