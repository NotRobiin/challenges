def char_at_pos(source, which: str):
    start_at = 1 if which == "even" else 0
    out = [source[i] for i in range(start_at, len(source), 2)]

    if type(source) == str:
        return "".join(out)

    return out


print(char_at_pos([2, 4, 6, 8, 10], "even") == [4, 8])
print(char_at_pos("EDABIT", "odd") == "EAI")
print(
    char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd")
    == ["A", "B", "T", "A", "I", "Y"]
)

