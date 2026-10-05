# Application: Pharmacy Management System
# Problem: Managing medicine inventory and sales, and taxes.
# Output: Total profits and losses, and tax owed on profit.
# Users: Pharmacist.
# Features: Add a medicine name, stock, price per unit and price of total sales of a certain units to get totals and tax owed on profit.

#stage 1

print("<---- Stage 1 Best Pharmacy Management ---->")
medicine_name = "Paracetamol"
price_bought_per_unit = 5
stock = 1000
price_per_unit = 10
total_sold = 200

remaining = stock - total_sold
total_earned = total_sold * price_per_unit
total_revenue = total_sold * price_bought_per_unit
total_profit = total_earned - total_revenue

print(f"Medicine bought {medicine_name}")
print(f"Total amount of {medicine_name} bought to stock {stock}")
print(f"Total amount of {medicine_name} sold {total_sold}")
print(f"Stock of {medicine_name} remaining {remaining}")
print(f"Total amount earned from sale {total_earned}")
print(f"Total profit earned {total_profit}")

#stage 2
print()
print("<----- Stage 2: Best Pharmacy Management ----->")

medicine_name2 = input("Please enter the name of the medicine ")
price_bought_per_unit2 = int(input("Please enter the price bought per unit e.g.30 "))
stock2 = int(input("Please enter the total stock bought e.g.30 "))
price_per_unit2 = int(input("Please enter the price per unit sold at e.g.30 "))
total_sold2 = int(input("Please enter total amount of the medicine sold e.g.30 "))

remaining2 = stock2 - total_sold2
total_earned2 = total_sold2 * price_per_unit2
total_revenue2 = total_sold2 * price_bought_per_unit2
total_profit2 = total_earned2 - total_revenue2


print(f"Medicine bought {medicine_name2}")
print(f"Total amount of {medicine_name2} bought to stock {stock2}")
print(f"Total amount of {medicine_name2} sold {total_sold2}")
print(f"Stock of {medicine_name2} remaining {remaining2}")
print(f"Total amount earned from sale {total_earned2}")
print(f"Total profit earned {total_profit2}")
print()

#stage 3
print("<----- Stage 3: Best Pharmacy Management ----->")
medicine_name3 = input("Please enter the name of the medicine ")
price_bought_per_unit3 = int(input("Please enter the price bought per unit e.g.30 "))
stock3 = int(input("Please enter the total stock bought e.g.30 "))
price_per_unit3 = int(input("Please enter the price per unit sold at e.g.30 "))
total_sold3 = int(input("Please enter total amount of the medicine sold e.g.30 "))

remaining3 = stock3 - total_sold3
total_earned3 = total_sold3 * price_per_unit3
total_revenue3 = total_sold3 * price_bought_per_unit3
total_profit3 = total_earned3 - total_revenue3

#check quantity. 
if total_sold3 > stock3:
    print(f"Error cannot have sold {total_sold3} more than available stock {stock3}")
elif total_sold3 <= stock3:
    print(f"Medicine bought {medicine_name3}")
    print(f"Total amount of {medicine_name3} bought to stock {stock3}")
    print(f"Total amount of {medicine_name3} sold {total_sold3}")
    print(f"Stock of {medicine_name3} remaining {remaining3}")
    print(f"Total amount earned from sale {total_earned3}")
    print(f"Total profit earned {total_profit3}")
    print()
elif total_sold3 == 0:
    print("No revenue earned, as no stock was sold.")
else:
    print("System done")

tax_owed = 0
if total_profit3 > 0 and total_profit3 <= 250:
    taxable_income = total_profit3 - 0
    tax1 = taxable_income * 0.1
    tax_owed+=tax1
elif total_profit3 > 250 and total_profit3 <= 500:
    taxable_income = total_profit3 - 250
    tax2 = taxable_income * 0.2
    tax_owed+=tax2
elif total_profit3 > 500:
    taxable_income = total_profit3 - 500
    tax3 = taxable_income * 0.3
    tax_owed+=tax3
print(f"Tax owed on profit of {total_profit3} is {tax_owed}")
