#list: is a collection which is ordered and changeable. Allows duplicate members.
#Lists are written with square brackets.

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

#deleting list items

this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)

#deleting multiple items:
top_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
del top_cities[1:4]
print(top_cities)

#adding elements to a list:
my_fruits = ["apple", "banana", "cherry"]
my_fruits.append("orange")
print(my_fruits)

my_fruits.insert(1, "grape")
print(my_fruits)

#iterating through a list:
my_cars = ["Toyota", "Honda", "Ford"]
for car in my_cars:
    print(car, end=" ")

#swapping element positions:
my_fruits = ["apple", "banana", "cherry"]
my_fruits[0], my_fruits[2] = my_fruits[2], my_fruits[0]
print(my_fruits)

#sorting a list alphabetically:
colors = ["red", "blue", "green", "yellow"]
colors.sort()
print(colors)

#sorting a list in reverse order:
colors.sort(reverse=True)
print(colors)

#copying lists using slicing:
original_list = ["apple", "banana", "cherry"]
copied_list = original_list[:]
original_list[0] = "grape"
print('Original list:', original_list)
print('Copied list:', copied_list)



#list comprehension: is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#Example: create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

numbers = [i for i in range(20) if i % 2 == 0]
print(numbers)


#nested lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # for a new line after each row


#Adding and Multiplying Lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

multiplied_list = list1 * 3
print(multiplied_list)