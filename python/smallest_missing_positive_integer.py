def min_miss_pos(l):
    # Sorted list of only positive integers
    l = list(filter(lambda i: i > 0, sorted(l)))

    # No positive integers provided
    if not len(l):
        return 1

    last = l[0]

    # We only need to check for the first value manually
    if last != 1:
        return 1

    # Check if the difference between currently processed numbers is
    # greater than 1. If it is, we're missing a number between those
    # numbers.
    for i in l:
        if i - last > 1:
            return i - 1

        last = i

    # If there are no missing positive integers, we just make one up
    return l[len(l) - 1] + 1


# [-2, 6, 4, 5, 7, -1, 7, 1, 3, 6, 6, -2, 9, 10, 2, 2]
# sort ->
# [1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 9, 10]


print(min_miss_pos([7, 6, 5, 4, 3, 2, 1]), 8)
