def max_possible(a: int, b: int) -> int:
    digits = sorted([i for i in str(b)], reverse=True)
    out = ""

    for d in str(a):
        if len(digits) > 0 and int(d) < int(digits[0]):
            out += digits[0]
            digits.pop(0)
        else:
            out += d

    return out
