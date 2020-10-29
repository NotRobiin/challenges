def convert_to_hex(s: str) -> str:
    out = [str(hex(ord(c)))[2:] for c in s]

    return " ".join(out)


print(convert_to_hex("hello world") == "68 65 6c 6c 6f 20 77 6f 72 6c 64")
print(convert_to_hex("Big Boi") == "42 69 67 20 42 6f 69")
print(
    convert_to_hex("Marty Poppinson") == "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
)

