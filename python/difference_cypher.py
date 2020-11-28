from typing import Union


def dif_ciph(source: Union[str, list]) -> Union[str, list]:
    if isinstance(source, str):
        last = source[0]
        out = [ord(last)]

        for c in source[1:]:
            diff = (ord(last) - ord(c)) * -1
            last = c

            out.append(diff)

        return out
    else:
        last = source[0]
        out = str(chr(last))

        for c in source[1:]:
            out += chr(last + c)
            last += c

        return out


print(dif_ciph([72, 33, -73, 84, -12, -3, 13, -13, -68]))
