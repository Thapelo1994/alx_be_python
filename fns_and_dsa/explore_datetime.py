from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days, then calculates and displays a future date.
    """
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

# Call the functions
display_current_datetime()
calculate_future_date()
