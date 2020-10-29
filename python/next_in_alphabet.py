import string

def get_next_char(l, c, index):
    a = string.ascii_uppercase
    idx = a.index(c)
    update = False
    o = {}

    if idx == len(a) - 1:
        idx = -1
        update = True

    if update:
        index -= 1

        if index >= 0:
            o.update(get_next_char(l, l[index], index))

    if idx == -1:
        o.update({0: a[idx + 1]})
    else:
        o.update({idx: a[idx + 1]})

    return o

    # if idx == -1:
    #     return {0: a[idx + 1]}
    #
    # return {idx: a[idx + 1]}

def next_letters(s):
    if len(s) == 0:
        return "A"

    lst = [c for c in s]
    last = len(lst) - 1
    changes = get_next_char(lst, lst[last], last)

    print(changes)

    for k, v in changes.items():
        if k == -1:
            lst.insert(0, v)
        else:
            lst[k] = v

    return ''.join(lst)

"""
"ABC" -> ["A", "B", "C"] -> get_next_char("C") -> "D"
"Z" -> ["Z"] -> get_next_char("Z") -> "AA"
"""

print(next_letters("ABC"), next_letters("ABC") == "ABD")
print(next_letters("Z"), next_letters("Z") == "AA")
print(next_letters("CAZ"), next_letters("CAZ") == "CBA")
