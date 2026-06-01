#dictionary is data structure that is used to store data in key-value pairs. It is also known as associative array or hash map. In Python, dictionaries are defined using curly braces {} and key-value pairs are separated by a colon :.

grade = {}

grade['John'] = 85
grade['Alice'] = 90
grade['Bob'] = 78

print(grade)  # Output: {'John': 85, 'Alice': 90, 'Bob': 78}

print(len(grade))  # Output: 3

#check if a key exists in the dictionary
if 'Alice' in grade:
    print("Alice's grade is:", grade['Alice'])  # Output: Alice's grade is: 90 

#iterate through the dictionary
for student, score in grade.items():
    print(student, "scored", score)

#keys() and values() methods
for student in grade.keys():
    print(student)

for score in grade.values():
    print(score)

#remove a key-value pair from the dictionary
del grade['Bob']    
print(grade)  # Output: {'John': 85, 'Alice': 90}

#clear the dictionary
grade.clear()
print(grade)  # Output: {}