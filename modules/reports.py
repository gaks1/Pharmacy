# contains all the diplay output to the user

from modules.validations import get_text_input

def display_menu():
    print()
    print("---- MENU ----")
    print("1. Add medicine and calculate")
    print("2. View all medicines")
    print("3. Search for a medicine")
    print("4. Exit")

def print_medicine_result(medicine):
    print(f"Medicine bought {medicine['name']}")
    print(f"Total amount of {medicine['name']} bought to stock {medicine['stock']}")
    print(f"Total amount of {medicine['name']} sold {medicine['sold']}")
    print(f"Stock of {medicine['name']} remaining {medicine['remaining']}")
    print()

    if medicine["profit"] > 0:
        print(f"Total amount earned from sale {medicine['earned']}")
        print(f"Total profit earned {medicine['profit']}")
    elif medicine["profit"] < 0:
        print(f"Total amount earned from sale {medicine['earned']}")
        print(f"Total loss incurred {abs(medicine['profit'])}")
    else:
        print("You broke even with no profit or loss")
    print()

    if medicine["profit"] > 0:
        print(f"Tax owed on profit of {medicine['profit']} is {medicine['tax']}")
    else:
        print("You have no tax obligation, as there is no profit")


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

    if not found:
        print(f"No medicine found with the name '{search_name}'.")