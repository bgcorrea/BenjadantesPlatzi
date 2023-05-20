'''
for element in range(1, 21): # range create the iteration
    print(element)
'''
# Iterate a list
my_list = [23, 45, 67, 89, 43]

for i in my_list:
    print(i)    

'''
¿Cúando usar “while” o “for” ?
while: cuando no nonozcas la cantidad de elementos a recorrer o la cantidad de iteraciones a realizar.
for: cuando conozas la cantidad de elementos a recorrer o el número de iteraciones a relaizar.
'''
# Iterate a tuple
my_tuple = ('nico', 'juli', 'santi')

for i in my_tuple:
    print(i)
    
# Iterate a dictionary
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for i in product:
    print(i,'=>', product[i])
    
for key in product:
    print(key, '=>', product[key])
    
for key, value in product.items():
    print(key, '=>', value)
    
    
people = [
    {
        'name': ' nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

for person in people:
    print(person)
    
for person in people:
    print('name =>', person['name'])
    
    
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for i in my_list:
  if i > 0:
    new_list.append(i)

print(new_list)