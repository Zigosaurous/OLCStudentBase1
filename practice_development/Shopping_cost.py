def total_cost(cost):
    total = cost * 1.07
    return total

def discount(cost):
    if cost >= 50 and cost < 100:
        amount = total_cost(cost)
        price = amount*0.95
        return price
    elif cost >= 100:
        amount = total_cost(cost)
        price = amount*0.90
        return price
    else:
        price = total_cost(cost)
        return price

def voucher(price):
    
