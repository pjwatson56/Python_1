#Input

user_input = input("Enter a positive integer: ")
while True:
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break
        else:
            user_input = input("The number must be a positive integer. Enter again: ")
    else:
        user_input = input("Invalid input. Please enter a positive integer: ")
print("Collatz Sequence: ")
while number != 1:
    print(number, end=" -> ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
print(1)