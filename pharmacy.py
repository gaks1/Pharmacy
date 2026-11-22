# Application: Best Pharmacy Management System
# Problem: A pharmacist who tracks medicine inventory, sales and profit by hand
#          can easily lose count of stock, profits, loss and calculation of taxes.
#          This can lead to miscalculation of inventories, over - ordering and incorrect
#          taxes.
#Expected input:
#         Medicine name (text)
#         Buying price per unit (number)
#         Selling price per unit (number)
#         Stock quantity (whole number)
#         Units sold (whole number)
#         Menu choice (number)
# Expected output:
#         Confirmation messages when a medicine is added or a sale recorded
#         Remaining stock for each medicine
#         Total amount earned from sales
#         Total profit or loss
#         Tax owed on profit
#         A summary report of all medicines
# Users: Pharmacist / Pharmacy owner.
# Features: Add a medicine, record a sale, view all medicines in stock, 
#           search for a medicine by name, calculate total earnings, total profit/loss and tax owed on profit, 
#           and generate a simple summary report of the pharmacy's performance

#Stage 8 - Error Handling

import os


def get_text_input(prompt):
    """
    Get the text from the user and check if it's an empty text.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("Input cannot be empty. Please enter a valid text.")
        else:
            return user_input


def get_number_input(prompt, min_value=None, max_value=None):
    """
    Get the number from the user and check if it's a valid number.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if min_value is not None and number < min_value:
            print(f"Invalid input. Value cannot be less than {min_value}.")
            continue
        if max_value is not None and number > max_value:
            print(f"Invalid input. Value cannot be more than {max_value}.")
            continue

        return number

def validate_menu_choice():
    """
    Validate the menu choice input by the user.
    """
    VALID_MENU_OPTIONS = ["1", "2", "3", "4"]
    while True:
            choice = input("Please choose an option (1 - 4): ").strip()
            if choice in VALID_MENU_OPTIONS:
                return choice
            print("Error: invalid choice. Please enter a number from 1 to 4.")

DATA_FILE = "medicine.txt"

def display_menu():
    print()
    print("---- MENU ----")
    print("1. Add medicine and calculate")
    print("2. View all medicines")
    print("3. Search for a medicine")
    print("4. Exit")


def calculate_tax(profit):
    if profit <= 0:
        return 0

    tax_owed = 0
    if profit <= 250:
        taxable_income = profit - 0
        tax_owed += taxable_income * 0.1
    elif profit <= 500:
        taxable_income = profit - 250
        tax_owed += taxable_income * 0.2
    else:
        taxable_income = profit - 500
        tax_owed += taxable_income * 0.3
    return tax_owed


def load_medicines():
    medicines = []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No saved data exists. Add medicine first.")
        return medicines
    except OSError as error:
        print(f"Error: could not read {DATA_FILE} ({error})")
        return medicines

    #skip the header
    for line_number, line in enumerate(lines[1:], start=2):
        line = line.strip()
        if line == "":
            continue

        parts = line.split("|")

        try:
            medicine = {
                "name": parts[0].strip(),
                "bought_price": int(parts[1].strip()),
                "stock": int(parts[2].strip()),
                "sell_price": int(parts[3].strip()),
                "sold": int(parts[4].strip()),
                "remaining": int(parts[5].strip()),
                "earned": int(parts[6].strip()),
                "profit": int(parts[7].strip()),
                "tax": float(parts[8].strip())
            }
        except (ValueError, IndexError):
            print(f"Warning: line {line_number} in {DATA_FILE} is damaged and was skipped.")
            continue

        medicines.append(medicine)

    return medicines

def save_medicine(medicines):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(f"{'Name':<20}|{'Bought Price':>15}|{'Stock':>10}|{'Sell Price':>15}|{'Sold':>10}|{'Remaining':>10}|{'Earned':>10}|{'Profit':>10}|{'Tax':>10}\n")
            for medicine in medicines:
                line = f"{medicine['name']:<20}|{medicine['bought_price']:>15}|{medicine['stock']:>10}|{medicine['sell_price']:>15}|{medicine['sold']:>10}|{medicine['remaining']:>10}|{medicine['earned']:>10}|{medicine['profit']:>10}|{medicine['tax']:>10.2f}"
                f.write(line + "\n")
    except OSError as error:
        print(f"Error: could not write to {DATA_FILE} ({error})")
             


