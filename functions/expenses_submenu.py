# Expenses submenu
def submenu():
    print("----- ----- -----")
    print("Expenses Submenu.")
    print("Please select following actions...")

    print("""
    1. Sum all the expenses
    2. Filter by category
    3. List by date (Most Recent)
    4. Select specific day
    5. Back to main menu
    """)

    action = input("Select the action: ")

    return action