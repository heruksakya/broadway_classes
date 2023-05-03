student = {"name": "John", "age": 23}
print(all(student)) # Returns True if all the values in the iterable area Truthy. Here result is True. This is like 'and' operation

print(all([])) # This is an exception because it gives True.

print(any(student)) # This gives True. any() returns True if any of the elements in an iterable is Truthy. This is like 'or' operation

print(any([]))  # This gives False

result = sorted(student)
print(result) # ['age', 'name']

student = {"name": "Aastha", "age": 30}
print(student.items()) # It gives list like objects [("name", "Aastha"), ("age", 30)

print(student.keys()) # It gives list like objects of dictionary keys
# Result ["name", "age:]

print(student.values())
# Result ["Aastha", 30]

d = student.fromkeys(([1, 2, 3]), "Hello")
print(d) # This gives a new dictionary with keys of iterable with common value
# Result {1: "Hello", 2: "Hello", 3: "Hello"}

d = student.fromkeys([1, 2, 3])
print(d) # {1: None, 2: None, 3: None}