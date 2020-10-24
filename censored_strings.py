def uncensor(txt, vowels):
    output = ""
    count = 0

    for i in txt:
        if i == "*":
            i = vowels[count]
            count += 1

        output += i

    return output


if __name__ == "__main__":
    uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")  # "Where did my vowels go?"
    uncensor("abcd", "")  # "abcd"
    uncensor("*PP*RC*S*", "UEAE")  # "UPPERCASE"

