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

#stage 1

print("<----- Stage 4: Best Pharmacy Management ----->")
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
elif total_sold == 0:
    print("No revenue earned, as no stock was sold.")    
else:
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
        print(" You broke even with no profit or loss ")
    print()    



tax_owed = 0

if total_profit > 0 and total_profit <= 250:
    taxable_income = total_profit - 0
    tax1 = taxable_income * 0.1
    tax_owed+=tax1
elif total_profit > 250 and total_profit <= 500:
    taxable_income = total_profit - 250
    tax2 = taxable_income * 0.2
    tax_owed+=tax2
elif total_profit > 500:
    taxable_income = total_profit - 500
    tax3 = taxable_income * 0.3
    tax_owed+=tax3

if total_profit > 0:    
    print(f"Tax owed on profit of {total_profit} is {tax_owed}")
else:
    print("You have o tax obligation, as there is no profit")
