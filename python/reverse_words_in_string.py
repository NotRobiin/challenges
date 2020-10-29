def reverse_words(txt):
    txt = txt.lstrip()
    txt = txt.rstrip()
    txt = txt.split(" ")
    words = [word for word in txt]

    return " ".join(words[::-1])


if __name__ == "__main__":
    print(reverse_words("the sky is blue"))
