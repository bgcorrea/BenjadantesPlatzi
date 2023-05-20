def increment(x):
    return x + 1

def higher_ord_func(x, func):
    return x + func(x)

increment_v2 = lambda x: x + 1

higher_ord_func_v2 = lambda x, func: x + func(x)


result = higher_ord_func(2, increment)
print(result)

result = higher_ord_func_v2(2, increment_v2)
print(result)

result = higher_ord_func_v2(2, lambda x: x + 2)
print(result)