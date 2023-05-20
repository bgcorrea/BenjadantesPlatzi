price = 100 # Global scope

def increment():
    price = 200 # Local scope
    result = price + 10
    print(price)
    return price


print(price)
price_2 = increment()
print(price_2)
