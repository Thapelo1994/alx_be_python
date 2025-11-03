def create_daily_reminder():
    """
    Prompts the user for task details and prints a formatted reminder.
    """
    print("--- Personal Daily Reminder ---")
    
    # Get user input for task
    task = input("Enter your task: ")
    
    # Get user input for priority (ensure valid input)
    priority = input("priority (high/medium/low): ").lower()
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("priority (high/medium/low): ").lower()
    
    # Get user input for time-bound status (ensure valid input)
    time_bound_input = input("Is it time-bound? (yes/no): ").lower()
    while time_bound_input not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time_bound_input = input("Is it time-bound? (yes/no): ").lower()
    
    # Determine the urgency message based on priority and time-bound status
    urgency = ""
    if priority == 'high' and time_bound_input == 'yes':
        urgency = "requires immediate attention today!"
    elif priority == 'high' and time_bound_input == 'no':
        urgency = "is a high priority task."
    elif priority == 'medium' and time_bound_input == 'yes':
        urgency = "is a medium priority task due today."
    elif priority == 'medium' and time_bound_input == 'no':
        urgency = "is a medium priority task."
    elif priority == 'low':
        urgency = "is a low priority task."

    # Print the final formatted reminder
    print("\nReminder: '{}' {} using python".format(task, urgency))

if __name__ == "__main__":
    create_daily_reminder()
