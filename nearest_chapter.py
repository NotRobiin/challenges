def nearest_chapter(d: dict, p: int) -> str:
    keys = list(d.keys())
    closest = []

    for i, key in enumerate(keys):
        if d[key] < p:
            continue

        if i - 1 >= 0:
            closest.append(key)
            closest.append(keys[i - 1])
            break

        else:
            return key

    a = closest[0]
    b = closest[1]

    if abs(p - d[a]) <= abs(p - d[b]):
        return a

    return b


print(
    nearest_chapter({"Chapter 1": 1, "Chapter 2": 15, "Chapter 3": 37}, 10), "Chapter 2"
)

print(
    nearest_chapter(
        {
            "New Beginnings": 1,
            "Strange Developments": 62,
            "The End?": 194,
            "The True Ending": 460,
        },
        200,
    ),
    "The End?",
)

print(nearest_chapter({"Chapter 1a": 1, "Chapter 1b": 5}, 3), "Chapter 1b")

print(
    nearest_chapter(
        {"Chapter 1a": 1, "Chapter 1b": 5, "Chapter 1c": 50, "Chapter 1d": 100}, 75
    ),
    "Chapter 1d",
)

print(
    nearest_chapter(
        {
            "Chapter 1a": 1,
            "Chapter 1b": 5,
            "Chapter 1c": 50,
            "Chapter 1d": 100,
            "Chapter 1e": 200,
        },
        150,
    ),
    "Chapter 1e",
)

print(
    nearest_chapter(
        {
            "Chapter 1a": 1,
            "Chapter 1b": 5,
            "Chapter 1c": 50,
            "Chapter 1d": 100,
            "Chapter 1e": 200,
        },
        74,
    ),
    "Chapter 1c",
)

print(
    nearest_chapter(
        {
            "Chapter 1a": 1,
            "Chapter 1b": 5,
            "Chapter 1c": 50,
            "Chapter 1d": 100,
            "Chapter 1e": 200,
            "Chapter 1f": 400,
        },
        300,
    ),
    "Chapter 1f",
)

