# Strings in Python are of immutable type
# We can create an empty string using str{} built-in function or using empty single or double quotes

example = "" # Empty string double quotes
print(example)
example = '' # Empty string using single quotes
example  = str() # Empty string
print(example)

example = "Hello World" # This is a valid string
# example = 'Hello World" # Invalid string
# example = "Hello World' # Invalid string

# Escape sequences
# Escape sequence / Characters are the strings in python which suppresses the usual meaning of a chracter and gives a new meaning
example = 'I\'m learning Python' # Here \' is an escape character
print(example)
example = "Path to my folder is C:\\Project\\broadway" # Here \\ is an escape character
print(example)
example = "Hello\nWorld" # Here \n is a new-line escape character
print(example)
example = "Hello\tWorld" # Here \t is a new-line escape character for tab
print(example)
example = "Hello\bWorld" # Here \b is an escape character for a backspace
print(example)

# Triple quoted strings
example = '''
Example1
'''
print(example) # Example with triple single quotes

example = """
Example2
"""
print(example) # Example with triple double quotes

example = """
I'm Learning Python
"""
print(example) # We don't need to use escape character for single/double quotes in triple quoted string

# Triple quoted string
"""
Function to calculate difference. We can treat this as a multiline comment
"""
def fxn(a, b):
    return a-b

# Indexing and slicing in string
# String indexing and slicing is similar to list slicing and indexing
message = "Hello World"
print(message[3]) # This gives 'l'
print(message[6]) # This gives 'W'. Space is also considered as a character
print(message[-2]) # Negative indexing is also possible. It gives 'l'
print(message[1: 7: 2]) # Results 'el '
print(message[1:- 3]) # Results 'ello Wo'
print(message[-7: -3]) # Results 'lo Wo'
print((message[-3: -7])) # Results ''

#String doesn't support item assignment because it is immutable
message = "Hello"
message[1] = "E" # This is not possible
