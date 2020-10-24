def XO(s):
    xs = s.count("x") + s.count("X")
    os = s.count("o") + s.count("O")

    return bool(xs == os)


if __name__ == "__main__":
    print(XO("ooxx"))