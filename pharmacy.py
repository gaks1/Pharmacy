#Stage 10 - Testing and Refinement

import os

from modules import records, reports, validations


def main():
    print("<----- Stage 10: Best Pharmacy Management ----->")

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

