import numpy as np
arr = np.array( [1, 2, 3, 4])
print(arr)
print(arr.dtype)

arr = np.array( [1, 2, 3, 4], dtype='float64')
print(arr.dtype)

arr = np.array( [0, 1, 2, 3, 4])
arr = arr.astype(np.bool_)
print(arr.dtype)

arr = np.array( [0, 1, 2, 3, 4])
arr = arr.astype(np.string_)
print(arr.dtype)
print(arr)

hola = np.arange(0,10)
print(hola)
