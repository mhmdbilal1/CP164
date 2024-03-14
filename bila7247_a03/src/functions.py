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
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
# Constants
OPERATORS = "+-*/"


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """

    target = Stack()
    print("source1\tsource2\ttarget")

    while not source1.is_empty() or not source2.is_empty():
        value1 = source1.pop() if not source1.is_empty() else ""
        value2 = source2.pop() if not source2.is_empty() else ""
        target.push(value1)
        target.push(value2)
        print("{:<10}{:<10}{:<10}".format(value1, value2, target.peek()))
    while not target.is_empty():
        print("{:<10}{:<10}".format("", "", target.pop()))
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list = []
    stack_to_array(source, list)
    array_to_stack(source, list)
    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    clean_string = ''.join(char.lower() for char in string if char.isalnum())
    stack = Stack()

    for char in clean_string:
        stack.push(char)

    reversed_string = ''.join(stack.pop() for _ in range(len(stack._values)))

    return clean_string == reversed_string


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split()

    for element in elements:
        if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
            stack.push(float(element))
        elif element in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if element == '+':
                result = operand1 + operand2
            elif element == '-':
                result = operand1 - operand2
            elif element == '*':
                result = operand1 * operand2
            elif element == '/':
                result = operand1 / operand2

            stack.push(result)

    return stack.pop()


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    visited = {}

    # Use tuple to include the parent point for backtracking
    stack.push(('Start', None))

    while not stack.is_empty():
        current_point, parent = stack.pop()

        if current_point == 'X':
            path = [current_point]
            while parent is not None:
                path.insert(0, parent)
                current_point, parent = parent, visited[parent]
            return path[1:]  # Exclude 'Start' from the path

        if current_point not in visited:
            visited[current_point] = parent
            if current_point in maze:
                for branch in maze[current_point]:
                    stack.push((branch, current_point))

    return None
