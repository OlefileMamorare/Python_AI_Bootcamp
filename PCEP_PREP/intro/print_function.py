print('Hello')
#each print call adds a newline character at the end by default, which is why each print statement appears on a new line. If you want to change this behavior, you can use the 'end' parameter of the print function.  For example:
print('Hello', end=' ')  # This will print 'Hello' followed by a space instead of a newline
print('World!')  # This will print 'World!' on the same line as 'Hello'


# escape characters:
print('I\'m learning Python')  # using backslash to escape the single quote
print("She said, \"Hello!\"")  # using backslash to escape the double quote
print("This is a backslash: \\")  # using double backslash to print a single backslash

#Printing multiple items:
name = "Alice"
age = 30

print("Name:", name, "Age:", age)  # This will print 'Name: Alice Age: 30' with spaces in between.

