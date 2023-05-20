lives = 3
print(type(lives)) # es un entero o int
age = 26
budget = 300

temperature = 12.12
print(type(temperature)) # es un float

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

number = 45500000000000000000000000.1
print(number)

number = 0.000000000000000000000000000001
print(number)

from statistics import mean

budgetEnero = int(input("¿Cuál es su presupuesto del mes de Enero?"))
budgetFebrero = int(input("¿Cuál es su presupuesto del mes de Febrero?"))
budgetMarzo = int(input("¿Cuál es su presupuesto del mes de Marzo?"))
mean = (budgetEnero + budgetFebrero + budgetMarzo) / 3
# mean = mean([budgetEnero, budgetFebrero, budgetMarzo])
print(f"El promedio de los tres meses indicados anteriormente es {mean}")
