# Lambda expressions are another way of creating functions.
# they are called anonymous function because they do not have a name (they are a single line of logical code)
# the terms: lambda expressions, lambda functions, anonymous functions or function literals can be used interchangeably

#lambda expressions are good if you only need them once for quick and simple solutions between large code blocks

#Syntax: lambda parameters: expression
# the result of this function is returned automatically
result = (lambda a, b, c: a + b +c)(3, 4, 5)
print(result)

# lambda that squares a number:
square = lambda x: x ** 2
print(square(4))


#another example:
friends = [('Diana', 30), ('Ana', 25), ('Tudor',22)]
friends.sort(key=lambda x: x[1])
print(friends)

#
friends.sort(key=lambda x: len(x[0]))
print(friends)