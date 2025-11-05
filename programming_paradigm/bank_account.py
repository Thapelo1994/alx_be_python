class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__account_balance += amount
        print(f"Deposited: ${amount:.2f}")
        self.display_balance()

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            self.display_balance()
            return True
        else:
            print("Insufficient funds for withdrawal.")
            self.display_balance()
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

# Example Usage:
if __name__ == "__main__":
    my_account = BankAccount(100.00)
    my_account.display_balance()

    my_account.deposit(50.75)
    my_account.withdraw(25.50)

    # Attempt to withdraw more than available
    my_account.withdraw(200.00)

    # Attempt to deposit a negative amount
    my_account.deposit(-10.00)

    # Attempt to withdraw a negative amount
    my_account.withdraw(-5.00)

    another_account = BankAccount() # Default initial balance of 0
    another_account.display_balance()
    another_account.deposit(1000)