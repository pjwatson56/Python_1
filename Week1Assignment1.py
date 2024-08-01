# Week 1 Assignment 1
# Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
# Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
# Output: Display the calculated simple interest.
# Initially, there is no error processing for non-numeric user input

# Get user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest:", simple_interest)
