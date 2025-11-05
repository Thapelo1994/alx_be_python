class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def display_balance(self):
        print(f"current_balance: {self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f}")
            self.display_balance()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount:.2f}")
            self.display_balance()
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

def main():
    # Create an instance of the BankAccount class with an initial balance
    account = BankAccount(initial_balance=100.00)
    
    print("Welcome to the Bank Account Management System")

    while True:
        print("\nMenu:")
        print("1. Display Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")
        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")
        elif choice == '4':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()