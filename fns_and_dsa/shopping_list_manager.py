shopping_list = []

def add_item(item):
    """Adds an item to the shopping list."""
    shopping_list.append(item.capitalize())
    print(f"'{item.capitalize()}' added to the list.")

def view_list():
    """Displays the current shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\n--- Your Shopping List ---")
        for index, item in enumerate(shopping_list):
            print(f"{index + 1}. {item}")
        print("--------------------------")

def remove_item(item_to_remove):
    """Removes an item from the shopping list."""
    try:
        shopping_list.remove(item_to_remove.capitalize())
        print(f"'{item_to_remove.capitalize()}' removed from the list.")
    except ValueError:
        print(f"'{item_to_remove.capitalize()}' not found in the list.")

def main():
    """Main function to run the shopping list application."""
    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. View list")
        print("3. Remove item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            view_list()
        elif choice == '3':
            item_to_remove = input("Enter the item to remove: ")
            remove_item(item_to_remove)
        elif choice == '4':
            print("Exiting shopping list application. Happy shopping!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()shopping_list = []

def add_item(item):
    """Adds an item to the shopping list."""
    shopping_list.append(item.capitalize())
    print(f"'{item.capitalize()}' added to the list.")

def view_list():
    """Displays the current shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\n--- Your Shopping List ---")
        for index, item in enumerate(shopping_list):
            print(f"{index + 1}. {item}")
        print("--------------------------")

def remove_item(item_to_remove):
    """Removes an item from the shopping list."""
    try:
        shopping_list.remove(item_to_remove.capitalize())
        print(f"'{item_to_remove.capitalize()}' removed from the list.")
    except ValueError:
        print(f"'{item_to_remove.capitalize()}' not found in the list.")

def main():
    """Main function to run the shopping list application."""
    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. View list")
        print("3. Remove item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            view_list()
        elif choice == '3':
            item_to_remove = input("Enter the item to remove: ")
            remove_item(item_to_remove)
        elif choice == '4':
            print("Exiting shopping list application. Happy shopping!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()