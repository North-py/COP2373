from functools import reduce

def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Please enter a valid number for the amount.")
    return expenses

def calculate_total(expenses):
    return reduce(lambda acc, exp: acc + exp[1], expenses, 0)

def find_highest_expense(expenses):
    return reduce(lambda acc, exp: exp if exp[1] > acc[1] else acc, expenses)

def find_lowest_expense(expenses):
    return reduce(lambda acc, exp: exp if exp[1] < acc[1] else acc, expenses)

def main():
    expenses = get_expenses()
    
    if not expenses:
        print("No expenses entered.")
        return

    total_expense = calculate_total(expenses)
    highest_expense = find_highest_expense(expenses)
    lowest_expense = find_lowest_expense(expenses)

    print(f"\nTotal Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

if __name__ == "__main__":
    main()
