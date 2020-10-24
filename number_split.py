import math


def number_split(num):
    a = int(num / 2)

    if num > 0:
        b = math.ceil(num / 2)
    else:
        b = math.floor(num / 2)

    lower = min(a, b)
    higher = max(a, b)

    return [lower, higher]


if __name__ == "__main__":
    print(number_split(-5))
