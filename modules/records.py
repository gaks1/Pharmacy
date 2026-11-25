# Creating loading and sving medicines in a txt file

from modules.calculations import calculate_results
from modules.validations import get_number_input, get_text_input

DATA_FILE = "medicine.txt"


def load_medicines():
    """
    Load all medicine records from the data file.
    """
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

    # skip the header
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
                "cost": int(parts[7].strip()),
                "profit": int(parts[8].strip()),
                "tax": float(parts[9].strip())
            }
        except (ValueError, IndexError):
            print(f"Warning: line {line_number} is damaged and was skipped.")
            continue

        medicines.append(medicine)

    return medicines


def save_medicine(medicines):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(f"{'Name':<20}|{'Bought Price':>15}|{'Stock':>10}|{'Sell Price':>15}|{'Sold':>10}|{'Remaining':>10}|{'Earned':>10}|{'Cost':>10}|{'Profit':>10}|{'Tax':>10}\n")
            for medicine in medicines:
                line = f"{medicine['name']:<20}|{medicine['bought_price']:>15}|{medicine['stock']:>10}|{medicine['sell_price']:>15}|{medicine['sold']:>10}|{medicine['remaining']:>10}|{medicine['earned']:>10}|{medicine['cost']:>10}|{medicine['profit']:>10}|{medicine['tax']:>10.2f}"
                f.write(line + "\n")
    except OSError as error:
        print(f"Error: could not write to {DATA_FILE} ({error})")


def add_medicine():
    """
    Ask the user for details and return a new medicine record, or None.
    """
    medicine_name = get_text_input("Please enter the name of the medicine: ")
    stock = get_number_input(
        "Please enter the total stock bought e.g.30: ", min_value=1)
    price_bought_per_unit = get_number_input(
        "Please enter the price bought per unit e.g.30: ", min_value=1)
    price_per_unit = get_number_input(
        "Please enter the price per unit sold at e.g.30: ", min_value=1)
    total_sold = get_number_input(
        "Please enter total amount of the medicine sold e.g.30: ",
        min_value=0, max_value=stock)

    if total_sold == 0:
        print("No revenue earned, as no stock was sold.")
        return None

    results = calculate_results(price_bought_per_unit, stock,
                                price_per_unit, total_sold)

    return {
        "name": medicine_name,
        "bought_price": price_bought_per_unit,
        "stock": stock,
        "sell_price": price_per_unit,
        "sold": total_sold,
        "remaining": results["remaining"],
        "earned": results["earned"],
        "cost": results["cost"],
        "profit": results["profit"],
        "tax": results["tax"]
    }