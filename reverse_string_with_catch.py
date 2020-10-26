def special_reverse_string(s: str) -> str:
    out = list(s[::-1].lower().replace(" ", ""))

    for i in [i for i, char in enumerate(s) if char == " "]:
        out.insert(i, " ")

    for i in [i for i, char in enumerate(s) if char.isupper()]:
        out[i] = out[i].upper()

    return "".join(out)


print(special_reverse_string("Hello World!"))
