expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Filter by Category")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the product name: ")
        price = int(input("enter the cost of the product: "))
        category = input("Enter the Category of the Product: ").lower()

        entry = {"Item":item, "Price": price, "Category": category}
        expenses.append(entry)
        print("Added")
    elif choice == "2":
        print("\n--- Your Spending ---")

        Total = 0
        for e in expenses:
            print(f"{e['Item']}: {e['Price']} : {e['Category']}")
            Total += e['Price']
        print(f"--- Total Spending: ₹{Total}---")

    elif choice == "3":
        print("\n--- Filter  ---")
        categor = input("Enter the Category: ").lower()
        print(f"\nResults for '{categor}':")
        category_total = 0
        found = False

        for e in expenses:
            if e['Category'].lower() == categor:
                print(f"{e['Item']}: {e['Price']}")
                category_total += e['Price']
                found = True
        if found:
            print(f"---Total for {categor}: ₹{category_total}")
        else:
            print(f"No Expense Foud for {categor} Filter ")

    elif choice == "4":
        print("Comeback Later, Now Goodbye")
        break
    else:
        print("Invalid choice, Try again")

