from AccountManager import AccountManager


def main():

    accountManager = AccountManager()
    val = input("Enter your value: ")

    if val == '1':
        ID = input("Enter your accnr: ")
        accountManager.createAccount(ID);

    return 0

if __name__ == "__main__":
    main()