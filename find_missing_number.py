def missing_num(l):
    sorted_list = sorted(l)

    for i in range(1, 11):
        if i not in sorted_list:
            return i


if __name__ == "__main__":
    print(missing_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

