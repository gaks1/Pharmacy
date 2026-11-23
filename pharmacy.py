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

#Stage 9 - Error Handling

import os

from modules import records, reports, validations


def main():
    print("<----- Stage 9: Best Pharmacy Management ----->")

    if os.path.exists(records.DATA_FILE):
        medicines = records.load_medicines()
        if len(medicines) == 0:
            print("No saved medications available. The pharmacy has just started.")
        else:
            print(f"Loaded {len(medicines)} medicine(s) from {records.DATA_FILE}")
    else:
        print("No saved data exists. Add medicine first.")
        medicines = []

    running = True

    while running:
        reports.display_menu()
        choice = validations.validate_menu_choice()

        if choice == "1":
            result = records.add_medicine()
            if result is not None:
                medicines.append(result)
                records.save_medicine(medicines)
                reports.print_medicine_result(result)
                print("Medicines saved to file")
        elif choice == "2":
            reports.view_all_medicines(medicines)
        elif choice == "3":
            reports.search_medicine(medicines)
        elif choice == "4":
            running = False

    print("Thank you for using the Best Pharmacy Management System. Goodbye!")


if __name__ == "__main__":
    main()

