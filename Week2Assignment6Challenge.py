# OWLL Assignment #6
# Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
# Input: Ask the user to enter an amount in one currency (e.g., USD).
# Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
# Output: Display the converted amount in the target currency.

# This code checks for invalid currency inputs. Currency pairs supported include:
# combinations of USD, EUR, GBP
# (USD, EUR), (USD, GBP), (EUR, USD), (EUR, GBP), (GBP, EUR), (GBP, USD)

# Input: Ask the user to enter an amount in one currency (e.g., USD)
amount = float(input("Enter an amount to be converted: "))
currency1 = input("Enter the first currency (USD, EUR, GBP): ")
currency2 = input("Enter the second currency (USD, EUR, GBP): ")

# Check if the input is a valid currency to proceed to processing
if currency1 in ["USD", "EUR", "GBP"] and currency2 in ["USD", "EUR", "GBP"]:

# Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate
  if currency1 == "USD" and currency2 == "EUR":
    rate = 0.93
    converted_amount = amount * rate
  elif currency1 == "USD" and currency2 == "GBP":
    rate = 0.78
    converted_amount = amount * rate
  elif currency1 == "EUR" and currency2 == "USD":
    rate = 1.07
    converted_amount = amount * rate
  elif currency1 == "EUR" and currency2 == "GBP":
    rate = 0.85
    converted_amount = amount * rate
  elif currency1 == "GBP" and currency2 == "EUR":
    rate = 1.18
    converted_amount = amount * rate
  elif currency1 == "GBP" and currency2 == "USD":
    rate = 1.27
    converted_amount = amount * rate

# Output: Display the converted amount in the target currency
  print(amount,currency1,'equates to',converted_amount,currency2)

# Check if the input is an invalid currency and print error message
if currency1 not in ["USD", "EUR", "GBP"] or currency2 not in ["USD", "EUR", "GBP"]:
    print("Invalid currency input. Please enter USD, EUR, or GBP")