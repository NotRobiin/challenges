import re


def positive_sum(s: str) -> int:
    ints = [int(i) for i in re.findall(r"-?\d{1,}", s) if int(i) >= 1]

    return sum(ints)


print(positive_sum("-12#-33 13%14&-11"))
print(positive_sum("22 13%14&-11-22 13 12 0"))
