# OWLL Assignment 16
# Challenge: Optimize the function to handle large input numbers efficiently.

# Description: Develop a function called is_prime that takes a positive integer as input
# and returns True if it is a prime number, and False otherwise.

# Input: Prompt the user to enter a positive integer
integer = int(input("Enter a positive integer: "))

# Processing: Check whether the exponent is negative
# Develop a function called is_prime that takes a positive integer as input
# and returns True if it is a prime number, and False otherwise.
# A prime number is a whole number *greater than 1* that cannot be exactly divided
# by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
# 1 is not considered prime

def is_prime(integer):
  if integer <= 1:
    return False
  if integer == 2 or integer == 3:
    return True
  for i in range(2, integer):
    if integer % i == 0:
# if the input integer is divisible by the current number i,
# the number is not prime
      return False
  return True
# Output: print result
print(is_prime(integer))