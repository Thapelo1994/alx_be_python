# finance_calculator.py

def calculate_savings():
    """
    Calculates monthly and projected annual savings based on user input.
    """
    # 1. User Input for Financial Details
    while True:
        try:
            monthly_income = float(input("Enter your monthly income: "))
            if monthly_income >= 0:
                break
            else:
                print("Income cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            monthly_expenses = float(input("Enter your total monthly expenses: "))
            if monthly_expenses >= 0:
                break
            else:
                print("Expenses cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 2. Calculate Monthly Savings
    monthly_savings = monthly_income - monthly_expenses
    print(f"\nYour monthly savings are: ${monthly_savings:.2f}")

    # 3. Project Annual Savings
    annual_savings_base = monthly_savings * 12
    annual_interest_rate = 0.05  # 5%
    
    # Simplified formula for annual savings projection
    projected_annual_savings = annual_savings_base + (annual_savings_base * annual_interest_rate)
    
    print(f"Your projected savings after one year (with {annual_interest_rate*100:.0f}% interest) are: ${projected_annual_savings:.2f}")

if __name__ == "__main__":
    calculate_savings()