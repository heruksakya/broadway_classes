s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s = s1.union(s2) # It gives union of two sets
print(s)
s = s1.intersection(s2) # It gives intersection of two sets
print(s)

s1.isdisjoint(s2) # s1 and s2 are not disjoint set as they have common elements {4, 5}. So it gives False

s = s1.symmetric_difference(s2) # This is a complement of s1 intersection s2. Result is {1, 2, 3, 6, 7, 8}

s1.symmetric_difference_update(s2) # This updates the symmetric difference of s1 and s2 to s1
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4}
print(s2.issubset(s1)) # True
print(s1.issuperset(s2)) # True
print(s2.issuperset(s1)) # False

# Bitwise operators in set operations
s = s1 | s2 # Union
print(s)
s = s1 & s2 # Intersection
print(s)
s = s1 - s2 # Difference
print(s)
s = s1 ^ s2 # Symmetric difference. It is same as s1.symmetric_difference(s2)
print(s)

