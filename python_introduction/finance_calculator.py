# Prompt for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt for total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with interest
interest_rate = 0.05
total_annual_income_saved = monthly_savings * 12
projected_annual_savings = total_annual_income_saved + (total_annual_income_saved * interest_rate)

# Display the results
print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after one year (including 5% interest) are: ${projected_annual_savings:.2f}")
