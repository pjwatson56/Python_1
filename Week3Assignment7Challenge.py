# OWLL Assignment 7
# Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.
# Input: Prompt the user to enter a year.
# Processing: Determine whether the entered year is a leap year or not.
# A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
# Output: Display whether the entered year is a leap year or not.

# Input: Prompt the user to enter a year
year = input("Enter a year: ")

# Check if the input is numeric
if year.isnumeric():
  year = int(year)

  # Processing: Determine whether the entered year is a leap year or not.
  # A leap year is (divisible by 4) but (not by 100 unless it is also divisible by 400)

  # To check if a year is a leap year, divide the year by 4. If it is fully divisible by 4, it is a leap year. For example, the year 2016 is divisible 4, so it is a leap year, whereas, 2015 is not.
  # However, Century years like 300, 700, 1900, 2000 need to be divided by 400 to check whether they are leap years or not.
  # to know whether the result is a whole number without a remainder, we need to
  # evaluate the remainder - a remainder  = 0 means the year was equally divisible by 4 (or 400).
  # The "modulo" operator (%) gives us the remainder of a division.

  if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):

  # Output: Display whether the entered year is a leap year or not
      print(year, "is a leap year")
  else:
      print(year, "is not a leap year")

else: # provide appropriate error messages
  print("Invalid input. Please enter numeric values only.")