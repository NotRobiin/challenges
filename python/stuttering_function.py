def stutter(word):
    s = word[:2] + '... '

    return s + s + word + '?'


if __name__ == "__main__":
    print(stutter("incredible") == "in... in... incredible?")
    print(stutter("enthusiastic") == "en... en... enthusiastic?")
    print(stutter("outstanding") == "ou... ou... outstanding?")
