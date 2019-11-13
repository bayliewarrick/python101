class BankAccount:
    def __init__(self,acctype,balance):
        BankAccount.type = acctype
        BankAccount.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"adding {amount} to your current balance!")
    def withdraw(self, amount):
        self.balance -= amount

ba = BankAccount("checking",0)
print(ba.balance)
ba.deposit(1000)
print(ba.balance)
