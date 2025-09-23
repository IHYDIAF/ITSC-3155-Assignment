from bank import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, name, currentbalance, minimum_balance, transfer_limit, account_number, routing_number):
        self.name = name
        self.currentBalance = currentbalance
        self.minimumBalance = minimum_balance
        self.transferLimit = transfer_limit
        self.accountNumber = account_number
        self.routingNumber = routing_number

    def transfer(self, value, target_account):
        if value > self.transferLimit:
            print(f"Transfer denied: Amount exceeds transfer limit of {self.transferLimit}$.\n")
        elif self.currentBalance - value < self.minimumBalance:
            print("Transfer denied: Insufficient funds for transfer.\n")
        else:
            self.currentBalance -= value
            target_account.currentBalance += value
            print(f"Transferred {value}$ to {target_account.name}. Your new balance: {self.currentBalance}$\n")