from bank_account import BankAccount

account1=BankAccount("1234",1000)
print(account1)
account1.deposit(1000)
account1.withdraw(500)
print(account1.get_balance())

account2=BankAccount("2345",5000)
account2.deposit(1000)
print(account2.get_balance())

