# OWLL Assignment 12
# Challenge: Use nested loop structures to print the pattern efficiently and neatly.
# Allow the user to specify the character used for the pattern.

# Description: Develop a program that prompts the user to enter the number of rows for a pattern
# and then prints a pattern of asterisks (*) in the form of a right triangle.

# Input: Prompt the user to enter a positive number of rows and a character

number = input("Enter a positive number of rows: ")
character = input("Enter a character for the pattern: ")

# Check if the input is positive
# If numeric, convert to integer
if number.isnumeric():
  number = int(number)
# If negative, error message
  if number <= 0:
    print("Invalid input, reenter a positive number.")
  else:
# Processing: generate a right triangle consisting of the number of rows
# entered, using the character entered, until the number of rows reaches 0
    while number > 0:
# Output: print the row of the right triangle
      print(character * number)
      number -= 1
else:
  print("Invalid input, reenter a positive number.")