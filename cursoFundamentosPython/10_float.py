x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# Two ways to transform the float

# Hard way: not mathematic

y_str = format(y, ".2g") # When we only need 2 digits
print('str =>', y_str)
print(y_str == str(x))

# Mathematic: tolerance margin

print("*" * 10)

print(y, x)
tolerance = 0.00001
print(abs(x-y) < tolerance)
