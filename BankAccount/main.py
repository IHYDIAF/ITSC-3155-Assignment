from bank import BankAccount
from checkings import CheckingAccount
from savings import SavingsAccount

checking1 = CheckingAccount("Alice", 1000, 100, 1000, "123456789", "987654321")
checking2 = CheckingAccount("Bob", 500, 100, 1000, "987654321", "123456789")

savings1 = SavingsAccount("Carol", 2000, 100, 0.02, "112233445", "554433221")
savings2 = SavingsAccount("Dave", 1500, 100, 0.02, "223344556", "665544332")

# scenario 1
print(f"Initial currentbalance for {checking1.name}: ${checking1.currentBalance}")
checking1.withdraw(200)
print(f"Balance after withdrawal for {checking1.name}: ${checking1.currentBalance}")

# scenario 2
print(f"\nInitial balance for {checking2.name}: ${checking2.currentBalance}")
checking2.deposit(300)
print(f"Balance after deposit for {checking2.name}: ${checking2.currentBalance}")

# scenario 3
print(f"\nInitial balance for {savings1.name}: ${savings1.currentBalance}")
savings1.deposit(500)
print(f"Balance after deposit for {savings1.name}: ${savings1.currentBalance}")

# scenario 4
print(f"\nInitial balance for {savings2.name}: ${savings2.currentBalance}")
savings2.withdraw(200)
print(f"Balance after withdrawal for {savings2.name}: ${savings2.currentBalance}")