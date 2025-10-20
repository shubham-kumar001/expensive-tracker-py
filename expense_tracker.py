import csv
import datetime
import os

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.date.today().strftime("%Y-%m-%d")
    category = input("Enter category (e.g. Food, Travel, Bills): ")
    amount = input("Enter amount (₹): ")
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return
    print("\n📒 Your Expenses:\n")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            date, category, amount, desc = row
            total += float(amount)
            print(f"{date} | {category} | ₹{amount} | {desc}")
        print(f"\n💰 Total Spent: ₹{total}\n")

def summary_by_category():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return
    categories = {}
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            _, category, amount, _ = row
            categories[category] = categories.get(category, 0) + float(amount)
    print("\n📊 Spending Summary by Category:\n")
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt}")
    print()

def clear_data():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("🗑️ All data cleared.\n")
    else:
        print("No data to clear.\n")

def main():
    while True:
        print("========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Clear All Data")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            clear_data()
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
