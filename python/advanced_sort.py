def advanced_sort(l: list) -> list:
    s = set()
    return [[v] * l.count(v) for v in [u for u in l if not (u in s or s.add(u))]]


advanced_sort([1, 2, 1, 2])

