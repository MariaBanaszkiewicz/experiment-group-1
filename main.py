from AccountManager import AccountManager
from ToDoList import ToDoList


def main():

    toDoList = ToDoList()
    toDoList.add_task("t", "d", 3)
    toDoList.view_sorted_tasks();

    accountManager = AccountManager()
    val = input("Enter your value: ")

    if val == '1':
        ID = input("Enter your accnr: ")
        accountManager.createAccount(ID);

    return 0

if __name__ == "__main__":
    main()