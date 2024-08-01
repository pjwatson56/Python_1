# OWLL Assignment #5
# Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
# Input: Prompt the user to enter a time duration in hours.
# Processing: Convert the time duration to minutes and seconds.
# Output: Display the converted time duration in minutes and seconds.

# This code checks for non-numeric input

# Input: Prompt the user to enter a time duration in hours.
hours = input("Enter a time duration in hours: ")

# Check if the input is numeric
if hours.isnumeric():
  hours = float(hours)

  # Processing: Convert the time duration to minutes and seconds
  minutes = (hours * 60)
  seconds = (minutes * 60)

  # Output: Display the converted time duration in minutes and seconds.
  print(hours,"Hour(s)",'equates to',minutes,"Minutes","and",seconds,"Seconds" )
else: # provide appropriate error messages
  print("Invalid input. Please enter numeric values only.")