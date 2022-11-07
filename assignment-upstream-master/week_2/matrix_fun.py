def calculate_inverse(matrix_tuple):
    coefficient = 1 / (matrix_tuple[0][0] * matrix_tuple[1][1] - matrix_tuple[0][1] * matrix_tuple[1][0])
    d = coefficient * matrix_tuple[1][1]
    b = coefficient * -matrix_tuple[0][1]
    c = coefficient * -matrix_tuple[1][0]
    a = coefficient * matrix_tuple[0][0]
    return ((d, b), (c, a))

a, b, c, d = [float(x) for x in raw_input("Enter four values: ").split()]
t = ((a, b), (c, d))
inverse_t = calculate_inverse(t)
print(t)
print(inverse_t)
