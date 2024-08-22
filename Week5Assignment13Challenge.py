# OWLL Assignment 14
# Challenge: Handle negative exponents efficiently.

# Description: Develop a function named power that takes two integers,
# base and exponent, as input and returns base raised to the power of exponent

# Input: Prompt the user to enter two integers, base and exponent
base = int(input("Enter the base integer: "))
exponent = int(input("Enter the exponent integer: "))

# Processing: Check whether the exponent is negative
#   Create a function named power that takes two integers,
#   base and exponent, as input and returns base raised to the power of exponent

def power(base, exponent):
  if exponent < 0:
# negative exponent, use absolute value
    return 1 / (base ** abs(exponent))
  else:
    return base ** exponent

# Output: print result
print(power(base, exponent))