class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._account_holder = account_holder
        self._balance = initial_balance

    def get_account_holder(self):
        return self._account_holder

    def get_balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds. Balance: ${self._balance:.2f}, Attempted withdrawal: ${amount:.2f}"
            )
        self._balance -= amount

    def transfer(self, amount: float, target_account):
        if not isinstance(target_account, BankAccount):
            raise ValueError("Target account must be a BankAccount instance")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds. Balance: ${self._balance:.2f}, Attempted transfer: ${amount:.2f}"
            )
        self._balance -= amount
        target_account.deposit(amount)

    def __str__(self):
        return f"Account holder: {self._account_holder}, Balance: ${self._balance:.2f}"


# Example Usage
alice_account = BankAccount("Alice", 1000.0)
bob_account = BankAccount("Bob", 500.0)

print(alice_account)
print(alice_account.get_balance())

alice_account.deposit(250.0)
print(alice_account.get_balance())

alice_account.withdraw(100.0)
print(alice_account.get_balance())

alice_account.transfer(200.0, bob_account)
print(alice_account.get_balance())
print(bob_account.get_balance())

try:
    alice_account.withdraw(2000.0)
except ValueError as e:
    print(e)

try:
    alice_account.deposit(-50.0)
except ValueError as e:
    print(e)

try:
    bob_account.withdraw(0)
except ValueError as e:
    print(e)

try:
    invalid_account = BankAccount("Charlie", -100.0)
except ValueError as e:
    print(e)