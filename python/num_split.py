def num_split(num: int) -> list:
    s = str(abs(num))[::-1]
    exp = 1
    out = []

    for c in s:
        val = int(c) * exp
        exp *= 10

        out.append(-val if num < 0 else val)

    return out[::-1]


print(num_split(39))
