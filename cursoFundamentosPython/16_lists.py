numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

comunas = ['Maipú', 'Las Condes', 'San Ramón']
print(comunas)
comunas_n = [1, 0, 1]

print('*' * 10)
from statistics import mean
promedio = mean(comunas_n)
print(promedio)

print('*' * 10)

types = {1, True, 'Hola'}
print(type(types)) # set

tasks = ['Jugar play', 'Pasear al perro']
print(tasks)
tasks[0] = 'Bañarse'
print(tasks)

print(numbers[:3])