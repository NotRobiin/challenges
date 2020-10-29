def staircase(n: int) -> str:
    size = abs(n)
    output = ""

    # Make the stairs using some math.
    for i in range(size):
        output += "_" * (size - i - 1)
        output += "#" * (i + 1)
        output += "\n"

    # Flip it if 'n' is negative.
    if n < 0:
        lines = output[::-1].split("\n")
        output = []

        for j in [i for i in lines]:
            output.append(j[::-1])

        return "\n".join(output)[1:]

    return output[: len(output) - 1]


if __name__ == "__main__":
    print(
        staircase(-8),
        "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#",
    )
