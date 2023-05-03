# Dictionary type is the key-value pair data type
# Empty dictionary can be created using curly braces {} or dict)_ built-in function

student = dict() # This is an empty dictionary
print(student)
student = {} # This is also an empty dictionary
print(student)
student = {"name": "John", "age": 45, "department": "CS"} # Non empty dictionary
print(student)
student = dict(name="John", age=45, department="CS") # Non enpty dictionary
print(student)

student = dict([
    ("name", "Bantu"),
    ("age", 27),
    ("department", "IT")
])
print(student) # This is also a dictionary

student = {"name": "Bibli", "age": 25, "department": "management"}
name = student['name']
print(name) # Result is Bibli
print(student['department']) # Result is management
# print(student['roll_number']) # It gives KeyError because roll_number is not a key of dictionary student

# We can also access the dictionary values using get() method
name = student.get('name')
print(name)

roll_number = student.get('roll_number')
print(roll_number) # This gives None. If the key not present in the dictionary is provided to the get() method then it returns None

# We can also provide a default value to the get() method
roll = student.get("roll_number", 4) # Here 4 is a default value
print(roll) # Result is 4
name = student.get("name", "Jane") # Here Jane is a default value
print(name) # Result is John

# Adding and updating dictionary
student = {"name": "John", "age": 45, "department": "CS"}
student["roll"] = 4
print(student) # Result is {'name': 'John', 'age': 45, 'department': 'CS, 'roll': 4}
# If the key is already present in the dictionary then it gets updated
student['name'] = "Jane"
print(student)

# Updating dictionary using update() method
student = {"name": "John", "age": 45}
student.update({"department": "CS", "roll": 4})
print(student)
# Result is {'name': 'John', 'age': 45, 'department': 'CS', 'roll': 4}

student.update(id=1, height= 5.8)
print(student)
# Result is {'name': 'John', 'age': 45, 'department': 'CS', 'roll': 4, 'id': 1, 'height': 5.8}

# Deleting / Removing dictionary key-values
student = {
    "name": "John",
    "age": 45,
    "department": "CS",
    "roll": 4,
    "id": 1,
    "height": 5.8
}
roll = student.pop("roll")
print(student) # Roll key is removed from the dictionary
print(roll) # 4

# Rules for Dictionary Keys and Values
# 1. Dictionary keys must be immutable
# 2. Dictionary values can be of any data type
# 3. A tuple can also be a dictionary key because it is immutable type. But, if it contains mutable type, then it can't be used as a key
#   Example d = {(1, 2, [1, 2]): "Hello} # This is invalid

# Membership Operation in Dictionary
student = {"name": "John", "age": 23}
print("age" in student) # True. Membership is checked in key in a dictionary
print("department" in student) # False

