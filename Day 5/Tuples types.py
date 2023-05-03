# Tuple data types are similar to python list type but they are immutable
# Indexing and slicing in tuple is same as that of list
# Empty tuple can be created using parenthesis () or tuple() built-in function

t = tuple() # An empty tuple
print(t)
t = (1, 2, 3) # A non-empty tuple
print(t)
t = tuple([1, 2, 3]) # tuple() function takes iterable as a parameter
print(t)

# Creating a tuple with a single element
t = (1) # This seems like a tuple but it is an integer type
print(type(t)) # Int
t = (1, ) # We need to add a comma while creating tuple with single element
print(type(t)) # Tuple

# Tuple packing and unpacking
t = 1, 2, "Hello World" # A tuple can be created without using parenthesis as given in this example. This type of tuple creating is tuple packing

# Assigning of the tuple elements to individual variables in the LHS is called tuple unpacking
a, b, c = 1, 2, "Hello World"
print(a) # Results 1
print(b) # Results 2
print(c) # Results "Hello World"

# This is how we do swapping normally in other languages. With the use of third variable 'c'
a = 1
b = 2
c = a
a = b
b = c
print(a)
print(b)

# Swapping can be implemented easily in python with tuple packing and unpacking
a = 1
b = 2
a, b = b, a # Swapping using tuple packing/unpacking
print(a)
print(b)

# Elements in LHS must be equal to RHS in tuple packing and unpacking else it raises an error
# a, b = 1, 2, 3 # This raises an error
# a, b, c = 1, 2 # This also raises an error

# Indexing and slicing in tuple is same as that of list
a = (1, 2, 3, 4, 5, 6, 7)
print(a[::2]) # This traverses forward jumping one step

print(a[-2:-6:-1]) # Providing negative step size traverse the sequence from backwards. Results (6, 5, 4, 3)
print(a[::-1]) # This reverses the sequence. Results (7, 6, 5, 4, 3, 2, 1)

del a # this deletes tuple 'a' (del keyword deletes any object)

