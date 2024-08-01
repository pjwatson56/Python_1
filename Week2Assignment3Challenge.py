# OWLL Assignment #3
#Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
#Input: Prompt the user to enter their weight in kilograms and height in meters.
#Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI.

# Input: Prompt the user to enter their weight in kilograms and height in meters
# 1 kilogram = 2.2 lbs
# 1 meter = 1.28 ft

weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2)
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
  bmi_category = "Under Weight"
elif bmi >= 18.5 and bmi < 25:
  bmi_category = "Normal Weight"
elif bmi >= 25 and bmi < 30:
  bmi_category = "Over Weight"
elif bmi > 30:
    bmi_category = "Obese"

# Output: Display the calculated BMI and BMI category
print("Based on your BMI of", bmi,"your BMI category is:  ", bmi_category)