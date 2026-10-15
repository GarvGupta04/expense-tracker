import json
from datetime import date
from pathlib import Path

# Store expenses in a JSON file in this project folder
FILE_NAME = Path("expenses.json")


def load_expenses():
    """Load saved expenses from the JSON file."""
    if FILE_NAME.exists():
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Ask the user for details and add a new expense."""
    try:
        amount = float(input("Enter amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category (Food/Travel/etc.): ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def show_total(expenses):
    """Calculate and display total spending."""
    total = sum(expense["amount"] for expense in expenses)

    print(f"Total expenses: ₹{total:.2f}")


def filter_expenses(expenses):
    """Display expenses belonging to a selected category."""
    category = input("Enter category to search: ").strip()

    matches = [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    if not matches:
        print("No expenses found in this category.")
        return

    print(f"\n--- {category} Expenses ---")

    for expense in matches:
        print(
            f"{expense['date']} | ₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )


def delete_expense(expenses):
    """Delete an expense using its displayed number."""
    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    removed = expenses.pop(number - 1)
    save_expenses(expenses)

    print(f"Deleted expense: {removed['description']}")


def main():
    """Display the menu and handle user choices."""
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            filter_expenses(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()