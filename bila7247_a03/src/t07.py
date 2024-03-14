"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
# Constants
sample_maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
               'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}

result = stack_maze(sample_maze)
print("Path:", result)  # Should print ['A', 'C', 'E', 'X']
