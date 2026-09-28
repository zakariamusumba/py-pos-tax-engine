def calculate_basic_goods(price,quantity):
    if basic_goods >= 0:
        basic_goods = price * 100
        amount = basic_goods(price,quantity)
        print(f"sold goods at {amount}")
        return(price,quantity)

def calculate_standard_goods(price,quantity):
    if standard_goods >= 16:
        standard_goods = price * 100
        amount = standard_goods(price,quantity)
        print(f"sold goods at {amount}")
        return(price,quantity)

def calculate_luxury_goods(price,quantity):
    if luxury_goods >= 25:
        luxury_goods = cost(price,quantity)
        cost = price * 100
        print(f"sold goods at cost of {cost} %")
    else:
        if luxury_cost <= "25":
            luxury_cost = cost(price / 25)
            print("This amount is not sufficient")
            return(price,quantity)