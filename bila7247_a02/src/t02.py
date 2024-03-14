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
from Food_utilities import average_calories
# Constants

file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)
avg = average_calories(foods)
print(avg)
file_variable.close()
