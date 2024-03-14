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
from functions import file_analyze
# Constants


fv = open('foods.txt', 'r', encoding='utf-8')
print(file_analyze(fv))
fv.close()
