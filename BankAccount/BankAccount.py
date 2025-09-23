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
