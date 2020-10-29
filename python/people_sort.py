def people_sort(l: list, sort_by: str) -> list:
    return sorted(l, key=lambda x: getattr(x, sort_by))
