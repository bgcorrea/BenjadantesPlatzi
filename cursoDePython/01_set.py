'''
[LIST]
(TUPLE)
{SET}
'''



set_countries = {'col', 'mex', 'bol', 'col'} # If i repeat a value, it will be deleted because a set doesn't incluided same values.
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

# Set from string
set_from_string = set('hoola')
print(set_from_string)

# Set from a Tuple
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# Set from a list
numbers = [1, 2, 3, 4, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers) # If I change list to set, automatically it will be changed to unique values.

unique_numbers = list(set_numbers)
print(unique_numbers)