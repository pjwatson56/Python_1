# Assignment 19

# Challenge: Implement the sorting algorithm without using any built-in sorting functions.

# Description: Develop a function called sort_list that takes a list of numbers as input and
# returns a new list containing the same elements sorted in ascending order

# Research:
# https://www.geeksforgeeks.org/sort-a-list-in-python-without-sort-function/

# Approach: To sort the list without using a sort function, you need to know the number of elements in the list, and compare them iteratively to place them in ascending order.

def sort_list(numbers):
    # sort in ascending order
    numbers.sort()
    return numbers

# prompt user for input
input_list = input("Enter a list of numbers (comma-separated): ").split(',')

# convert input strings to integers
input_list = [int(x) for x in input_list]

# sort list
result = sort_list(input_list)
print("Sorted list:", result)

# Code below sorts list numbers without using a sort function
# with help from ChatGPT for the loop logic

def sort_list(numbers):
    # define a new list for the sorted numbers
    # [:] means all numbers in the list
    sorted_list = numbers[:]
    n = len(sorted_list)

    # examine the list elements, comparing/ordering them
    # with help from ChatGPT
    for i in range(n):
        # this loop runs as many times as there are elements in the list
        # after each pass, the last i elements are already sorted
        # the last i elements are already sorted and in their final positions.
        for j in range(0, n - i - 1):
            # examine the list from 0 to n-i-1
            # swap positions if the element found is greater than the next element
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list


# prompt user for input
input_list = input("Enter a list of numbers (comma-separated): ").split(',')

# convert input strings to integers
input_list = [int(x) for x in input_list]

# sort the list
result = sort_list(input_list)
print("Sorted list:", result)