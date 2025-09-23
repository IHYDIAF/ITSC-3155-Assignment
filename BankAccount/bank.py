class BankAccount:

    bank_title = "Bank of Banks"

    def __init__(self, name, currentbalance, minimum_balance, account_number, routing_number):
        self.name = name
        self.currentBalance = currentbalance
        self.minimumBalance = minimum_balance

        self._account_number = account_number         
        self.__routing_number = routing_number        

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
        print(f"Account Number: {self._account_number}")
