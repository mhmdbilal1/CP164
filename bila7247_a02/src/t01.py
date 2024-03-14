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
from Food_utilities import by_origin
from Food_utilities import read_foods

# Constants
file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)

origin = 2
origins = by_origin(foods, origin)
for food in origins:
    print(food)

file_variable.close()
