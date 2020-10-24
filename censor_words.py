def censor_string(txt, lst, char):
    new_str = txt

    for word in lst:
        new_str = new_str.replace(word, char * len(word), 1)

    return new_str


print(
    censor_string("Today is a Wednesday!", ["Today", "a"], "-")
    == "----- is - Wednesday!"
)
print(
    censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
    == "The *** jumped **** the moon."
)
