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
from Food import Food
from Food_utilities import read_foods
from Food_utilities import calories_by_origin
# Constants

filename = "foods.txt"
file_variable = open(filename, "r", encoding="utf-8")
foods = read_foods(file_variable)

origin = 8
avg = calories_by_origin(foods, origin)

print(f"Average calories for {Food.ORIGIN[origin]}:{avg}")
