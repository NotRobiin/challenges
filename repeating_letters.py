def double_char(s):
    return ''.join(c * 2 for c in s)


print(double_char("String") == "SSttrriinngg")
print(double_char("Hello World!") == "HHeelllloo  WWoorrlldd!!")
print(double_char("1234!_ ") == "11223344!!__  ")
