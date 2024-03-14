"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports

# Constants
from BST_linked import BST
from morse import fill_code_bst, decode_morse, DATA1

bst = BST()

# Step 2: Fill the BST with Morse code data sorted by Morse code
fill_code_bst(bst, DATA1)

# Step 3: Decode a Morse code string into English text
morse_code = "... --- ..."
decoded_text = decode_morse(bst, morse_code)
print(f"Morse Code: {morse_code}")
print(f"Decoded Text: {decoded_text}")
