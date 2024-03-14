"""
   -------------------------------------------------------
   [program description]
   -------------------------------------------------------
   Author:  Muhammad Bilal
   ID:      169047247
   Email:   bila7247@mylaurier.ca
   __updated__ = "2024-02-08"
   -------------------------------------------------------
   """
# Imports

# Constants


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x - 1, y) + recurse(x, y - 1)
    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if n == 0:
        ans = m
    else:
        ans = gcd(n, m % n)
    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    if not s:
        return 0
    else:
        if s[0].lower() in vowels:
            return 1 + vowel_count(s[1:])
        else:
            return vowel_count(s[1:])


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power < 0:
        ans = 1 / to_power(base, -power)
    elif power % 2 == 0:
        half_power = to_power(base, power // 2)
        ans = half_power * half_power
    else:
        ans = base * to_power(base, power - 1)
    return ans


def new_string(s):
    new = ""
    if s != '':
        if s[0].isalpha():
            char = s[0].lower()
            s = s[1:]
            new = char + new_string(s)
        else:
            s = s[1:]
            new = '' + new_string(s)
    return new


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    new = new_string(s)
    return new == new[::-1]


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = []
    if bag == []:
        new_set = []
    else:
        if bag[-1] not in bag[:-1]:
            new_set = bag_to_set(bag[:-1]) + [bag[-1]]
        else:
            new_set = bag_to_set(bag[:-1])
    return new_set
