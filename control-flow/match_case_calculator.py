# Get input from the user
num1 = 10
num2 = 5

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Try to convert the inputs to numbers, handling potential errors
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

# Get the operation from the user
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using a match case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")