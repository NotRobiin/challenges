from typing import Union


class Magic:
    def replace(self, source: str, old: str, new: str) -> str:
        return source.replace(old, new)

    def str_length(self, source: str) -> int:
        return len(source)

    def trim(self, source: str) -> str:
        return source.strip()

    def list_slice(self, source: list, indexes: tuple) -> Union[list, int]:
        if len(source) == 0:
            return -1

        a = indexes[0] - 1
        b = indexes[1] if len(source) > 1 else a + 1

        return source[a:b]
