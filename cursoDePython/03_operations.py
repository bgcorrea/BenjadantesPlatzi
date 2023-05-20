set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union
set_union = set_a.union(set_b)
print(set_union)
print(set_a | set_b)

# Intersection
set_intersection = set_a.intersection(set_b)
print(set_intersection)
print(set_a & set_b)

# Difference
set_difference = set_a.difference(set_b)
print(set_difference)
print(set_a - set_b)

# Symmetric Difference: is like an union without the common elements
set_symmetric_difference = set_a.symmetric_difference(set_b)
print(set_symmetric_difference)

