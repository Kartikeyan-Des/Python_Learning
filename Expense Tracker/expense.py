import json

def add(expense_list):
        item = input("Enter the product name: ")
        try:
            price = int(input("enter the cost of the product: "))
            category = input("Enter the Category of the Product: ").lower() 
            expense_list.append({"Item":item, "Price":price, "Category":category})
            print("Expense added Successfully!!")
        except ValueError:
                print("Error: Price must be Number")

def view(expense_list):
    print("\n--- Your Spending ---")
    Total = 0
    for e in expense_list:
            print(f"{e['Item']}: {e['Price']} : {e['Category']}")
            Total += e['Price']
    print(f"--- Total Spending: ₹{Total}---")




try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
    print("Data loaded Successfully")
except FileNotFoundError:
    expenses=[]
    print("No saved Data, Starting Fresh.")

# with open("expenses.json", "r") as f:
#     expenses = json.load(f)

# expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Filter by Category")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add(expenses)
        # item = input("Enter the product name: ")
        # price = int(input("enter the cost of the product: "))
        # category = input("Enter the Category of the Product: ").lower()

        # entry = {"Item":item, "Price": price, "Category": category}
        # expenses.append(entry)
        # print("Added")

    elif choice == "2":
         view(expenses)
        # print("\n--- Your Spending ---")

        # Total = 0
        # for e in expenses:
        #     print(f"{e['Item']}: {e['Price']} : {e['Category']}")
        #     Total += e['Price']
        # print(f"--- Total Spending: ₹{Total}---")

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

        with open("expenses.json", "w") as f:
            json.dump(expenses,f,indent=4)
        print("Progress Saved, Now Goodbye")
        break
    else:
        print("Invalid choice, Try again")

