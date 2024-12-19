from BankAccount import BankAccount


class AccountManager:

    def __init__(self):
        self.accounts = []

    def findAccount(self, ID):
        for i in range(len(self.accounts)):
            if self.accounts[i].accountNumber == ID:
                return self.accounts[i]
        return None

    def createAccount(self, ID):
        if self.findAccount(ID) is None:
            self.accounts.append(BankAccount(ID))
            print("account created")
        else:
            print("accountNumber already exists")

    def deposit(self, ID, amount):
        if amount < 0:
            print("invalid amount")
            return
        account = self.findAccount(ID)
        if account is None:
            print("create account first")
            return
        account.balance += amount
        print("new balance is", account.balance)

    def withdrawal(self, ID, amount):
        if amount <= 0:
            print("invalid amount")
            return
        account = self.findAccount(ID)
        if account is None:
            print("create account first")
            return
        if (amount > account.balance):
            print("not sufficient balance")
            return
        account.balance -= amount
        print("new balance is", account.balance)

    def listAccounts(self):
        for i in range(len(self.accounts)):
            print("nr:", self.accounts[i].accountNumber, "balance:", self.accounts[i].accountNumber, "\n")

    def transferMoney(self, src, dest, amount):
        srcAccount = self.findAccount(src)
        if srcAccount is None:
            print("create source account first")
            return

        destAccount = self.findAccount(dest)
        if destAccount is None:
            print("create destination account first")
            return

        if (amount > srcAccount.balance):
            print("not sufficient balance")
            return

        srcAccount.balance -= amount
        destAccount.balance += amount