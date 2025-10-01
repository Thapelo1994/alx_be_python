from datetime import datetime

# Get the current local date and time
current_datetime = datetime.now()

# Print the resulting datetime object
print("Current date and time:", current_datetime)


from datetime import datetime, timedelta

# Get the current local date and time
current_datetime = datetime.now()

# Add 10 days to the current datetime
future_datetime = current_datetime + timedelta(days=10)

# Print the original and modified datetime objects
print(f"Current datetime: {current_datetime}")
print(f"Datetime in 10 days: {future_datetime}")