def shift_sentence(source: str) -> str:
    words = source.split(" ")

    if len(words) == 1:
        return source

    first_letters = [w[0] for w in words]
    last = first_letters[-1]
    first_letters.pop(len(first_letters) - 1)
    first_letters.insert(0, last)

    return " ".join(
        "%s%s" % (first_letters[i], words[i][1:]) for i in range(len(words))
    )
