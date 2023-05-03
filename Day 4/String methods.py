m = "hello world"
print(m.capitalize()) # Result is Hello world
print((m.title())) # Result is Hello World
print(m.upper()) # Result is HELLO WORLD
print(m.lower()) # Result is hello world

result = m.split() # Result is ["hello, "world"]. Splits from a space
print(result)
result = m.split('e') # Splits from 'e'. Result ['h', 'llo world']
print(result)
result = m.split('o') # Splits from 'o'. Result ['hell', ' w', rld']
print(result)

message = ["Hello", "World"]
" ".join(message) # This joins the list with a space (" ") and returns "Hello World"
print(message)
"+".join(message) # This joins the list with a + and returns "Hello+World
print(message)

m = "Hello World"
result = m.find("Wo") # 'Wo' in the string is at 6th position. Result is 6
print(result)
result = m.find("Wooo") # 'Wooo' is not present in the list. Result is -1
print(result)

m.replace("World", 'world') # Replace 'World' in the string to 'world'
print(result) # Result is "Hello world"

