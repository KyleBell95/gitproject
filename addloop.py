def addloop(groceries):
    print(groceries)
    prices = 0.00
    for x in groceries:
        #prices = prices + x
        prices += x
    return prices




#MAIN
groceryPrices = [12.12, 13.23, 6.00]
print(addloop(groceryPrices))
print(sum(groceryPrices))