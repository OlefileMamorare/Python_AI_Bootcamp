#empty tuples:
empty_1 = tuple()
empty_2 = ()

#a tuple with a single element in it:
single = (10, )

nums = tuple([1,2,3])
print(nums)

#tuple unpacking:
coordinates = (37.7749 , -122.4194)
latitude , longitude = coordinates
print("latitude: " , latitude , " | " , "longitude: " , longitude)

#nested tuples:
matrix = (
    (1 , 2 , 3),
    (4 , 5 , 6),
    (67 , 8 , 9)
)

print(matrix[1][2])