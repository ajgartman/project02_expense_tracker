# List all expenses function
import os
import json
from functions.expenses_submenu import submenu
from functions.add_expense import is_valid_date
import pandas as pd

def list_expenses():

    json_list = []
    data_fetched = False
    while True:
        path = os.path.join("json_output", "expenses.json")
        # Fetching current JSON files
        if not data_fetched:
            try:
                with open(path, mode="r") as file:
                    json_data = json.load(file)
                    for item in json_data:
                        json_list.append(item)
                        data_fetched = True
            except json.decoder.JSONDecodeError:
                print("File is empty!")

            for entry_id,entry in enumerate(json_list,start=1):
                category = entry["category"]
                amount = entry["amount"]
                date = entry["date"]
                location = entry["location"]

                print(f"ID: {entry_id}. Name: {category}. Amount: {amount}. Date: {date}. Location: {location}")

        user_action = submenu()

        match user_action:
            case "1":
                print("Summing expenses... Loading.")
                total = 0
                for entry in json_list:
                    print(entry)
                    total += int(entry["amount"])
                print(f"Total amount of money spent: {total}")
            case "2":
                print("Filtering by category...")
                print("\n")
                print("FOOD")
                print("-----")
                # Creating dataframe
                df = pd.DataFrame(json_list)
                print(df[df["category"]=="Food"])
                print("\n")
                print("TRANSPORT")
                print("-----")
                print(df[df["category"] == "Transport"])
                print("\n")
                print("ENTERTAINMENT")
                print("-----")
                print(df[df["category"] == "Entertainment"])
                print("\n")
                print("UTILITIES")
                print("-----")
                print(df[df["category"] == "Utilities"])

            case "3":
                print("Sorting by most recent date...")

                for entry_id, entry in enumerate(json_list[::-1], start=1):
                    category = entry["category"]
                    amount = entry["amount"]
                    date = entry["date"]
                    location = entry["location"]

                    print(f"ID: {entry_id}. Name: {category}. Amount {amount}. Date: {date}. Location: {location}")


            case "4":
                print("Select the date: Follow the following format YYYY-MM-DD")
                user_action2 = input("Enter the date: ")

                if user_action2:
                    result = is_valid_date(user_action2)
                    if not result:
                        print("----- ----- -----")
                        print("Invalid date format! Please follow the YYYY-MM-DD pattern!")
                        continue

                print("Records found: ")
                for entry_id, entry in enumerate(json_list[::-1], start=1):
                    if entry["date"] == user_action2:
                        category = entry["category"]
                        amount = entry["amount"]
                        date = entry["date"]
                        location = entry["location"]
                        print(f"ID: {entry_id}. Name: {category}. Amount {amount}. Date: {date}. Location: {location}")

            case "5":
                break