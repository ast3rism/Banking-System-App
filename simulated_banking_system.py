import random  # For generating account numbers

class Account:
    def __init__(self, name, balance, account_number=None):
        self.name = name
        self.balance = balance
        self.account_number = account_number or self.generate_account_number()

    def generate_account_number(self):
        # Generate a 6-digit random number for account number
        return random.randint(100000, 999999)

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            print(f"{self.name} deposited ${amount}. Current balance is: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{self.name} withdrew ${amount}. Current balance is: ${self.balance}")
            else:
                print("You don't have enough funds to withdraw.")
        else:
            print("Invalid withdrawal amount.")

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate, account_number=None):
        super().__init__(name, balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added at rate {self.interest_rate*100}%. New balance is: ${self.balance}")

def create_account(name, account_type='regular'):
    # Simulate a database interaction for account creation
    account_number = random.randint(100000, 999999)  # Generate random account number
    initial_balance = 1000  # Initial balance
    if account_type == 'savings':
        interest_rate = 0.05  # 5% interest rate
        return SavingsAccount(name, initial_balance, interest_rate, account_number)
    else:
        return Account(name, initial_balance, account_number)

def manage_account(account):
    while True:
        print("\n\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        if isinstance(account, SavingsAccount):
            print("4. Add Interest")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 3:
                print(f"Balance: ${account.balance}")
            elif choice == 4 and isinstance(account, SavingsAccount):
                account.add_interest()
            elif choice == 5:
                print("Exiting account management.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    name = input("\nEnter your name: ")
    account_type = input("Enter account type (regular/savings): ").lower()
    account = create_account(name, account_type)
    print(f"\nYour account has been created successfully. Account number: {account.account_number}")
    manage_account(account)

if __name__ == "__main__":
    main()
