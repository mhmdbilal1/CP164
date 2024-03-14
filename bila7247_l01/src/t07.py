"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_vegetarian, read_foods


fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
fv.close()
vegs = get_vegetarian(foods)
for veg in vegs:
    print(veg)
    print()
