set_countries = {'col', 'mex', 'bol', 'col'} 

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add

set_countries.add('pe')
print(set_countries)

set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'chi', 'arg'})
print(set_countries)

# remove 

set_countries.remove('col')
print(set_countries)

set_countries.discard({'arg'})
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))