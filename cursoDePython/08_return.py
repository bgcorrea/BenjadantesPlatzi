def sum_with_range(min, max):
    print(f'El número mínimo ingresado es {min} y el máximo ingresado es {max}')
    sum = 0
    for x in range(min, max):
        sum += x
    return sum
    
result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
sum_with_range(1, 100)