def add_medicine():
    medicine_name = get_text_input("Please enter the name of the medicine: ")
    price_bought_per_unit = get_number_input("Please enter the price bought per unit e.g.30: ", min_value=1)
    stock = get_number_input("Please enter the total stock bought e.g.30: ", min_value=1)
    price_per_unit = get_number_input("Please enter the price per unit sold at e.g.30: ", min_value=1)
    total_sold = get_number_input("Please enter total amount of the medicine sold e.g.30: ", min_value=0, max_value=stock)

    remaining = stock - total_sold
    total_earned = total_sold * price_per_unit
    total_revenue = total_sold * price_bought_per_unit
    total_profit = total_earned - total_revenue

    #check quantity.
    if total_sold > stock:
        print(f"Error cannot have sold {total_sold} more than available stock {stock}")
        return None
    elif total_sold == 0:
        print("No revenue earned, as no stock was sold.")
        return None

    print(f"Medicine bought {medicine_name}")
    print(f"Total amount of {medicine_name} bought to stock {stock}")
    print(f"Total amount of {medicine_name} sold {total_sold}")
    print(f"Stock of {medicine_name} remaining {remaining}")
    print()

    if total_profit > 0:
        print(f"Total amount earned from sale {total_earned}")
        print(f"Total profit earned {total_profit}")
    elif total_profit < 0:
        print(f"Total amount earned from sale {total_earned}")
        print(f"Total loss incurred {abs(total_profit)}")
    else:
        print("You broke even with no profit or loss")
    print()

    tax_owed = calculate_tax(total_profit)

    if total_profit > 0:
        print(f"Tax owed on profit of {total_profit} is {tax_owed}")
    else:
        print("You have no tax obligation, as there is no profit")

    return {
        "name": medicine_name,
        "bought_price": price_bought_per_unit,
        "stock": stock,
        "sell_price": price_per_unit,
        "sold": total_sold,
        "remaining": remaining,
        "earned": total_earned,
        "profit": total_profit,
        "tax": tax_owed
    }



def view_all_medicines(medicines):
    if len(medicines) == 0:
        print("No medicines have been added yet.")
        return

    print()
    print(f"===== ALL MEDICINES ({len(medicines)}) =====")
    for medicine in medicines:
        print(f"Name: {medicine['name']}")
        print(f"  Bought price: {medicine['bought_price']}")
        print(f"  Sell price: {medicine['sell_price']}")
        print(f"  Stock bought: {medicine['stock']}")
        print(f"  Sold: {medicine['sold']}")
        print(f"  Remaining: {medicine['remaining']}")
        print(f"  Earned: {medicine['earned']}")

        if medicine["profit"] > 0:
            print(f"  Profit: {medicine['profit']}")
        elif medicine["profit"] < 0:
            print(f"  Loss: {abs(medicine['profit'])}")
        else:
            print("  Break-even")

        print(f"  Tax owed: {medicine['tax']}")
        print("  ------------------------")

def search_medicine(medicines):
    if len(medicines) == 0:
        print("No medicines have been added yet.")
        return

    search_name = get_text_input("Enter the name of the medicine to search: ")
    found = False

    for medicine in medicines:
        if medicine["name"].lower() == search_name.lower():
            found = True
            print()
            print(f"Found: {medicine['name']}")
            print(f"  Bought price: {medicine['bought_price']}")
            print(f"  Sell price: {medicine['sell_price']}")
            print(f"  Stock bought: {medicine['stock']}")
            print(f"  Sold: {medicine['sold']}")
            print(f"  Remaining: {medicine['remaining']}")
            print(f"  Earned: {medicine['earned']}")
            print(f"  Profit/Loss: {medicine['profit']}")
            print(f"  Tax owed: {medicine['tax']}")

    if found == False:
        print(f"No medicine found with the name '{search_name}'.")



# main program
print("<----- Stage 8: Best Pharmacy Management ----->")


if os.path.exists(DATA_FILE):
    medicines = load_medicines()
    if len(medicines) == 0:
        print("No saved medications available. The pharmacy has just started. ")
    else:
        print(f"Loaded {len(medicines)} medicine(s) from {DATA_FILE}")
else:
    print(f"No saved data exists. Add medicine first. ")
    medicines = []
running = True

while running:
    display_menu()
    choice = input("Please choose an option (1 - 4): ")

    if choice == "1":
        result = add_medicine()
        if result is not None:
            medicines.append(result)
            save_medicine(medicines)
            print("Medicines saved to file")
    elif choice == "2":
        view_all_medicines(medicines)
    elif choice == "3":
        search_medicine(medicines)
    elif choice == "4":
        running = False
    else:
        print("Invalid choice. Please choose a valid option (1 - 4).")

print("Thank you for using the Best Pharmacy Management System. Goodbye!")

