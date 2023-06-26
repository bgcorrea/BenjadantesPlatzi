import numpy as np
arr = np.random.randint(1, 20, 10)
print(arr)
matriz = arr.reshape(2, 5)

print(matriz.max())
print(matriz.max(0))
print(matriz.max(1))
print(matriz.argmax())

print(matriz.min())
print(matriz.min(0))
print(matriz.min(1))

print(arr.ptp()) # Peak to peak
print(matriz)
print(matriz.ptp(0))

print(np.percentile(arr, 50))
arr = np.random.randint(1, 20, 10)
print(arr.sort())
print(np.median(arr))
print(np.std(arr))
print(np.var(arr)) # varianza = desviación estandar ^ 2
print(np.mean(arr))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b.T), axis=1)
print(c)