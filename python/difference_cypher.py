from typing import Union


def dif_ciph(source: Union[str, list]) -> Union[str, list]:
    last = source[0]

    if isinstance(source, str):
        out = [ord(last)]

        for c in source[1:]:
            diff = (ord(last) - ord(c)) * -1
            last = c

            out.append(diff)
    else:
        out = str(chr(last))

        for c in source[1:]:
            out += chr(last + c)
            last += c

    return out
