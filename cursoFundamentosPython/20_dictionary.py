person = {
    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python', 'javascript'],
    'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['last_name'] # corchetes
person.pop('age') # parethesis
print(person)

print('items')
print(person.items()) # keys and values

print('keys')
print(person.keys()) # only keys

print('values')
print(person.values()) # only values


