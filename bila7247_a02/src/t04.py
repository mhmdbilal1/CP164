"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from Food_utilities import food_table
# Constants
filename = "foods.txt"
file_variable = open(filename, "r", encoding="utf_8")
foods = read_foods(file_variable)
food_table(foods)

file_variable.close()
