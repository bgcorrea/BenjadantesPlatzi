import numpy as np
arr = np.arange(0, 11)
print(arr)
fraccion = (arr[0:6])
fraccion[:] = 0
print(fraccion)
print(arr)

arr_copy = arr.copy()
print(arr_copy)