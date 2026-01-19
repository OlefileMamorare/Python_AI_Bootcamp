# Write a function `zipper(list1, list2)` that returns a 2D list containing pairs of elements at
# the same indices. Assume lists have same length.

def zipper(list1, list2):
    matrix = []

    for i in range(len(list1)):
        pair = [list1[i], list2[i]]

        matrix.append(pair)

    return matrix

array1 = ["a", "b", "c", "d"]
array2 = [-1, -2, -3, -4]
print(zipper(array1, array2))

array3 = ["whisper", "talk", "shout"]
array4 = ["quiet", "normal", "loud"]
print(zipper(array3, array4))
