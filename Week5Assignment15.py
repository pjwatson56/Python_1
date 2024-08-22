# OWLL Assignment 15
# Challenge: Write the function using recursion.
# Description: Create a function named is_palindrome that takes a string as input
# and returns True if it is a palindrome, and False otherwise.

# Input: Prompt the user to enter a string

string = input("Enter a string: ")

# Processing: Check whether the string is a palindrome
#   Compare the first and last characters iteratively
#   Need to know the length of the string to determine when the loop stops
#   Loop stops in middle of the palindrome
#   Python indices start at 0 (string processing; failed when using 1 and len(string)

def is_palindrome(string):
# Set a palindrome flag to True
  palindrome = True
  left_character = 0
  right_character = len(string) - 1
  while left_character < right_character:
# Output: print log of characters being compared for debugging
#    print("Left character: ", string[left_character])
#    print("Right character: ", string[right_character])
    if string[left_character] != string[right_character]:
      palindrome = False
# Exit loop by setting while condition to False (left_character > right_character)
# or use break (not taught yet)
      break
    else:
      left_character += 1
      right_character -= 1
  return palindrome

# Output: Print the result
print(is_palindrome(string))