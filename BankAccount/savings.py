from bank import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, currentbalance, minimum_balance, interest_rate, account_number, routing_number):
        self.name = name
        self.currentBalance = currentbalance
        self.minimumBalance = minimum_balance
        self.interestRate = interest_rate
        self.accountNumber = account_number
        self.routingNumber = routing_number

    def add_interest(self):
        interest = self.currentBalance * self.interest_rate
        self.currentBalance += interest
        print(f"Interest of {interest}$ added. New balance: {self.currentBalance}$\n")