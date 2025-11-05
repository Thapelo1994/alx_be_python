# main.py
# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division safely, handling ZeroDivisionError and ValueError.

    Args:
        numerator: The numerator (can be string or numeric).
        denominator: The denominator (can be string or numeric).

    Returns:
        A string message with the result or an error description.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        try:
            # Attempt the division
            result = num / den
            return f"The result of {num} divided by {den} is: {result}"

        except ZeroDivisionError:
            # Handle division by zero error
            return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input error
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    # Example usage if the script is run directly
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))
    print(safe_divide("ten", 5))
    print(safe_divide(12, 2))
    print(safe_divide("twelve", 2))
    print(safe_divide(73, 5))
    
          
