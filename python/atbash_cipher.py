import string


def replace_char(char):
    forbidden_chars = string.digits + string.punctuation + " "

    # Don't change digits and punctuation.
    if char in forbidden_chars:
        return char

    alphabet = list(
        string.ascii_uppercase if ord(char) < 97 else string.ascii_lowercase
    )

    index = alphabet.index(char)
    new_char = alphabet[::-1][index]

    return new_char


def atbash(s):
    return "".join([replace_char(c) for c in s])


if __name__ == "__main__":
    atbash("apple")  # "zkkov"
    atbash("Hello world!")  # "Svool dliow!"
    atbash("Christmas is the 25th of December")  # "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
