#Profit loss and tax calculations


def calculate_tax(profit):
    """
    Return the tax owed on the given profit. A loss owes no tax.
    """
    if profit <= 0:
        return 0

    tax_owed = 0
    if profit <= 250:
        tax_owed += (profit - 0) * 0.1
    elif profit <= 500:
        tax_owed +=  (profit - 250) * 0.2
    else:
        tax_owed += (profit - 500) * 0.3
    return tax_owed

def calculate_results(bought_price, stock, sell_price, sold):
    """
    Return a dictionary of all calculated figures for one medicine.
    """
    remaining = stock - sold
    earned = sold * sell_price
    cost = sold * bought_price
    profit = earned - cost
    tax = calculate_tax(profit)

    return {
        "remaining": remaining,
        "earned": earned,
        "cost": cost,
        "profit": profit,
        "tax": tax
    }