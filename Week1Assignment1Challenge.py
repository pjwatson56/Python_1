# Week 1 Assignment 1 with Challenge
# Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
# Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
# Output: Display the calculated simple interest.
# Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period,
# and provide appropriate error messages.

# This code checks for non-numeric input after inputting ALL 3 fields,
# not after EACH input field.

# Get user input
principal = input("Enter the principal amount: ")
rate = input("Enter the interest rate (in percentage): ")
time = input("Enter the time period (in years): ")

# Check if input is numeric
if principal.isnumeric() and rate.isnumeric() and time.isnumeric():
  principal = float(principal)
  rate = float(rate)
  time = float(time)

# Calculate simple interest
  simple_interest = (principal * rate * time) / 100

# Display result
  print("Simple Interest:", simple_interest)
else:
  print("Invalid input. Please enter numeric values only.")

# Code above evaluates for non numeric input only after user
# inputs all 3 fields.