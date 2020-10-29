def can_see_stage(l: list) -> bool:
    columns = []

    # Flip the matrix so we operate on columns rather than rows
    for r in range(len(l[0])):
        columns.append([l[c][r] for c in range(len(l) - 1, -1, -1)])

    # Search the column for the 'too high' seat
    for column in columns:
        prev = column[0] + 1

        for value in column:
            if value >= prev:
                return False

            prev = value

    return True


if __name__ == "__main__":
    print(can_see_stage([[1, 2, 2], [1, 2, 3], [4, 4, 4]]))

"""
[1, 2, 2],
[1, 2, 3],
[4, 4, 4]
"""
