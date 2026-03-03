expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the product name: ")
        price = int(input("enter the cost of the product: "))

        entry = {"Item":item, "Price": price}
        expenses.append(entry)
        print("Added")
    elif choice == "2":
        print("\n--- Your Spending ---")
        for e in expenses:
            print(f"{e['Item']}: {e['Price']}")
    elif choice == "3":
        print("Comeback Later, Now Goodbye")
        break
    else:
        print("Invalid choice, Try again")

