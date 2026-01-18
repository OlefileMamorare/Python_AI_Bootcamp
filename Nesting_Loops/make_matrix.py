# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.

def make_matrix(m, n, value):
    matrix = []


    for row in range(m):
        rows = []
        for item in range(n):
            rows.append(value)

        matrix.append(rows)
        #rows.clear()

    return matrix

make_matrix(3, 5, None)
make_matrix(4, 2, "x")
make_matrix(2, 2, 0)

# Example [
# [None, None, None, None, None],
# [None, None, None, None, None],
# [None, None, None, None, None]
# ]