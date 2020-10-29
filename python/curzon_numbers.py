def is_curzon(num):
    f = 2 ** num + 1
    s = 2 * num + 1

    return bool(f % s == 0)


if __name__ == "__main__":
    print(is_curzon(10))
