class BankAccount:
    """
    A class to represent a bank account with basic operations.
    """
    def __init__(self, owner, initial_balance=0.0):
        """
        Initializes the bank account with an owner name and an optional initial balance.
        """
        self.owner = owner
        self.balance = initial_balance
        print(f"Account created for {self.owner} with initial balance of ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account, if sufficient funds are available.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds. Withdrawal failed.")

    def display_balance(self):
        """
        Displays the current balance of the account.
        """
        print(f"{self.owner}'s Balance: ${self.balance:.2f}")

    def display_current_balance(self):
        """
        An alias method to display the current balance (as requested).
        """
        # This method calls the display_balance method for simplicity and consistency
        self.display_balance()


if __name__ == "__main__":
    # Example usage of the BankAccount class
    print("Welcome to the simple banking system.")
    