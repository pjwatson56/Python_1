# OWLL Assignment 9
# Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
# Input: Ask the user to enter a single character.
# Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
# Output: Display whether the entered character is a vowel or a consonant.

# Input: Ask the user to enter a single character
character = input("Enter one character: ")

# Check if the input is a single character
if len(character) != 1 or not character.isalpha():
    print("Invalid input. Please enter a single character.")
else:
  # Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        print(character, "is a vowel")
    else:
        print(character, "is a consonant")