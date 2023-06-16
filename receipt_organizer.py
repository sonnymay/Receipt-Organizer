class Receipt:
    def __init__(self, store_name, date, amount, items):
        self.store_name = store_name
        self.date = date
        self.amount = amount
        self.items = items

    def __str__(self):
        return f"{self.store_name} - {self.date} - ${self.amount}"

import datetime

receipts = []

def add_receipt(store_name, date, amount, items):
    receipts.append(Receipt(store_name, date, amount, items))

def view_receipts():
    for receipt in receipts:
        print(receipt)

def search_receipts(store_name):
    for receipt in receipts:
        if receipt.store_name == store_name:
            print(receipt)

while True:
    print("\nReceipt Organizer")
    print("1. Add receipt")
    print("2. View all receipts")
    print("3. Search receipts by store name")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        store_name = input("Enter store name: ")

        # Validate date
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
            continue

        # Validate amount
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue

        items = input("Enter items (comma separated): ").split(',')
        add_receipt(store_name, date, amount, items)

    elif choice == '2':
        view_receipts()

    elif choice == '3':
        store_name = input("Enter store name to search: ")
        search_receipts(store_name)

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please try again.")
