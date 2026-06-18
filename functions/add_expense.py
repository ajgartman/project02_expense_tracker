import datetime
import os
import json
# Add expense function.
# Date input validation

def is_valid_date(user_input,date_format = "%Y-%m-%d"):
    try:
        datetime.datetime.strptime(user_input, date_format)
        return True
    except ValueError:
        return False

def add_expense():
    # Each expense will need to have: category, amount, date, location.

    category = input("Please insert the category of the expense. [Food, Transport, Utilities, Entertainment]: ")
    try:
        amount = float(input("Please type the amount of money spent: "))
    except ValueError:
        print("Please enter correct value! [0-9] numbers allowed only!")
        return
    date = input("Please type the date of the expense. Omit to set it to today. Format YYYY-MM-DD: ")
    location = input("Please insert location/venue of the expense: ")


    allowed_categories = ["food","transport","utilities","entertainment"]


    if category.lower() not in allowed_categories:
        print("----- ----- -----")
        print("Invalid category selection! Please follow the schema!")
        return


    # Date validation
    if date:
        result = is_valid_date(date)
        if not result:
            print("----- ----- -----")
            print("Invalid date format! Please follow the YYYY-MM-DD pattern!")
            return
    elif not date:
        date = str(datetime.datetime.now().date())


    json_string = {"category":category,
                   "amount":amount,
                   "date":date,
                   "location":location}

    path = os.path.join("json_output","expenses.json")
    dir_path = os.path.dirname(path)
    json_list = []

    # Checking if directory exists
    os.makedirs(dir_path,exist_ok=True)

    # Checking if file exists:
    if not os.path.exists(path):
        print("File does not exist...Creating it now! ")
        with open(path,mode="w") as file:
            json.dump([],file)

    # Fetching current JSON files
    try:
        with open(path, mode="r") as file:
            json_data = json.load(file)
            for item in json_data:
                json_list.append(item)
    except json.decoder.JSONDecodeError:
        print("File is empty!")

    # Appending new item
    json_list.append(json_string)
    # Writing it back to JSON
    with open(path, mode="w") as file:
        json.dump(json_list, file, indent=4)

    print("Submitting the expense!")
