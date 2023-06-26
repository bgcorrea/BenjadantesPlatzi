# Array
# La estructura central de NumPy

import numpy as np
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

arr = np.array(lista)
print(arr)
print(type(arr))


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(matriz)
print(matriz)

print(arr[0])
print(matriz[0])

suma = arr[0] + arr[2]
print(suma)

print(matriz[0,2])

# Slicing

print(arr[0:3]) # Start and end

print(arr[:6])
print(arr[2:]) # I can work without start and without end :)

print(arr[::3]) # tres en tres

print(arr[-1])

print(matriz[1:, 1:])