def rearranged_difference(n: int) -> int:
    digits = [d for d in str(n)]
    minimum = int("".join(sorted(digits)))
    maximum = int("".join(sorted(digits, reverse=True)))

    return maximum - minimum


print(rearranged_difference(972882) == 760833)
print(rearranged_difference(3320707) == 7709823)
print(rearranged_difference(90010) == 90981)
