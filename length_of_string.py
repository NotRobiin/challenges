def length(s):
    l = len(s)

    if l == 0:
        return 0

    if l == 1:
        return 1

    return length(s[1:]) + 1


if __name__ == "__main__":
    print(length("apple"))
