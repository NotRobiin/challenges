def reverse(s):
    new_str = ""

    for char in s:
        if char.isupper():
            new_str += char.lower()
        else:
            new_str += char.upper()

    return new_str[::-1]


if __name__ == "__main__":
    print(reverse("Hello World"))
