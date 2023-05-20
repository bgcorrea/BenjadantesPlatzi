def dhondt(n, p, seats):
    """
    Implementación del método D'Hondt para asignar escaños a diferentes listas.
    n: número de listas.
    p: lista de porcentajes obtenidos por cada lista.
    seats: número de escaños a asignar.
    """

    # Crear una lista vacía para almacenar los escaños asignados a cada lista.
    assigned_seats = [0] * n

    # Iterar sobre el número de escaños a asignar.
    for i in range(seats):
        # Crear una lista para almacenar los cocientes de D'Hondt de cada lista.
        quotients = []
        # Iterar sobre las listas y calcular el cociente de D'Hondt para cada una.
        for j in range(n):
            quotient = p[j] / (assigned_seats[j] + 1)
            quotients.append(quotient)
        # Obtener el índice de la lista con el cociente de D'Hondt más alto.
        index_max = quotients.index(max(quotients))
        # Asignar un escaño a la lista correspondiente.
        assigned_seats[index_max] += 1

    # Devolver la lista de escaños asignados a cada lista.
    return assigned_seats

# Solicitar al usuario la cantidad de listas, los porcentajes obtenidos por cada lista
# y el número de escaños a asignar.
n = int(input("Ingrese el número de listas: "))
p = []
for i in range(n):
    percentage = float(input(f"Ingrese el porcentaje obtenido por la lista {i + 1}: "))
    p.append(percentage)
seats = int(input("Ingrese el número de escaños a asignar: "))

# Llamar a la función dhondt para asignar los escaños a cada lista.
assigned_seats = dhondt(n, p, seats)

# Imprimir los escaños asignados a cada lista.
for i in range(n):
    print(f"La lista {i + 1} obtuvo {assigned_seats[i]} escaño(s).")
