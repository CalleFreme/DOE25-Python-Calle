# Funktionalitet:
# - Lägg till transaktion
# - Visa ekonomisk status
# - Skapa budget
# - Visa budgetar
# - Budgetövervakning

# Non-functional requirements:
# 3 files of code:
# (finance_tracker.py (main),
# tracker_class.py,
# transaction_class.py,
# one or more JSON-files)

# Data:
# Transactions
# Budget

from transaction_class import Transaction
#from transaction_class import *
import datetime
# Date format: YYYY-MM-DD
# Example: 2023-10-15

def add_transaction(transaction, transactions=[]):
    transactions.append(transaction)
    print(f"Added transaction: {transaction}")
    return transactions

def calculate_balance(transactions):
    # Show balance/saldo
    balance = 0
    try:
        for transaction in transactions:
            transaction_type = transaction.type # "i" or "e"
            amount = transaction.amount # amount in kr
            if transaction_type == "i":
                balance += int(amount)
            else:
                balance -= int(amount)
    except ValueError:
        print("Invalid transaction data.")
    return balance

def show_balance(balance):
    print(f"Your balance is {balance}")

def show_transactions_history(transactions):
    print()
    sorted_transactions = sorted(transactions, reverse=True)
    print(sorted_transactions)
    print()

def create_budget():
    pass

def show_budgets():
    pass

def start_budget_monitoring():
    pass

def read_financial_data_from_file():
    transactions = []
    try:
        with open("transaction_data.txt", 'r') as transaction_file:
            transaction_lines = transaction_file.readlines() # readlines() returns a list of lines
            for transaction in transaction_lines:
                # Strip removes whitespace/newline, split creates a list by splitting the string at every ","
                transaction_info = transaction.strip().split(",")
                transaction_type = transaction_info[0]
                transaction_amount = transaction_info[1]
                transaction_category = transaction_info[2]
                transaction_descr = transaction_info[3]
                transaction_date = transaction_info[4]
                new_transaction = Transaction(
                    transaction_type,
                    transaction_amount,
                    transaction_category,
                    transaction_descr,
                    transaction_date)
                transactions.append(new_transaction)  
        return transactions          
    except IOError:
        print("File could not be read.")

def write_financial_data_to_file(transactions):
    try:
        with open("transaction_data.txt", 'w') as transaction_file:
            for transaction in transactions:
                transaction_line = f"{transaction.type},{transaction.amount},{transaction.category},{transaction.descr},{transaction.date}\n"
                transaction_file.write(transaction_line)
    except IOError:
        print("File could not be written.")

def show_main_menu():
    print("Welcome to your Finance Tracker")
    print("1. Add transaction")
    print("2. Show financial status")
    print("3. Create budget")
    print("4. Show budget")
    print("5. Budget monitoring")
    print("6. Quit")


#def handle_input():
#    pass

def main():
    transactions = read_financial_data_from_file()
    while True:
        show_main_menu()
        valid_input = False
        while not valid_input:
            menu_choice = input("Choose menu option 1-6: ")
            match menu_choice:
                case "1":
                    transaction_type = input("Type of transaction ((i)ncome/(e)xpense): ").strip().lower()
                    amount = input("Transaction amount (kr): ")
                    category = input("Category (Food/Transport/Salary/Rent): ").lower()
                    description = input("Optional description: ")
                    date = input("Optional date for transaction: ")
                    new_transaction = Transaction(transaction_type, amount, category, description, date)
                    transactions = add_transaction(transactions, new_transaction)
                    valid_input = True
                case "2":
                    current_balance = calculate_balance(transactions)
                    show_balance(current_balance)
                    show_transactions_history(transactions)
                    valid_input = True
                case "3":
                    create_budget()
                    valid_input = True
                case "4":
                    show_budgets()
                    valid_input = True
                case "5":
                    start_budget_monitoring()
                    valid_input = True
                case "6":
                    write_financial_data_to_file()
                    quit()
                case _:
                    print("Invalid choice, please choose again.")



main()
