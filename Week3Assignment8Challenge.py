# OWLL Assignment 8
# Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
# Input: Ask the user to enter their marks for three subjects.
# Processing: Calculate the average of the marks. Determine the grade based on the average:
# 90 and above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Output: Display the calculated grade.

# Input: Ask the user to enter their marks for three subjects

mark1 = int(input("Enter your first mark: "))
mark2 = int(input("Enter your second mark: "))
mark3 = int(input("Enter your third mark: "))
# Check if the input is valid (between 0 and 100)
if mark1 < 0 or mark1 > 100 or mark2 < 0 or mark2 > 100 or mark3 < 0 or mark3 > 100:
  print("Invalid input, reenter marks between 0 and 100.")
else:
  mark1 = int(mark1)
  mark2 = int(mark2)
  mark3 = int(mark3)

# Processing: Calculate the average of the marks. Determine the grade based on the average:
# 90 and above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

  average = int(mark1 + mark2 + mark3) / 3

# Determine grade
  if average >= 90:
    grade = "A"
  elif average >= 80:
    grade = "B"
  elif average >= 70:
    grade = "C"
  elif average >= 60:
    grade = "D"
  else:
    grade = "F"

# Output: Display the calculated BMI and BMI category
  print("Based on your marks average of", average,"your grade is:  ", grade)