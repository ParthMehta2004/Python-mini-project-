import os


def read_balance(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            balance = float(file.read().strip())
    else:
        balance = None
    return balance


def write_balance(filename, balance):
    with open(filename, 'w') as file:
        file.write(str(balance))


def expense_tracker():
    filename = "balance.txt"
    balance = read_balance(filename)

    
    if balance is None:
        while True:
            try:
                balance = float(input("Welcome! It seems this is your first time using the tracker.\nPlease enter your initial balance: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        write_balance(filename, balance)

    while True:
        print("\nCurrent Balance: Rs.{:.2f}".format(balance))
        print("1. Add Income")
        print("2. Subtract Expense")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            try:
                income = float(input("Enter the income amount to add: "))
                balance += income
                write_balance(filename, balance)
                print("Income added successfully!")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '2':
            try:
                expense = float(input("Enter the expense amount to subtract: "))
                if expense > balance:
                    print("Warning: This will result in a negative balance.")
                balance -= expense
                write_balance(filename, balance)
                print("Expense subtracted successfully!")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '3':
            print("Current Balance: Rs.{:.2f}".format(balance))

        elif choice == '4':
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print("Exiting the tracker. Goodbye!")
                break
            else:
                print("Returning to the main menu.")

        else:
            print("Invalid option. Please choose a valid option (1-4).")

if __name__ == "__main__":
    expense_tracker()
