def count_datatypes(*args):
    # No args specified.
    if len(args) == 0:
        return [0] * 6

    types = {int: 0, str: 0, bool: 0, list: 0, tuple: 0, dict: 0}

    for i in args:
        t = type(i)
        v = types[t]

        types[t] = v + 1

    return [i for i in types.values()]


if __name__ == "__main__":
    count_datatypes(1, 45, "Hi", False)  # [2, 1, 1, 0, 0, 0]
    count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1)  # [3, 0, 0, 1, 1, 0]
    count_datatypes(
        "Hello",
        "Bye",
        True,
        True,
        False,
        {"1": "One", "2": "Two"},
        [1, 3],
        {"Brayan": 18},
        25,
        23,
    )  # [2, 2, 3, 1, 0, 2]
    count_datatypes(
        4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]
    )  # [2, 0, 1, 2, 2, 0]

