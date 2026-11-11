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

#stage 5 - Functions



def display_menu():
    print()
    print("---- MENU ----")
    print("1. Add medicine and calculate")
    print("2. View last result")
    print("3. Exit")


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


def add_medicine():
    medicine_name = input("Please enter the name of the medicine: ")
    price_bought_per_unit = int(input("Please enter the price bought per unit e.g.30: "))
    stock = int(input("Please enter the total stock bought e.g.30: "))
    price_per_unit = int(input("Please enter the price per unit sold at e.g.30: "))
    total_sold = int(input("Please enter total amount of the medicine sold e.g.30: "))

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

def view_last_result(result):
    if result is None:
        print("No medicine has been added yet.")
        return

    print(f"Last medicine: {result['name']}")
    print(f"Last bought price: {result['bought_price']}")
    print(f"Last total bought: {result['stock']}")
    print(f"Last total sold: {result['sold']}")
    print(f"Last sell price: {result['sell_price']}")
    print(f"Last stock remaining: {result['remaining']}")
    print(f"Last amount earned: {result['earned']}")

    if result["profit"] > 0:
        print(f"Last profit: {result['profit']}")
    elif result["profit"] < 0:
        print(f"Last loss: {abs(result['profit'])}")
    else:
        print("Last result: break-even")

    print(f"Last tax owed: {result['tax']}")


# main program
print("<----- Stage 5: Best Pharmacy Management ----->")

last_result = None
running = True

while running:
    display_menu()
    choice = input("Please choose an option (1 - 3): ")

    if choice == "1":
        result = add_medicine()
        if result is not None:
            last_result = result
    elif choice == "2":
        view_last_result(last_result)
    elif choice == "3":
        running = False
    else:
        print("Invalid choice. Please choose a valid option (1 - 3).")

print("Thank you for using the Best Pharmacy Management System. Goodbye!")


