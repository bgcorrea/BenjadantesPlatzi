# CRUD: Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) # insert a element at the end of the list
print(numbers)

numbers.insert(0, 'hola')  # insert a element at the beginning of the list
print(numbers)

tasks = ['Hola', 'Chao', 'Afternoon']
new_list = numbers + tasks
print(new_list)

index = new_list.index('Hola')
new_list[index] = 'todo changed'
print(new_list)

'''
new_list.append('Chao')
print(new_list)
index = new_list.index('Chao')
new_list[index] = 'nothing changed'
print(new_list)
'''

new_list.remove('Chao') # Remove based in the instructions 
print(new_list)

new_list.pop() # Remove based in the instructions of the position
print(new_list) 

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 5, 4, 2, 3, 6] # Order array of elements, low to high
numbers_a.sort()
print(numbers_a)

lista = ['Hola', 'Chao', 'Afternoon'] # Order array of elements, alphabetic order
lista.sort()
print(lista)

# If the array have a mix of types, the sort method doesn't work.

letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

letters.append('G')
letters[0] = 'Z'
letters.remove('C')
letters.reverse()
print(letters)