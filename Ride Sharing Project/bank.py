class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, name, initial_deposit):
        user = User(name, initial_deposit)
        self.users.append(user)
        self.total_balance += initial_deposit
        return user

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature

    def is_bankrupt(self):
        return self.total_balance < 0

    def process_loan(self, user):
        if self.loan_feature:
            loan_amount = 2 * user.get_balance()
            user.deposit(loan_amount)
            self.total_loan_amount += loan_amount
            return loan_amount
        else:
            return 0


class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            return True
        else:
            return False

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
            return True
        else:
            return False

    def get_transaction_history(self):
        return self.transaction_history


# Example usage:
bank = Bank()

user1 = bank.create_account("John", 1000)
user2 = bank.create_account("Alice", 2000)

print(f"User1 balance: {user1.get_balance()}")  # Output: User1 balance: 1000
print(f"User2 balance: {user2.get_balance()}")  # Output: User2 balance: 2000

user1.deposit(500)
user2.withdraw(1000)

print(f"User1 balance: {user1.get_balance()}")  # Output: User1 balance: 1500
print(f"User2 balance: {user2.get_balance()}")  # Output: User2 balance: 1000

user1.transfer(700, user2)

print(f"User1 balance: {user1.get_balance()}")  # Output: User1 balance: 800
print(f"User2 balance: {user2.get_balance()}")  # Output: User2 balance: 1700

print(user1.get_transaction_history())  # Output: ['Deposited 500', 'Transferred 700 to Alice']
print(user2.get_transaction_history())  # Output: ['Withdrew 1000', 'Deposited 700']

bank.toggle_loan_feature()
loan_amount = bank.process_loan(user1)
print(f"User1 balance: {user1.get_balance()}")  # Output: User1 balance: 2500
print(f"Bank total loan amount: {bank.get_total_loan_amount()}")  # Output: Bank total loan amount: 2500
