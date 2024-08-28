# Assignment 18

# Challenge: Ensure that the function works correctly with tuples of different lengths.

# Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.

# Research tuples: https://www.w3schools.com/Python/python_tuples.asp
# Example:
# mytuple = ("apple", "banana", "cherry")

# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data (the other 3 are List, Set, and Dictionary, all with different qualities and usage).

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

def concat_tuples(tuple1, tuple2):
    # concatenate the two tuples into a new tuple containing all elements from both input tuples
    new_tuple = tuple1 + tuple2
    return new_tuple

# prompt user for input
# use what was learned in Assignment 17 about comma delimited input
tuple_a = tuple(input("Enter the first tuple of elements, separated by a comma: ").split(','))
tuple_b = tuple(input("Enter the second tuple of elements, separated by a comma: ").split(','))


result = concat_tuples(tuple_a, tuple_b)
print("New tuple:", result)