class BankAccount:
    def __init__(self,account_number,balance=0.0):
        self.account_number = account_number 
        self.balance = balance 

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount 
            print(f"Deposite:${amount:2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance = amount 
            print(f"Withdrawn:${amount:2f}")
        else:
            print("Withdraw amount must be greater than zero.")

    def check_balance(self):
            print(f"Account{self.account_number} Balance:${self.balance:2f}")
account = BankAccount("123456789",500.00)
account.check_balance()
account.deposit(200)
account.withdraw(100)
account.check_balance()
