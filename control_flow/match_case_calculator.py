num1 = 10
num2 = 5

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

# Use an if/elif/else statement to perform the calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."

# Print the result
print(f"The result is {result}.")