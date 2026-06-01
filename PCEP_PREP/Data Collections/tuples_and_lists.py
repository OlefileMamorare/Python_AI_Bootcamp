# Tuples in Lists, lists in tuples, and nested structures:
#A tuple can contain a list as an element, and a list can contain a tuple as an element. This allows for complex data structures.

#tuple containing a list:
my_tuple = ("apple", [1, 2, 3], "banana")

capitals = [('London', 'UK', 8.98), ('Paris', 'France', 2.15), ('Berlin', 'Germany', 3.67)]

for capital in capitals:
    print(f"City: {capital[0]}, Country: {capital[1]}, Population: {capital[2]} million")

my_tuple[1].append(4)
print(my_tuple)  # Output: ('apple', [1, 2, 3, 4], 'banana')
