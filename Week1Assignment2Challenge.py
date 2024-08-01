# Amend error checking to check for *any non-numeric input
# This code checks for non-numeric input after inputting ALL 2 fields,
# not after EACH iknput field

# Input: Ask the user to enter the length and width of a rectangle
length = input("Enter the rectangle length: ")
width = input("Enter the rectangle width: ")

# Check if the input is numeric
if length.isnumeric() and width.isnumeric():
  length = float(length)
  width = float(width)

  # Processing: Calculate the area of the rectangle using the formula: Area = Length * Width
  area_of_rectangle = (length * width)

  # Output: : Display the calculated area of the rectangle.
  print("Rectangle area:", area_of_rectangle)

else: # provide appropriate error messages
  print("Invalid input. Please enter numeric values only.")

# Code above evaluates for non numeric input only after user inputs all 2 fields1-