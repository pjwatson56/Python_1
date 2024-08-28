# Assignment 17
# Challenge: Optimize the function to handle large input lists efficiently.

# Description: Develop a function called find_common_elements that takes two lists as input
# and returns a new list containing elements that are common to both input lists.

# Research finding comon elements in lists:
# https://www.geeksforgeeks.org/python-print-common-elements-two-lists/
# Convert the lists to sets and then print set1&set2. set1&set2 returns the common elements set, where set1 is the list1 and set2 is the list2. The & acts like a venn diagram.

# Research using a comma delimiter (so space isn't returned as a common element):
# https://www.simplilearn.com/tutorials/python-tutorial/split-in-python#:~:text=The%20split()%20function%20can,is%20returned%20as%20the%20output.


def find_common_elements(list1, list2):
    # convert lists to sets, and look for common elements (&)
    common_elements = set(list1) & set(list2)
    # convert the set of common elemnents back to a list
    return list(common_elements)

# Note that without any direction to the user regarding spacing, entering
# "1 2 3 4 5" and "5 6 7 8 9" results in 5 and a space being identified as common
# elements. Change code to include a delimiter, and then use split function to get rid of the delimiter.

# get two lists as input
# list_a = input("Enter the first list of elements: ")
# list_b = input("Enter the second list of elements: ")

list_a = input("Enter the first list of elements, using a comma between the numbers: ").split(',')
list_b = input("Enter the second list of elements, using a comma between the numbers: ").split(',')
# Convert string elements to their appropriate types (e.g., int, float, etc.) if needed
# Example: list_a = [int(x) for x in list_a]

common = find_common_elements(list_a, list_b)
print("Common elements:", common)