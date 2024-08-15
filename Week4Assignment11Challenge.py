# OWLL Assignment 11 Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1.
# Handle cases where the user enters a non-numeric input.

# Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user.
# The Collatz sequence is generated iteratively by repeatedly applying the following rules:
# If the current number is even, divide it by 2.
# If the current number is odd, multiply it by 3 and add 1.

# Input: Prompt the user to enter a positive number

number = input("Enter a positive number: ")

# Check if the input is positive or non-numeric
# If numeric, convert to integer
if number.isnumeric():
  number = int(number)
# If negative, error message
  if number <= 0:
    print("Invalid input, reenter a positive number.")
  else:
# Processing: generate the Collatz sequence until it reaches 1
# If the current number is even, divide it by 2
# If the current number is odd, multiply it by 3 and add 1
# The modulus operator "%" returns the remainder obtained after division
# Loop until number = 1
    while number != 1:
      if number % 2 == 0:
        number = number // 2
      else:
        number = (number * 3) + 1
# Output: print the Collatz sequence number
      print("The number is:", number)
# If string entered is non-numeric, print error message
else:
  print("Invalid input, reenter a positive number.")