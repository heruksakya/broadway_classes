# String formatting using %

m = "Hello I'm %s. I'm %d years old" %("John", 45)
print(m)

m = "I have Rs %.2f" %(30.4567)
print(m)

# String formattingusing format() method

m = "Hello I'm {}".format("John")
print(m)

m = "I'm {age} years old".format(age=45)
print(m)

m = "I have {0}, {1} and {2}".format("pen", "pencil", "copy")
print(m) # Result is I have pen, pencil and copy
m = "I have {1}, {0} and {2}".format("pen", "pencil", "copy")
print(m) # Result is I have pencil, pen and copy

# If we don't give index and have multiple placeholders then the values are taken in order
m = "I have {}, {} and {}".format("pen", "pencil", "copy")
print(m) # Result is I have pen, pencil and copy

