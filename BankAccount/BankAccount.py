class BankAccount:

    bank_title = "Bank of Banks"

    def __init__(self, name, currentbalance, minimum_balance):
        self.name = name
        self.currentBalance = currentbalance
        self.minimumBalance = minimum_balance

    def deposit(self, value):
        self.currentBalance += value
        print("You have deposited " + str(value) + "$ into your bank self \nYou now have " + str(
            self.currentBalance) + "$ in your self.\n")

    def withdraw(self, value):
        remainingBalance = self.currentBalance - value
        if remainingBalance > self.minimumBalance - 1:
            self.currentBalance -= value
            print("You have withdrawn " + str(value) + "$ from your acccunt. \nYou have now " + str(
                self.currentBalance) + "$ left.\n")
        else:
            print("Transaction denied: You do not have sufficient funds in self to withdraw wanted amount.\n")

    def print_customer_information(self):
        print(BankAccount.bank_title + "\n" + self.name + "'s account: \nBalance: " + str(self.currentBalance) + "\n")

class SavingsAccount(BankAccount):
    def __init__(self, name, currentbalance, minimum_balance, interest_rate):
        self.name = name
        self.currentBalance = currentbalance
        self.minimumBalance = minimum_balance
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.currentBalance * self.interest_rate
        self.currentBalance += interest
        print(f"Interest of {interest}$ added. New balance: {self.currentBalance}$\n")


class CheckingAccount(BankAccount):
    def __init__(self, name, currentbalance, minimum_balance, transfer_limit):
        self.name = name
        self.currentBalance = currentbalance
        self.minimumBalance = minimum_balance
        self.transfer_limit = transfer_limit

    def transfer(self, value, target_account):
        if value > self.transfer_limit:
            print(f"Transfer denied: Amount exceeds transfer limit of {self.transfer_limit}$.\n")
        elif self.currentBalance - value < self.minimumBalance:
            print("Transfer denied: Insufficient funds for transfer.\n")
        else:
            self.currentBalance -= value
            target_account.currentBalance += value
            print(f"Transferred {value}$ to {target_account.name}. Your new balance: {self.currentBalance}$\n")

b1 = BankAccount("Josh", 2000, 100)
b1.print_customer_information()
b1.deposit(2000)
b1.withdraw(300)
b1.withdraw(10000)

b2 = BankAccount("Marcel", 1000, 100)
b2.print_customer_information()
b2.deposit(100)
b2.withdraw(100)
b2.withdraw(10000)
