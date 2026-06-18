# Main app.
from functions.menu import menu
from functions.add_expense import add_expense
from functions.list_expenses import list_expenses

while True:
    menu()
    user_input = input("Please select option: ")

    match user_input:
        case "1":
            print("Option 1 picked... Loading.")
            add_expense()
        case "2":
            print("Displaying current expenses...")
            list_expenses()
        case "3":
            print("Exiting...")
            break

