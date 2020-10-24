def id_mtrx(n):
    # "n" is not an int.
    if not isinstance(n, int):
        return "Error"

    matrix = []

    # "n" requires no computation.
    if n == 0:
        return matrix

    size = abs(n)
    mirror = bool(n < 0)

    if mirror:
        loop_range = range(size - 1, -1, -1)
    else:
        loop_range = range(size)

    # Make matrix, fill it with 0s and 1s.
    for i in loop_range:
        row = [0] * size
        row[i] = 1

        matrix.append(row)

    return matrix


if __name__ == "__main__":
    print(id_mtrx(5))
    print(id_mtrx(-4))
    print(id_mtrx("a"))
