shopping_list = []  # Initialize an empty list to store shopping items

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Shopping List Menu ---")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear List")
    print("5. Exit")
    print("-------------------------")

def view_list():
    """Displays the current items in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\n--- Your Shopping List ---")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
        print("--------------------------")

def add_item():
    """Prompts the user to add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the list.")
    else:
        print("Item cannot be empty.")

def remove_item():
    """Prompts the user to remove an item from the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty, nothing to remove.")
        return

    view_list()  # Display the list to help the user choose
    try:
        item_index = int(input("Enter the number of the item to remove: ")) - 1
        if 0 <= item_index < len(shopping_list):
            removed_item = shopping_list.pop(item_index)
            print(f"'{removed_item}' removed from the list.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def clear_list():
    """Clears all items from the shopping list."""
    if shopping_list:
        confirm = input("Are you sure you want to clear the entire list? (yes/no): ").lower()
        if confirm == 'yes':
            shopping_list.clear()
            print("Shopping list cleared.")
        else:
            print("Clearing cancelled.")
    else:
        print("Your shopping list is already empty.")

def main():
    """Main function to run the shopping list application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_list()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            clear_list()
        elif choice == '5':
            print("Exiting shopping list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()