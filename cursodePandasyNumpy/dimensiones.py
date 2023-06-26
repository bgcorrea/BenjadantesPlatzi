import numpy as np

scalar = np.array(42)
print(scalar)
print(scalar.ndim)

scalar = np.array([1, 2, 3])
print(scalar)
print(scalar.ndim)

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
print(matriz.ndim)

matriz = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(matriz)
print(matriz.ndim)

# Agregar o eliminar dimensiones

vector = np.array([1, 2, 3], ndmin=10)
print(scalar)
print(scalar.ndim)

expand = np.expand_dims(np.array([1, 2, 3]), axis=0)
print(expand)
print(expand.ndim)

print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)
