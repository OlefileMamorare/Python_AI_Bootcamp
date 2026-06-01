#tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#empty tuple:
empty_tuple = ()

#tuple with items:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#one element tuple:
single_tuple = ("apple",)
print(single_tuple)

#tuples are immutable, meaning you cannot change their items after they have been created. However, you can concatenate tuples to create a new tuple:
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "date")
combined_tuple = tuple1 + tuple2
print(combined_tuple)

#accessing tuple items:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana

#tuple operations:
user_data = ('John', 30, 'Engineer', 'John')
print(len(user_data))  # Output: 4
print(user_data.count('John'))  # Output: 2
print(user_data.index('John'))  # Output: 0