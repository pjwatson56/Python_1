# OWLL Assignment #4
# Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
# Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
# Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
# Output: Display the calculated distance between the two points

# Amend error checking to check for *any non-numeric input
# This code checks for non-numeric input after inputting ALL 4 fields,
# not after EACH input field

# Need to import the math module for the square root calculation
import math

# Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2)
x1 = input("Enter the first x coordinate: ")
y1 = input("Enter the first y coordinate: ")
x2 = input("Enter the second x coordinate: ")
y2 = input("Enter the second y coordinate: ")

# Check if the input is numeric
if x1.isnumeric() and y1.isnumeric() and x2.isnumeric() and y2.isnumeric():
  x1 = float(x1)
  y1 = float(y1)
  x2 = float(x2)
  y2 = float(y2)

  # Processing: Calculate the distance between the two points using the distance formula:
  # Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
  distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

  # Output: : Display the distance between the two points
  print("Distance between the two points:", distance)

else: # provide appropriate error messages
  print("Invalid input. Please enter numeric values only.")

# Code above evaluates for non numeric input only after user inputs all 4 fields