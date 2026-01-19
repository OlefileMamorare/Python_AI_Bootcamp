# Write a function `total_product(matrix)` that returns the product of all numbers in a 2D list.

def total_product(matrix):
    product = 1
    for row in matrix:
        for item in row:
            product *= item

    return product

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

total_product(array1)  # 360
total_product(array2)  # 288

