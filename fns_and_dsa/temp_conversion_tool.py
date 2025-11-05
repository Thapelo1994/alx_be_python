class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account. Defaults to 0.
        """
        if initial_balance < 0:
            print("Initial balance cannot be negative. Setting to 0.")
            self._account_balance = 0
        else:
            self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self._account_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self._account_balance:
            print("Insufficient funds for withdrawal.")
            return False
        else:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self._account_balance:.2f}")
            return True

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current account balance: ${self._account_balance:.2f}")

# Example Usage:
if __name__ == "__main__":
    # Create an account with an initial balance
    my_account = BankAccount(1000)
    my_account.display_balance()

    # Deposit some money
    my_account.deposit(500)
    my_account.display_balance()

    # Attempt a successful withdrawal
    my_account.withdraw(200)
    my_account.display_balance()

    # Attempt an unsuccessful withdrawal (insufficient funds)
    my_account.withdraw(1500)
    my_account.display_balance()

    # Attempt an invalid deposit or withdrawal amount
    my_account.deposit(-50)
    my_account.withdraw(0)

    # Create another account with default initial balance
    another_account = BankAccount()
    another_account.display_balance()
    another_account.deposit(75)
    another_account.display_balance()