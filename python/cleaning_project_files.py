def clean_up(files: list, st: str) -> list:
    storage = {}

    for name in files:
        dot = name.index(".")
        ext = name[dot + 1 :]
        n = name[:dot]
        key = ext if st == "suffix" else n
        val = n if st == "suffix" else ext

        if key not in storage.keys():
            storage[key] = [val]
        else:
            storage[key] = storage[key] + [val]

    out = []

    for k in storage.keys():
        o = []

        for v in storage[k]:
            a = v if st == "suffix" else k
            b = k if st == "suffix" else v
            o.append("%s.%s" % (a, b))

        out.append(o)

    return out


print(
    clean_up(
        ["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"],
        "prefix",
    )
    == [["music_app.js", "music_app.png", "music_app.wav"], ["tetris.png", "tetris.js"]]
)
