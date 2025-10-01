# Define functions with def


def add(a, b):
    """Adds two numbers and returns the sum."""
    return a + b


def main():
    """Main function to demonstrate calculations."""
    num1 = 5
    num2 = 6

    # Call the calculation functions
    sum_val = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_val}")




if __name__ == "__main__":
    main()