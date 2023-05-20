my_dict = {}
print(type(my_dict))

my_dict = {
    'avión': 'bla bla bla',
    'name': 'Benjamín',
    'last_name': 'Correa',
    'age': 26
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('unvalor')) # Best option if I don't know if the key exists

print('avión' in my_dict) # I ask if the key exists
print('otroqueno' in  my_dict)