# OWLL Assignment 10
# Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
# Input: Prompt the user to enter their age.
# Processing: Classify the age into different categories:
# Under 18: Minor
# 18-65: Adult
# Above 65: Senior citizen
# Output: Display the category based on the entered age.

# Input: Prompt the user to enter their age

age = int(input("Enter your age in years: "))
# Check if the input is positive
if age <= 0:
  print("Invalid input, reenter a positive number.")
else:
  age = int(age)

# Processing: Classify the age into different categories:
# Under 18: Minor
# 18-65: Adult
# Above 65: Senior citizen

  if age < 18:
    age_category = "Minor"
  elif age >= 18 and age <= 65:
    age_category = "Adult"
  elif age > 65:
    age_category = "Senior Citizen"

# Output: Display the category based on the entered age
  print("Based on your age of", age, "your age category is: ", age_category)