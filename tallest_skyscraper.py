def tallest_skyscraper(lst):
    columns = len(lst)
    rows = len(lst[0])
    highest = 0

    for j in range(rows):
        height = 0

        for i in range(columns):
            height += lst[i][j]

        if height > highest:
            highest = height

    return highest


print(tallest_skyscraper([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]))
print(tallest_skyscraper([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
print(tallest_skyscraper([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))
