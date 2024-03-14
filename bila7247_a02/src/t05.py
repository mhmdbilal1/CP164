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
from Food_utilities import food_search
# Constants
filename = "foods.txt"
file_variable = open(filename, "r", encoding="utf-8")

foods = read_foods(file_variable)
origin = 8
max_cals = 500
is_veg = True

result = food_search(foods, origin, max_cals, is_veg)

for item in result:
    print(item)
file_variable.close()
