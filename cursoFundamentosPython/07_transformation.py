name = "Benjamín"
print(type(name))
name = 12
print(type(name))
name = False
print(type(name))

# It possible to change a variable in dinamic form.

print("Nicolás" + " Molina")
print(10 + 20)
# print("Nicolás" + 10) It not possible concatenate two types of data.

age = 12
print("Mi edad es " + str(age)) # Is necessary transform the variable age to string to concatenate this print.
print (f"Mi edad es {age}") # Another way wich is not necessary change the type of the data.

#age = input('Escribe tu edad aquí => ')
age= int(input("Ingresa tu edad aquí =>")) # Shortcut
# print(type(age))
# age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')