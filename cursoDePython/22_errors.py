try:
    print (0/0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('No se aceptan menores de edad')
except Exception as error:
    print(error)

try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual a uno'
    age = 10
    if age < 18:
        raise Exception('No se aceptan menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
    
print('Hola')

def my_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as error:
        result = 'No se puede dividir por 0'
    return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response)