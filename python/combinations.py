from itertools import permutations


def combinations(*args):
    s = 0

    for arg in args:
        if arg == 0:
            continue

        if s == 0:
            s = arg
        else:
            s *= arg

    return s


print(combinations(2, 3), combinations(2, 3) == 6)
print(combinations(3, 7, 4), combinations(3, 7, 4) == 84)
print(combinations(2, 3, 4, 5), combinations(2, 3, 4, 5) == 120)
print(combinations(6, 7, 0), combinations(6, 7, 0) == 42)
