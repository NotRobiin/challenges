def encrypt(s):
    vowels = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}

    new_s = ""
    s = s[::-1]

    for c in s:
        new_s += vowels[c] if c in vowels.keys() else c

    return new_s + "aca"


print(encrypt("banana"), encrypt("banana") == "0n0n0baca")
print(encrypt("karaca"), encrypt("karaca") == "0c0r0kaca")
print(encrypt("burak"), encrypt("burak") == "k0r3baca")
print(encrypt("alpaca"), encrypt("alpaca") == "0c0pl0aca")

