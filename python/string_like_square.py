def create_square(size):
    if size < 1:
        return ""

    if size == 1:
        return "#"

    border = "#" * size
    new_size = size - 2
    output = border + "\n"

    for _ in range(new_size):
        output += "#" + (" " * new_size) + "#" + "\n"

    output += border

    return output


print(create_square(-1), create_square(-1) == "")
print(create_square(0), create_square(0) == "")
print(create_square(1), create_square(1) == "#")
print(create_square(2), create_square(2) == "##\n##")
print(create_square(3), create_square(3) == "###\n# #\n###")
print(create_square(4), create_square(4) == "####\n#  #\n#  #\n####")
