# Arithmetic Operators
a = 10
b = 5

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication

print(a / b)  # Division
print(a // b) # Floor Division
#The floor division operator (//) divides the first operand by the second operand and rounds down to the nearest whole number. For example, 10 // 3 will return 3, because 10 divided by 3 is approximately 3.33, and rounding down gives you 3.

#If you have a negative number, the floor division operator will round down to the next lowest integer. For example, -10 // 3 will return -4, because -10 divided by 3 is approximately -3.33, and rounding down gives you -4.

#If you integer divide two integers, the result is of type integer. But if at least one of the input numbers is a float, you will get a float instead. For example, 10 // 3 will return 3 (integer), but 10.0 // 3 will return 3.0 (float).
print(b // a)


print(a % b)  # Modulus
#if you have a negative number, the modulus operator will return a positive result. For example, -10 % 3 will return 2, because -10 divided by 3 is -3 with a remainder of 2.
#if you have x % y, and the second number (y) is greater than the first number (x), the modulus operator will return x. For example, 5 % 10 will return 5, because 5 divided by 10 is 0 with a remainder of 5.

print(a ** b) # Exponent

# Comparison Operators
print(a == b) # Equal to
print(a != b) # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to

# Logical Operators
x = True
y = False

print(x and y) # Logical AND
print(x or y)  # Logical OR
print(not x)   # Logical NOT