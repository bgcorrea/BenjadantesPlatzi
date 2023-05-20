if True:
    print("Debería ejecutarse")
if False:
    print("Nunca se ejecuta")
    

pet = input("¿Cuál es tu mascota favorita? ")

if pet == 'perro':
    print('Genial, tienes buen gusto')
if pet == 'gato':
    print('Espero tengas suerte.')
else:
    print('No tienes ninguna mascota :c')

    
'''
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')
'''


# Program to identify pair and unpair numbers

number = int(input('Ingresa un número aquí => '))
if number % 2 == 0:
    print('El número ingresado es par!')
else:
    print('El número ingresado es inpar')