# OWLL Assignment 13
# Challenge: Use a loop structure to compare characters from both ends of the string
# to determine whether it is a palindrome.

# Description: Write a program that prompts the user to enter a string
# and then checks whether it is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward.

# Input: Prompt the user to enter a string

string = input("Enter a string: ")

# Processing: Check whether the string is a palindrome
#   Compare the first and last characters iteratively
#   Need to know the length of the string to determine when the loop stops
#   Loop stops in middle of the palindrome
#   Python indices start at 0 (string processing; failed when using 1 and len(string)
left_character = 0
right_character = len(string) - 1

# Set a palindrome flag to True
palindrome = True

while left_character < right_character:
    # Output: print log of characters being compared for debugging
    print("Left character: ", string[left_character])
    print("Right character: ", string[right_character])
    if string[left_character] != string[right_character]:
        palindrome = False
        # Exit loop by setting while condition to False (left_character > right_character)
        # or use break (not taught yet)
        break
    else:
        left_character += 1
        right_character -= 1

if palindrome == True:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")