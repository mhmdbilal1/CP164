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
from Food_utilities import read_foods, write_foods
# Constants

fw = open('new_foods.txt', 'w', encoding='utf-8')
fr = open('foods.txt', 'r', encoding='utf-8')

foods = read_foods(fr)
write_foods(fw, foods)
print("new_foods.txt created")

fr.close()
fw.close()
