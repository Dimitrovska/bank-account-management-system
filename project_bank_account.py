class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

        """
        Constructor method to initialize the account number and balance.
        """
        # ✳️ Write code to initialize the account number and balance attributes

    def deposit(self, amount):
        self.balance += amount
        """
        Method to deposit money into the account.
        """
        # ✳️ Write code to add the deposited amount to the balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Insufficient availability"
        """
        Method to withdraw money from the account.
        """
        # ✳️ Write code to check if there are sufficient funds and deduct the withdrawn amount from the balance

    def get_balance(self):
        return self.balance

        """
        Method to retrieve the current balance.
        """
        # ✳️ Write code to return the current balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        # ✳️ Call the superclass constructor to initialize common attributes
        # ✳️ Initialize the interest rate attribute

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        """
        Method to calculate and add interest to the account balance.
        """
        # ✳️ Write code to calculate the interest based on the current balance and interest rate
        # ✳️ Write code to add the calculated interest to the account balance


# Testing the functionality of the classes
if __name__ == "__main__":
    # ✳️ Create a BankAccount instance with account number "123456789" and initial balance of 1000
    first_bank_account = BankAccount("123456789")
    balance_first_bank_account = 1000
    # ✳️ Deposit 500 into the account
    first_bank_account.deposit(500)
    # ✳️ Withdraw 200 from the account
    first_bank_account.withdraw(200)
# ✳️ Get the current balance of the bank account
    print(f"First bank account balance:", first_bank_account.get_balance())
# ✳️ Create a SavingsAccount instance with account number "987654321", initial balance of 2000, and interest rate of 5%
    savings_account = SavingsAccount("987654321")
    balance_savings_account = 2000
    interest_rate = 0.05
# ✳️ Deposit 1000 into the savings account
    savings_account.deposit(1000)
# ✳️ Calculate and add interest to the savings account
    savings_account.calculate_interest()
# ✳️ Get the current balance of the savings account after adding interest
    print(f"Savings account current balance:", savings_account.get_balance())