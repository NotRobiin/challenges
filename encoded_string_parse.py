def parse_code(s: str) -> dict:
    s = list(filter(lambda e: len(e), s.replace("0", " ").split(" ")))

    return {"first_name": s[0], "last_name": s[1], "id": s[2]}


print(
    parse_code("John000Doe000123")
    == {"first_name": "John", "last_name": "Doe", "id": "123"}
)

print(
    parse_code("michael0smith004331")
    == {"first_name": "michael", "last_name": "smith", "id": "4331"}
)

print(
    parse_code("Thomas00LEE0000043")
    == {"first_name": "Thomas", "last_name": "LEE", "id": "43"}
)

