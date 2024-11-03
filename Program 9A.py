class BankAcct:
    def __init__(self, name, account_number, initial_amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = initial_amount
        self.interest_rate = interest_rate  # as a percentage

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds for withdrawal.")
        else:
            self.amount -= amount
            print(f"Withdrew ${amount}. New balance is ${self.amount}.")

    def deposit(self, amount):
        self.amount += amount
        print(f"Deposited ${amount}. New balance is ${self.amount}.")

    def calculate_interest(self, days):
        interest = (self.amount * self.interest_rate / 100) * (days / 365)
        return interest

    def get_balance(self):
        return self.amount

    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2f}%")

def test_bank_acct():
    # Create an instance of BankAcct
    acct = BankAcct("Alice Smith", "123456789", 1000.00, 5.0)

    # Display account information
    print(acct)

    # Test deposit
    acct.deposit(500)
    
    # Test withdraw
    acct.withdraw(200)
    
    # Attempt to withdraw more than the balance
    acct.withdraw(2000)
    
    # Check balance
    print(f"Current balance: ${acct.get_balance():.2f}")

    # Adjust interest rate
    acct.adjust_interest_rate(6.0)
    print(f"New interest rate: {acct.interest_rate}%")

    # Calculate interest for 30 days
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

# Run the test function
if __name__ == "__main__":
    test_bank_acct()
